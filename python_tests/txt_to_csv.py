#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import csv

un = "\u001A"

csv_file = "heble.csv"
txt_file = "text_file"

## just read csv
with open(txt_file, "w") as my_output_file:
    with open(csv_file, "r") as my_input_file:
        for i, row in enumerate(csv.reader(my_input_file)):
            if i<75:
                my_output_file.write(",".join(row) + '\n')
            else:
                break
    my_output_file.close()

## with pandas read csv
import pandas as pd

d = pd.read_csv(csv_file, index_col=None, header=0, delimiter=chr(ord(unicode(un))))

d.to_csv("find_result.csv", sep=',', index=False, encoding='utf-8')
