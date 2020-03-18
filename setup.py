# -*- coding: utf-8 -*-
"""Setup module."""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


MINIMAL_DESCRIPTION = '''
Penney's game, named after its inventor Walter Penney, is a binary (head/tail) sequence generating game between two or more players.
Player A selects a sequence of heads and tails (of length 3 or larger), and shows this sequence to player B. Player B then
selects another sequence of heads and tails of the same length. Subsequently, a fair coin is tossed until either player A's
or player B's sequence appears as a consecutive subsequence of the coin toss outcomes. The player whose sequence appears first wins.
'''


def get_requires():
    """Read requirements.txt."""
    requirements = open("requirements.txt", "r").read()
    return list(filter(lambda x: x != "", requirements.split()))


def read_description():
    """Read README.md and CHANGELOG.md."""
    try:
        with open("README.md") as r:
            description = "\n"
            description += r.read()
        with open("CHANGELOG.md") as c:
            description += "\n"
            description += c.read()
        return description
    except Exception:
        return MINIMAL_DESCRIPTION


setup(
    name='penney',
    packages=['penney'],
    version='0.1',
    description="Penney's game",
    long_description=read_description(),
    long_description_content_type='text/markdown',
    author='Sepand Haghighi',
    author_email='sepand@pycm.ir',
    url='https://github.com/sepandhaghighi/penney',
    keywords="penney probability game",
    project_urls={
        'Source': 'https://github.com/sepandhaghighi/penney',
        'Tracker': 'https://github.com/sepandhaghighi/penney/issues',
    },
    install_requires=get_requires(),
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Games/Entertainment',
        'Topic :: Games/Entertainment :: Simulation',
    ],
    license='MIT',
    include_package_data=True
)
