#! /usr/bin/python3

# Copyright (c) 2019 Filippo Ranza <filipporanza@gmail.com>


from .instance_store import InstanceStore

class LatexTable:
    def __init__(self, columns):
        head = '|'.join(' c ' * columns)
        self.buff = f'\\begin{{tablular}}{{|{head}|}}\n'
        self.body = ''
        self.caption = ''
        self.title = ''
        self.cols = columns

    def add_caption(self, caption):
        self.caption += f'\caption{{{caption}}}'

    def add_title(self, title):
        self.title += f'\multicolumn{self.cols}{{|c|}}{title}\\\n'

    def add_row(self, row):
        row = '&'.join(row) + '\\\n'
        self.buff += row

    def close_table(self):
        self.buff += self.caption
        self.buff += self.title
        self.buff += self.body
        self.buff += f'\end{{tabular}}'
        return self.buff

class SerializeLatexTable(InstanceStore):

    def __init__(self, translate_file):
        super(SerializeLatexTable, self).__init__(translate_file)

    def _hub_info_(self):
        table = LatexTable(2)
        table.add_title('INSERT TITLE')
        table.add_caption('INSERT CAPTION')
        return ''

    def _service_info_(self):
        return ''

    def _patients_requests_(self):
        return ''

    def serialize(self):
        out = self._hub_info_()
        out += self._service_info_()
        out += self._patients_requests_()
        return out
