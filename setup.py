import os
from setuptools import setup

version_file = open(os.path.join(os.path.dirname(__file__), 'VERSION'))
version = version_file.read().strip()
README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

setup(
    name='canvas_python_sdk',
    version=version,
    description='A python sdk for the canvas LMS api',
    author='Harvard University',
    author_email='some_email_tbd@Harvard.edu',
    url='https://github.com/Harvard-University-iCommons/canvas_python_sdk',
    packages=['canvas_sdk'],
    long_description=README,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        'Operating System :: OS Independent',
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development",
    ],
    keywords='canvas api sdk LMS',
    license='MIT',
    install_requires=[
    ],
    test_suite='tests',
    tests_require=[
        'mock>=1.0.1',
    ],
)
