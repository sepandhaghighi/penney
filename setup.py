# -*- coding: utf-8 -*-
"""Setup module."""
from typing import List
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


def get_requires() -> List[str]:
    """Read requirements.txt."""
    with open("requirements.txt", "r") as f:
        requirements = f.read()
    return list(filter(lambda x: x != "", requirements.split()))


def read_description() -> str:
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
    version='0.5',
    description="Penney's game",
    long_description=read_description(),
    long_description_content_type='text/markdown',
    author='Sepand Haghighi',
    author_email='me@sepand.tech',
    url='https://github.com/sepandhaghighi/penney',
    keywords="penney probability game fun terminal",
    project_urls={
        'Source': 'https://github.com/sepandhaghighi/penney',
        'Tracker': 'https://github.com/sepandhaghighi/penney/issues',
    },
    install_requires=get_requires(),
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Games/Entertainment',
        'Topic :: Games/Entertainment :: Simulation',
        'Topic :: Games/Entertainment :: Turn Based Strategy',
    ],
    license='MIT',
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'penney = penney.__main__:main',
        ]},
)
