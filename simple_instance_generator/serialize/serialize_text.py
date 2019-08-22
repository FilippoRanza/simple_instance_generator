#! /usr/bin/python3

# Copyright (c) 2019 Filippo Ranza <filipporanza@gmail.com>


from .instance_store import InstanceStore


class SerializeText(InstanceStore):
    def __init__(self, translate_file):
        super(SerializeText, self).__init__(translate_file)

    @staticmethod
    def _item_to_str_(key, value):
        out = f'{key}: {value}\n'
        return out

    @staticmethod
    def _patients_to_str_(key, patients):
        out = f'{key}:\n'
        for patient in patients:
            for k, v in patient.items():
                out += f'\t{k}:{v}\n'
            out += '\n'
        return out

    def serialize(self):
        out = ''
        patients_key = self.translate.get_name('PATIENTS')
        for k, v in self.store.items():
            if k == patients_key:
                out += SerializeText._patients_to_str_(patients_key, v)
            else:
                out += SerializeText._item_to_str_(k, v)

        return out
