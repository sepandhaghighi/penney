<div align="center">
<img src="https://github.com/sepandhaghighi/penney/raw/master/otherfiles/logo.png" width="164px" height="297px">
<h1>Penney's Game</h1>
</div>

----------

## Overview	

Penney's game, named after its inventor Walter Penney, is a binary (head/tail) sequence generating game between two or more players. Player A selects a sequence of heads and tails (of length 3 or larger), and shows this sequence to player B. Player B then selects another sequence of heads and tails of the same length. Subsequently, a fair coin is tossed until either player A's or player B's sequence appears as a consecutive subsequence of the coin toss outcomes. The player whose sequence appears first wins.
Here we have a friendly clone of this game that I wrote during coronavirus quarantine days.
## Installation	

### Source Code
- Download and install [Python3.x](https://www.python.org/downloads/) (>=3.5)
	- [x] Select `Add to PATH` option
	- [x] Select `Install pip` option
- Download [Version 0.1](https://github.com/sepandhaghighi/penney/archive/v0.1.zip) or [Latest Source ](https://github.com/sepandhaghighi/penney/archive/develop.zip)
- Run `pip install -r requirements.txt` or `pip3 install -r requirements.txt` (Need root access)
- Run `python3 setup.py install` or `python setup.py install` (Need root access)				

### PyPI

- Check [Python Packaging User Guide](https://packaging.python.org/installing/)     
- Run `pip install penney` or `pip3 install penney` (Need root access)

### Easy Install

- Run `easy_install --upgrade penney` (Need root access)

### Exe Version (Only Windows)
- Download [Penney 0.1](https://github.com/sepandhaghighi/penney/releases/download/v0.1/Penney-0.1.exe)
- Run `Penney-0.1.exe`

## How to Play

- Open `CMD` (Windows) or `Terminal` (UNIX)
- Run `python -m penney` or `python3 -m penney` (or run `Penney.exe`)



## Contribution			

Changes and improvements are more than welcome! ❤️ Feel free to fork and open a pull request.		


Please consider the following :


1. Fork it!
2. Create your feature branch (under `dev` branch)
3. Add your functions/methods to proper files
4. Pass all CI tests
5. Update `CHANGELOG.md`
	- Describe changes under `[Unreleased]` section
6. Submit a pull request into `dev` (please complete the pull request template)

## Issues & bug reports			

Just fill an issue and describe it. I'll check it ASAP!							
or send an email to [sepand@pycm.ir](mailto:sepand@pycm.ir "sepand@pycm.ir"). 

* Please complete the issue template


## Dependencies

<table>
	<tr> 
		<td align="center">master</td>	
		<td align="center">dev</td>	
	</tr>
	<tr>
		<td align="center"><a href="https://requires.io/github/sepandhaghighi/penney/requirements/?branch=master"><img src="https://requires.io/github/sepandhaghighi/penney/requirements.svg?branch=master" alt="Requirements Status" /></a></td>
		<td align="center"><a href="https://requires.io/github/sepandhaghighi/penney/requirements/?branch=dev"><img src="https://requires.io/github/sepandhaghighi/penney/requirements.svg?branch=dev" alt="Requirements Status" /></a></td>
	</tr>
</table>