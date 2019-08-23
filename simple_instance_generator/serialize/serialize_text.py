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

    def _patient_distance_to_str_(key, distance):
        out = f'{key}:\n'
        for dist in distance:
            line = ', '.join(map(lambda x: f'{x:.3f}', dist))
            out += f'\t{line}\n'
        return out

    def _hub_distance_to_str_(key, distance):
        out = f'{key}:\n\t'
        out += ', '.join(map(lambda x: f'{x:.3f}', distance)) + '\n'
        return out


    def serialize(self):
        out = ''
        patients_key = self.translate.get_name(InstanceStore.PATIENTS)
        patient_distance_key = self.translate.get_name(InstanceStore.PATIENTS_DISTANCE)
        hub_distance_key = self.translate.get_name(InstanceStore.HUB_DISTANCE)
        for k, v in self.store.items():
            if k == patients_key:
                out += SerializeText._patients_to_str_(patients_key, v)
            elif k == patient_distance_key:
                out += SerializeText._patient_distance_to_str_(patient_distance_key, v)
            elif k == hub_distance_key:
                out += SerializeText._hub_distance_to_str_(hub_distance_key, v)
            else:
                out += SerializeText._item_to_str_(k, v)

        return out
