import os
from setuptools import setup, find_packages

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
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
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
    zip_safe=False,
    install_requires=[
        # requests 2.6.1 and higher has bug (https://github.com/kennethreitz/requests/issues/2568)
        # if SDK is required in a project affected by the above bug, it will need to also be pinned to 2.6.0
        'requests==2.6.0',
        'sphinx>=1.2.0',
    ],
    test_suite='tests',
    tests_require=[
        'mock>=1.0.1',
    ],
)
