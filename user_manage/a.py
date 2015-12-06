#!/usr/bin/env python

import os

path = os.path.dirname(os.path.abspath(__file__)) + '/password_file.txt'
f = open(path, 'r')
line = f.readline()
encryption = line[10:21]

count = 10
for i in range(10):
    port = f.readline().strip()[5:]
    password = f.readline().strip()[9:]
    f.readline()
    print port
    print password
