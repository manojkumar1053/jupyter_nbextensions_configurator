#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Setup script for jupyter_nbextensions_configurator."""

from __future__ import print_function

import os
from glob import glob

from setuptools import find_packages, setup


def main():

    setup(
        name='jupyter_nbextensions_configurator',
        description=("jupyter serverextension providing configuration "
                     "interfaces for nbextensions."),
        long_description="""
The jupyter_nbextensions_configurator jupyter server extension provides
graphical user interfaces for configuring which nbextensions are enabled (load
automatically for every notebook), and display their readme files.
In addition, for extensions which include an appropriate yaml descriptor file,
the interface also provides controls to configure the extensions' options.
""",
        version='0.0.0',
        author='IPython-contrib Developers',
        author_email='joshuacookebarnes@gmail.com',
        url='https://github.com/jcb91/IPython-notebook-extensions.git',
        download_url=('https://github.com/'
                      'jcb91/jupyter_nbextensions_configurator/'
                      'tarball/0.0.0'),
        keywords=['Jupyter', 'notebook'],
        license='BSD',
        platform=['Any'],
        packages=find_packages('src'),
        package_dir={'': 'src'},
        include_package_data=True,
        py_modules=[
            os.path.splitext(os.path.basename(path))[0]
            for path in glob('src/*.py')
        ],
        install_requires=[
            'ipython_genutils',
            'jupyter_core',
            'notebook >=4.0',
            'pyyaml',
            'tornado',
            'traitlets',
        ],
        extras_require={
            'test': [
                'nose',
                'requests',
                'selenium',
            ],
            'test:python_version == "2.7"': [
                'mock',
            ],
        },
        # we can't be zip safe as we require templates etc to be accessible to
        # jupyter server
        zip_safe=False,
        entry_points={
            'console_scripts': [
                'jupyter_nbextensions_configurator = jupyter_nbextensions_configurator.application:main',  # noqa
            ],
        },
        classifiers=[
            'Intended Audience :: End Users/Desktop',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: BSD License',
            'Natural Language :: English',
            'Operating System :: OS Independent',
            'Programming Language :: JavaScript',
            'Programming Language :: Python',
            'Topic :: Utilities',
        ],
    )

if __name__ == '__main__':
    main()