#! /usr/bin/python3

class OutputInstance:

    def __init__(self, outname):
        self.name = outname
        self.buff = ''

    def set_nurse_work_time(self, time):
        self.buff += f'NURSER_WORK_TIME: {time}\n'

    def set_nurses(self, nurses):
        self.buff += f'NURSES: {nurses}\n'

    def set_world_map(self, world_map):
        self.buff += f'HUB: {world_map.hub}\n'
        self.buff += f'PATIENTS:\n'
        for i, p in enumerate(world_map.patients):
            self.buff += f'\t {i + 1} {p}\n'

    def set_services(self, services):
        self.buff += 'SERVICES:\n'
        for i, s in enumerate(services):
            self.buff += f'\t {i + 1} {s}\n'
        
    def set_requests(self, requests):
        self.buff += 'USER_REQUESTS:\n'
        for i, user in enumerate(requests.T):
            self.buff += f'\t{i + 1} {user}\n'

    def save(self):
        if self.name:
            with open(self.name, 'w') as out:
                print(self.buff, file=out)
        else:
            print(self.buff)

