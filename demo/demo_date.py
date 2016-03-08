#!/usr/bin/python
# -*- coding: UTF-8 -*-

import datetime;
from datetime import date

date = datetime.date;
d = date.fromordinal(730920)
print(d.strftime("%d/%m/%y"))
print (d)