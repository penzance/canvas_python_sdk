import os
from setuptools import setup

setup(
    name='canvas_python_sdk',
    version='0.0.1',
    description='A python sdk for the canvas LMS api',
    author='Harvard University',
    author_email='some_email_tbd@Harvard.edu',
    url='https://github.com/Harvard-University-iCommons/canvas_python_sdk/wiki',
    packages=['canvas_python_sdk'],
      long_description=open('README.md').read(),
      classifiers=[
          "License :: OSI Approved :: MIT License",
          'Operating System :: OS Independent',
          "Programming Language :: Python",
          "Development Status :: 4 - Beta",
          "Intended Audience :: Developers",
          "Topic :: Internet",
      ],
      keywords='canvas api sdk LMS',
      license='MIT',
      install_requires=[
        'setuptools',
      ],
      )
