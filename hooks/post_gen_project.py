#!/usr/bin/env python

import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

def remove_dir(filepath):
    os.rmdir(os.path.join(PROJECT_DIRECTORY, filepath))

if __name__ == '__main__':

    if '{{ cookiecutter.models }}' == 'n':
        remove_dir('models/')

    if '{{ cookiecutter.tests }}' == 'n':
        remove_dir('tests/')
