# Copyright (c) 2016, Matt Layman
"""
HTTPony is an HTTP request listener that pretty prints requests to a terminal.
"""

from setuptools import find_packages, setup

from httpony import __version__


if __name__ == '__main__':
    with open('docs/releases.rst', 'r') as f:
        releases = f.read()

    long_description = __doc__ + '\n\n' + releases

    install_requires = [
        'httpie>=0.9.4',
        'Werkzeug',
    ]

    setup(
        name='httpony',
        version=__version__,
        url='https://github.com/mblayman/httpony',
        license='BSD',
        author='Matt Layman',
        author_email='matthewlayman@gmail.com',
        description='A simple HTTP request listener and pretty printer',
        long_description=long_description,
        packages=find_packages(),
        entry_points={
            'console_scripts': ['httpony = httpony.server:main'],
        },
        include_package_data=True,
        zip_safe=False,
        platforms='any',
        install_requires=install_requires,
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: Implementation :: PyPy',
            'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
            'Topic :: Software Development :: Testing',
        ],
        keywords=[
            'HTTP',
            'Pretty print',
            'JSON',
            'XML',
        ],
    )
