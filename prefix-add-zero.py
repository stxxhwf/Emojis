#!/usr/bin/python

import os;
import fnmatch;

#无语了

for file in os.listdir('.'):
    if not fnmatch.fnmatch(file, "*.py"):
        os.rename(file, "0" + file)
