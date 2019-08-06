#! /usr/bin/python3

class ContainerWrapper:
    def __init__(self, unique):
        self.u = unique
        if unique:
            self.data = set()
        else:
            self.data = list()

    def insert(self, data):
        if self.u:
            self.data.add(data)
        else:
            self.data.append(data)

    def __len__(self):
        return len(self.data)