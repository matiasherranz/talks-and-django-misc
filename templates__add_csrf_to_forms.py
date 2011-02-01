# -*- coding: utf-8 -*-

import os

LINE_TO_ADD_TO_FORMS = '{% csrf_token %}\n'


# Base directory path from where to walk template directories.
CURRENT_PATH = os.path.realpath(".")
BASE_PATH = CURRENT_PATH + '/trunk/expo/'
print BASE_PATH

def csrf_form_adder():
    for root, dirs, files in os.walk(BASE_PATH):
        for name in files:
            if ('.svn' not in root) and name.endswith('.html'):
                print '==> root: ', root

                print 'root: ', root
                print 'name: ', name

                make_replacements(root, name)


def make_replacements(root, name):
    filepath = os.path.join(root, name)

    f = open(filepath, 'r')
    lines = f.readlines()
    f.close()

    new_lines = []
    for line in lines:
        new_lines.append(line)
        if  ('<form' in line) and (not '</' in line) and (not '"form' in line):
                               # exclude form closing   exclude form as a css classname
            new_lines.append(LINE_TO_ADD_TO_FORMS)
            print 'Added csrf token ok.\n'
    new_content = ''.join(new_lines)

    f = open(filepath, 'w')
    f.write(new_content)
    f.close()


if __name__ == '__main__':
    csrf_form_adder()
