from setuptools import setup, find_packages


APP_NAME = 'pylearn'
VERSION = '0.1.0'
AUTHOR = 'James Hibbard'

setup(
    name=APP_NAME,
    version=VERSION,
    author=AUTHOR,
    description="Python workshop modules",
    license="MIT",
    install_requires=[
        'Click==7.0',
        'appdirs==1.4.3',
    ],
    extras_require={
        'tests': 'pytest==3.8.1',
    },
    packages=find_packages(),
    entry_points='''
        [console_scripts]
        pylearn=pylearn.runner:cli
    ''',
)
