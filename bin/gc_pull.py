#! /usr/bin/env python

import sys
import os
import shutil

modules = sys.argv[1:]
installed = []

# first lets check the local file system.
hit = 0
print ''

if os.environ.get('GENIE_COMPONENT_LIBRARY', False):
    print 'found local lib'
    path = os.environ.get('GENIE_COMPONENT_LIBRARY')

    if not modules:
        print 'Modules:'
        for j in os.listdir(path):
            print '    ', j

    else:
        for i in modules:
            if i.startswith('-'):
                continue

            fdir = path + i.split('/',1)[0]
            fname = i.split('/', 1)[-1]

            if os.path.isdir(path + i):
                fdir = path + i
                fname = ''

            if os.path.isfile(path + i) and i not in installed:
                if os.path.exists(path + i) and '-f' in sys.argv:
                    print '    installing', i
                    shutil.copy(path + i, '.')
                else:
                    print '    skipping', i, 'add -f to force add.'
                installed.append(i)

            elif os.path.isdir(fdir):
                if os.path.isdir(fdir):
                    print "Options:"
                    for j in os.listdir(fdir):
                        if j.startswith(fname):
                            print '    ', j


print ''
