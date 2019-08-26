#! /usr/bin/python3

# Copyright (c) 2019 Filippo Ranza <filipporanza@gmail.com>

import yaml


class Translate:

    def __init__(self, file_name):
        if file_name:
           with open(file_name) as file:
               self.translate = yaml.safe_load(file)
        else:
            self.translate = {}

    def get_name(self, key):
        out = self.translate.get(key, key)
        return out

