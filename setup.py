'''LEGO LIRC :: setup.py'''

from setuptools import setup, find_packages

with open('README.rst') as f:
    README = f.read()

setup(
    name='lego-lirc',
    version='0.2.1',
    description='Control LEGO Power Functions with a Raspberry Pi and an IR LED, using LIRC.',
    long_description=README,
    author='Conor Cary',
    author_email='cary.42@osu.edu',
    url='http://github.com/iConor/lego-lirc',
    license='MIT',
    packages=find_packages(exclude=('config-files', 'docs', 'tests')),
    classifiers=(
        'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Intended Audience :: Developers',
        # 'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        # 'Operating System :: Microsoft :: Windows',
        # 'Operating System :: OS Independent',
        # 'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        # 'Programming Language :: Python :: 3',
        # 'Topic :: Communications',
        # 'Topic :: Education',
        # 'Topic :: Games/Entertainment',
        # 'Topic :: Home Automation',
        # 'Topic :: Software Development :: Embedded Systems',
        # 'Topic :: Software Development :: Libraries :: Python Modules',
        # 'Topic :: System :: Hardware :: Hardware Drivers'
    ),
    keywords=['lego', 'lirc', 'power', 'functions', 'powerfunctions', 'linux',
              'inrared', 'remote', 'control', 'raspberry', 'pi']
)
