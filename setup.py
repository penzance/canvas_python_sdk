import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'VERSION')) as v_file:
    version = v_file.read().strip()

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

setup(
    name='canvas_python_sdk',
    version=version,
    description='A python SDK for Instructure\'s Canvas LMS API',
    author='Harvard University',
    author_email='tlt-opensource@g.harvard.edu',
    url='https://github.com/penzance/canvas_python_sdk',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    long_description=README,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        'Operating System :: OS Independent',
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development",
    ],
    keywords='canvas api sdk LMS',
    license='MIT',
    zip_safe=False,
    install_requires=[
        'future',
        'requests',
        'six',
    ],
    extras_require={
        'docs': ['sphinx>=1.2.0'],
    },
    # TODO: `from collections import ABC` imports will break in python 3.8.
    #       They are present both in this library and in the `futurize`
    #       library which maintains cross-compatibility with python 2 and 3.
    #       In order to move to python 3.8, we will likely need to discontinue
    #       support for python 2 in this library.
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*, <3.8',
    test_suite='tests',
    tests_require=[
        'mock>=1.0.1',
    ],
)
