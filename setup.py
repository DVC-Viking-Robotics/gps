"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
repo = 'https://github.com/DVC-Viking-Robotics/GPS_Serial'

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='gps_serial',

    use_scm_version=True,
    setup_requires=['setuptools_scm'],

    description='A threaded NMEA sentence parser for the Raspberry Pi',
    long_description=long_description,
    long_description_content_type='text/x-rst',

    # Author details
    author='Brendan Doherty',
    author_email='2bndy5@gmail.com',

    install_requires=[
        'pyserial',
    ],

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Hardware',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    # What does your project relate to?
    keywords='raspberry pi gps nmea threaded',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    # TODO: IF LIBRARY FILES ARE A PACKAGE FOLDER,
    #       CHANGE `py_modules=['...']` TO `packages=['...']`
    py_modules=['gps_serial'],

    # Specifiy your homepage URL for your project here
    url=repo,

    # Extra links for the sidebar on pypi
    project_urls={
        'Documentation': 'https://gps-serial.readthedocs.io/en/latest/',
    },
    download_url='https://github.com/DVC-Viking-Robotics/GPS_Serial/archive/master.zip',
)
