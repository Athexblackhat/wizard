#!/usr/bin/env python3
"""
WIZARD Framework Setup Script
"""

from setuptools import setup, find_packages
import os

# Read requirements
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

# Read README
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='wizard-framework',
    version='3.0.0',
    description=' WIZARD - Advanced Cyber Security & Penetration Testing Framework',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='ATHEX BLACK HAT',
    url='https://github.com/Athexblackhat/wizard',
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'wizard=wizard:main',
            'wizard-config=wizard_config:main',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Information Technology',
        'Topic :: Security',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.8',
)