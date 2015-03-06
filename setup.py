#!/usr/bin/env python3

""" Setup script for packaging and installation. """

from distutils.core import setup

with open('README.rest', 'r', encoding='utf-8') as fin:
    LONG_DESCRIPTION = fin.read()

setup(
    #
    # Basic information
    #
    name='py-unix-cmd',
    version='1.0.0',
    author='yaoguai',
    author_email='lapislazulitexts@gmail.com',
    url='https://github.com/yaoguai/py-unix-cmd',
    license='Public Domain',
    #
    # Descriptions & classifiers
    #
    description='Example of a Unix command written in Python.',
    long_description=LONG_DESCRIPTION,
    keywords='command example unix utility',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: Public Domain',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development',
        'Topic :: Utilities'],
    #
    # Included Python files
    #
    scripts=['py-unix-cmd'],
    py_modules=['py_unix_cmd'],
    data_files=[
        ('share/doc/py-unix-cmd', [
            'README.rest']),
        ('share/man/man1/py-unix-cmd.1', [
            'py-unix-cmd.1'])]
)
