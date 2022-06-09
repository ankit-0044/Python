#!/usr/bin/env python3
from platform import *
from numpy import *
import numpy
import cv2

version = python_version()
version2 = numpy.__version__
version3 = cv2.__version__

print("This is python version {}".format(version))
print("This is numpy version {}".format(version2))
print("This is opencv version {}".format(version3))
