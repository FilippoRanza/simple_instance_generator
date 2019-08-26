#! /usr/bin/python3

# Copyright (c) 2019 Filippo Ranza <filipporanza@gmail.com>


from .instance_store import InstanceStore

class SubTable:

    def __init__(self, cols, title):
        self.title = f'\\multicolumn{{{cols}}}{{|c|}}{{{title}}}\\\\\n\\hline\n'
        self.buff = ''

    def add_row(self, row):
        tmp = map(str, row)
        row = ' & '.join(tmp) + ' \\\\\n'
        self.buff += row

    def build_table(self):
        return self.title + self.buff


class LatexTable:
    def __init__(self, columns):
        head = '|'.join([' c '] * columns)
        self.head = f'\\begin{{tabular}}{{|{head}|}}\n\\hline'
        self.caption = ''
        self.cols = columns
        self.tables = []
        self.curr = None

    def add_caption(self, caption):
        self.caption += f'\\caption{{{caption}}}\\\\\n'

    def add_title(self, title):
        if self.curr:
            self.tables.append(self.curr)
        self.curr = SubTable(self.cols, title)

    def add_row(self, *row):
        self.curr.add_row(row)

    def close_table(self):
        if self.curr:
            self.tables.append(self.curr)
        out = '\\begin{table}\n\\centering\n'
        out += self.caption
        out += self.head
        out += '\n\\hline\n\\hline\n'.join(map(lambda s: s.build_table(), self.tables))
        out += f'\\hline\n\\end{{tabular}}'
        out += '\\end{table}'

        return out



class SerializeLatexTable(InstanceStore):

    def __init__(self, translate_file):
        super(SerializeLatexTable, self).__init__(translate_file)
        self.table = LatexTable(2)
        self.table.add_caption('INSERT CAPTION')

    def _hub_info_(self):
        self.table.add_title('NURSE  TITLE')
        for key in [InstanceStore.NURSES, InstanceStore.NURSES_WORK_TIME, InstanceStore.HUB]:
            real_key = self.translate.get_name(key)
            self.table.add_row(real_key, self.store[real_key])

    def _service_info_(self):
        self.table.add_title('SERVICE TITLE')
        self.table.add_row('ID', 'COST')
        key = self.translate.get_name(InstanceStore.SERVICES)
        for data in enumerate(self.store[key], start=1):
            self.table.add_row(*data)

    def _patients_requests_(self):
        self.table.add_title('PATIENTS TITLE')

        loc = self.translate.get_name(InstanceStore.ID)
        ser = self.translate.get_name(InstanceStore.REQUEST)
        self.table.add_row(loc, ser)
        key = self.translate.get_name(InstanceStore.PATIENTS)
        for patient in self.store[key]:
            self.table.add_row(patient[loc], patient[ser])



    def serialize(self):
        self._hub_info_()
        self._service_info_()
        self._patients_requests_()
        return self.table.close_table()
