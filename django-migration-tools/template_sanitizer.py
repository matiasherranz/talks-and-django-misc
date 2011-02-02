# -*- coding: utf-8 -*-

import os
import re


# Base directory path from where to walk template directories.
CURRENT_PATH = os.path.realpath(".")
TEMPLATES_PATH = CURRENT_PATH + '/trunk/expo/_templates'
print TEMPLATES_PATH

def sanitizer():
    for root, dirs, files in os.walk(TEMPLATES_PATH):
        for name in files:
            if ('.svn' not in root) and name.endswith('.html'):
                print '==> root: ', root

                print 'root: ', root
                print 'name: ', name
                print''

                make_replacements(root, name)

#            else:
#                print '==> Directory excluded: ', root
#                print''


def make_replacements(root, name):
    filepath = os.path.join(root, name)

    data = open(filepath).read()

    o = open(filepath, "w")
    o.write(re.sub("http://www.laexpo.com.ar/", "{{ SITE_URL }}/", data))
    o.close()


if __name__ == '__main__':
    sanitizer()
