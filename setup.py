name = 'newt.qbe'
version = '0'

install_requires = ['setuptools', 'relstorage >=2.1a2', 'newt.db >=0.5.1']
extras_require = dict(test=['manuel', 'mock', 'zope.testing'])

entry_points = """
"""

from setuptools import setup

long_description=open('README.rst').read() + '\n\n' + open('CHANGES.rst').read()

setup(
    author = 'Jim Fulton',
    author_email = 'jim@jimfulton.info',
    license = 'MIT',

    name = name, version = version,
    long_description = long_description,
    description = long_description.strip().split('\n')[1],
    packages = [name.split('.')[0], name],
    namespace_packages = [name.split('.')[0]],
    package_dir = {'': 'src'},
    install_requires = install_requires,
    zip_safe = False,
    entry_points=entry_points,
    package_data = {name: ['*.txt', '*.test', '*.html']},
    extras_require = extras_require,
    tests_require = extras_require['test'],
    test_suite = name+'.tests.test_suite',
    )
