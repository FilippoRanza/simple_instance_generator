#! /usr/bin/python3

# Copyright (c) 2019 Filippo Ranza <filipporanza@gmail.com>


class Serializer:

    def serialize(self, store) -> str:
        raise NotImplementedError()
