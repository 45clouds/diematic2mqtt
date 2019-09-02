#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='diematic2mqtt',
    version='1.1.0',
    author='45clouds',
    author_email='hi@45clouds.com',
    packages= find_packages(),
    scripts=['bin/poll_isystem_mqtt.py', 'bin/dump_isystem.py'],
    url='https://github.com/45clouds/diematic2mqtt',
    install_requires=['MinimalModbus', 'paho-mqtt'],
    license='LICENSE',
    description='Request De Dietrich iSystem boiler and send value to mqtt',
    classifiers=['Programming Language :: Python :: 2.7']
)
