#! /usr/bin/env python

import os
import json

try:
    os.mkdir('build')
except:
    pass

import urllib
print 'downloading latest genie library...'
urllib.urlretrieve(
    url='https://raw.githubusercontent.com/graham/genie/master/build/genie.min.js', 
    filename='build/genie.min.js')

print 'downloading latest jquery...'
urllib.urlretrieve(
    url='http://code.jquery.com/jquery-2.1.1.min.js',
    filename='build/jquery.js')

def get_components(path):
    components = []
    for i in os.listdir(path):
        rpath = path + '/' + i
        if rpath.startswith('.'):
            pass
        elif rpath.endswith('~'):
            pass
        elif os.path.isdir(rpath):
            components.extend(get_components(rpath))
        elif rpath.endswith('.html') or rpath.endswith('.txt'):
            components.append(rpath)
            print '  found:', rpath
    return components

print 'finding components...'    
comps = get_components('components')
print ''

comps.sort()

print 'saving...',
f = open('build/list.json', 'w')
f.write(json.dumps({'list':comps}, indent=True))
f.close()
print '#done\n'
