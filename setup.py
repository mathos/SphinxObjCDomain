# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

long_desc = '''
This package contains an objective-c Sphinx extension.

It needs Sphinx 1.0 or newer.

Detail document: http://packages.python.org/
'''

requires = ['Sphinx>=1.0','ply>=3.4']

setup(
    name='sphinxcontrib-objc',
    version='0.1',
    url='',
    download_url='',
    license='BSD',
    author='Mathos Marcer',
    author_email='mathos dot marcer at gmail dot com',
    description='Sphinx extension for objective-c',
    long_description=long_desc,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
)
