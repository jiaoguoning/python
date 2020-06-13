#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 07:15:35 2020

@author: jiaoguoning
"""

import csv
import numpy as np 
import matplotlib.pyplot as plt 

with open('appendixf.csv', 'rt') as fin:
    cin = csv.reader(fin)
    villains = [row for row in cin]

nplist_appendix = np.array(villains)
print(nplist_appendix) 
# 实验git 