# -*- coding: utf-8 -*-

__author__ = "Matias Herranz (matiasherranz@gmail.com)"
__version__ = "0.1"


import os
import re


# Base directory path from where to walk template directories.
# Set the paths according to your project.
CURRENT_PATH = os.path.realpath(".")
BASE_PATH = CURRENT_PATH + '/trunk/'
print BASE_PATH

def sanitizer():
    for root, dirs, files in os.walk(BASE_PATH):
        for name in files:
            if ('.svn' not in root) and (name == 'models.py'):
                print '==> root: ', root

                print 'root: ', root
                print 'name: ', name
                print''

                make_replacements(root, name)


def make_replacements(root, name):
    filepath = os.path.join(root, name)

    data = open(filepath).read()

    o = open(filepath, "w")
    # uncomment here to change one or another:
    # this should be a parameter of the function. A TODO :-)
#    o.write(re.sub("maxlength", "max_length", data))
    o.write(re.sub("FloatField", "DecimalField", data))
    o.close()


if __name__ == '__main__':
    sanitizer()
