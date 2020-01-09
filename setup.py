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
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development",
    ],
    keywords='canvas api sdk LMS',
    license='MIT',
    zip_safe=False,
    install_requires=[
        'requests',
    ],
    extras_require={
        'docs': ['sphinx>=1.2.0'],
    },
    python_requires='>=3.6',
    test_suite='tests',
    tests_require=[
        'requests',
    ],
)
