#! /usr/bin/python3

# Copyright (c) 2019 Filippo Ranza <filipporanza@gmail.com>


from argparse import ArgumentParser

from simple_instance_generator import *

DEFAULT_TIME_SLOT_SIZE = 15

DEFAULT_MIN_TIME_SLOT = 1
DEFAULT_MAX_TIME_SLOT = 8

# 6 hours
DEFAULT_NURSE_WORK_TIME = 360

DEFAULT_SIZE_X = 1000
DEFAULT_SIZE_Y = 1000


DEFAULT_VARIANCE = 1

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
    out.add_argument('-o', '--output',
                     help='output file name')


    out.add_argument('-m', '--mean', default=0, type=int,
                     help='set mean number of request per day, default half of patient number')

    out.add_argument('-v', '--variance', default=DEFAULT_VARIANCE, type=int,
                     help=f'set variance of request per day, default {DEFAULT_VARIANCE}')

    out.add_argument('-w', '--working', default=DEFAULT_NURSE_WORK_TIME,
                     help=f'set nurse work time, in minutes, default {DEFAULT_NURSE_WORK_TIME}',
                     type=int)

    out.add_argument('--tmin', type=int, default=DEFAULT_MIN_TIME_SLOT,
                     help=f'minimum number of time slots, default {DEFAULT_MIN_TIME_SLOT}')

    out.add_argument('--tmax', type=int, default=DEFAULT_MAX_TIME_SLOT,
                     help=f'maximum number of time slots, default {DEFAULT_MAX_TIME_SLOT}')

    out.add_argument('--sizex', type=int, default=DEFAULT_SIZE_X,
                     help=f'set number of columns in the grid, default {DEFAULT_SIZE_X}')

    out.add_argument('--sizey', type=int, default=DEFAULT_SIZE_Y,
                     help=f'set number of rows in the grid, default {DEFAULT_SIZE_Y}')

    out.add_argument('--non-unique', default=True,
                     action='store_false' ,
                     help='allow non unique patients')

    return out


def check_args(args):
    if args.mean > args.patients:
        raise ValueError(f'not enough patient {args.patients} for given mean {args.mean}')


def generate_instance(args):
    world = map_generator(args.sizex, args.sizey, args.patients, args.non_unique, 1)
    services = service_generator(args.tmin, args.tmax, args.time, args.services)
    requests = request_generator(world, services, args.days, args.mean, args.variance)

    writer = OutputInstance(args.output)
    writer.set_nurses(args.nurses)
    writer.set_nurse_work_time(args.working)
    writer.set_world_map(world)
    writer.set_services(services.service)
    writer.set_requests(requests)
    writer.save()


def main():
    parser = conf_arg_parser()
    args = parser.parse_args()
    if args:
        try:
            check_args(args)
        except ValueError as err:
            print(err)
            print('exit now')
        else:
            generate_instance(args)

if __name__ == "__main__":
    main()
