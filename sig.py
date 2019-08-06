#! /usr/bin/python3

from argparse import ArgumentParser

from simple_instance_generator import *

DEFAULT_TIME_SLOT_SIZE = 15

def conf_arg_parser():
    out = ArgumentParser()
    
    out.add_argument('-d', '--days', required=True,
                     type=int, help='number of days')
    out.add_argument('-p', '--patients', required=True,
                     type=int, help='number of patients')
    out.add_argument('-s', '--services', required=True,
                     type=int, help='number of services')
    out.add_argument('-n', '--nurses', required=True,
                     type=int, help='number of nurses')
    out.add_argument('-t', '--time', default=DEFAULT_TIME_SLOT_SIZE,
                     type=int, 
                     help=f'time slot length, in minutes, default {DEFAULT_TIME_SLOT_SIZE}')

    return out


def generate_instance(args):
    world = map_generator(1000, 1000, args.patients, True, 1)
    services = service_generator(1, 10, args.time, args.services)
    requests = request_generator(world, services, args.days)

    writer = OutputInstance('test.txt')
    writer.set_world_map(world)
    writer.set_nurses(args.nurses)
    writer.set_services(services)
    writer.set_requests(requests)
    writer.save()


def main():
    parser = conf_arg_parser()
    args = parser.parse_args()
    if args:
        generate_instance(args)

if __name__ == "__main__":
    main()

