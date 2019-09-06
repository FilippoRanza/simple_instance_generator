#! /usr/bin/python3

# Copyright (c) 2019 Filippo Ranza <filipporanza@gmail.com>

from abc import abstractmethod, ABC

class ContainerStrategy(ABC):
    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def insert(self, data):
        pass

    @abstractmethod
    def get_collection(self):
        pass


class UniqueStrategy(ContainerStrategy):
    def __init__(self):
        self.coll = set()
    
    def __len__(self):
        return len(self.coll)

    def insert(self, data):
        self.coll.add(data)

    def get_collection(self):
        return self.coll

class ListStrategy(ContainerStrategy):
    def __init__(self):
        self.coll = list()

    def __len__(self):
        return len(self.coll)

    def insert(self, data):
        self.coll.append(data)

    def get_collection(self):
        return self.coll

def container_factory(unique):
    if unique:
        out = UniqueStrategy()
    else:
        out = ListStrategy()
    return out