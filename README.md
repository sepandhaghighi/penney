<div align="center">
<img src="https://github.com/sepandhaghighi/penney/raw/logo/otherfiles/logo.png" width="260">
<h1>Penney's Game</h1>
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/built%20with-Python3-green.svg" alt="built with Python3"></a>
<a href="https://github.com/sepandhaghighi/penney"><img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/sepandhaghighi/penney"></a>
<a href="https://codecov.io/gh/sepandhaghighi/penney"><img src="https://codecov.io/gh/sepandhaghighi/penney/branch/master/graph/badge.svg"></a>
<a href="https://badge.fury.io/py/penney"><img src="https://badge.fury.io/py/penney.svg" alt="PyPI version"></a>
</div>

----------

## Overview	

Penney's game, named after its inventor Walter Penney, is a binary (head/tail) sequence generating game between two or more players. Player A selects a sequence of heads and tails (of length 3 or larger), and shows this sequence to player B. Player B then selects another sequence of heads and tails of the same length. Subsequently, a fair coin is tossed until either player A's or player B's sequence appears as a consecutive subsequence of the coin toss outcomes. The player whose sequence appears first wins [[Wikipedia](https://en.wikipedia.org/wiki/Penney%27s_game)].
							
Here we have a clone of this game that I wrote during coronavirus quarantine days.


<table>
	<tr>
		<td align="center">PyPI Counter</td>
		<td align="center"><a href="http://pepy.tech/count/penney"><img src="http://pepy.tech/badge/penney"></a></td>
	</tr>
	<tr>
		<td align="center">GitHub Stars</td>
		<td align="center"><a href="https://github.com/sepandhaghighi/penney"><img src="https://img.shields.io/github/stars/sepandhaghighi/penney.svg?style=social&label=Stars"></a></td>
	</tr>
</table>



<table>
	<tr> 
		<td align="center">Branch</td>
		<td align="center">master</td>	
		<td align="center">dev</td>	
	</tr>
	<tr>
		<td align="center">CI</td>
		<td align="center"><img src="https://github.com/sepandhaghighi/penney/actions/workflows/test.yml/badge.svg?branch=master"></td>
		<td align="center"><img src="https://github.com/sepandhaghighi/penney/actions/workflows/test.yml/badge.svg?branch=dev"></td>
	</tr>
</table>


<table>
	<tr> 
		<td align="center">Code Quality</td>	
		<td align="center"><a href="https://www.codefactor.io/repository/github/sepandhaghighi/penney"><img src="https://www.codefactor.io/repository/github/sepandhaghighi/penney/badge" alt="CodeFactor" /></a></td>	
		<td align="center"><a href="https://app.codacy.com/gh/sepandhaghighi/penney/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/d95056b079c844f587dd81914ed9d300"/></a></td>
	</tr>
</table>

## Installation	

### Source Code
- Download and install [Python3.x](https://www.python.org/downloads/) (>=3.7)
	- [x] Select `Add to PATH` option
	- [x] Select `Install pip` option
- Download [Version 0.4](https://github.com/sepandhaghighi/penney/archive/v0.4.zip) or [Latest Source ](https://github.com/sepandhaghighi/penney/archive/dev.zip)
- Run `pip install .`			

### PyPI
- Check [Python Packaging User Guide](https://packaging.python.org/installing/)     
- Run `pip install penney==0.4`

### Exe Version (Windows)
- Download [Exe-Version 0.4](https://github.com/sepandhaghighi/penney/releases/download/v0.4/Penney-0.4.exe)
- Run `Penney-0.4.exe`

## How to Play

- You can use `penney`, `python -m penney` or `Penney.exe` to run this program

<div align="center">
<img src="https://github.com/sepandhaghighi/penney/raw/master/otherfiles/help.gif" alt="Screen Record">
<p>Screen Record</p>
</div>

## Try Penney in Your Browser!

You can play Penney's game online in interactive Jupyter Notebooks via the Binder or Colab services! Try it out now!:


[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/sepandhaghighi/penney/master)

[![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sepandhaghighi/penney/blob/master)

- Open `Notebook.ipynb`

## Contribution			

Changes and improvements are more than welcome! ❤️ Feel free to fork and open a pull request.		


Please consider the following :


1. Fork it!
2. Create your feature branch (under `dev` branch)
3. Add your functions/methods to proper files
4. Add standard `docstring` to your functions/methods
5. Add tests for your functions/methods (test cases in `test` folder)
6. Pass all CI tests
7. Update `CHANGELOG.md`
	- Describe changes under `[Unreleased]` section
8. Submit a pull request into `dev` (please complete the pull request template)

## Issues & Bug Reports			

Just open an issue and describe it. I'll check it ASAP!							
or send an email to [me@sepand.tech](mailto:me@sepand.tech "me@sepand.tech"). 

* Please complete the issue template


## References			

<blockquote>1- Penney, Walter. "Problem 95: penney-ante." Journal of Recreational Mathematics 7 (1974): 321.</blockquote>

<blockquote>2- Zajkowski, Krzysztof. "Penney's game between many players." arXiv preprint arXiv:1212.3973 (2012). </blockquote>

<blockquote>3- Guy, R. K., and John Horton Conway. Winning Ways for your Mathematical Plays. Academic Press, London, 1982. </blockquote>

<blockquote>4- Humble, Steve, and Yutaka Nishiyama. "Humble-Nishiyama Randomness Game-A New Variation on Penney's Coin Game." (2010). </blockquote>	

## Show Your Support
								
<h3>Star This Repo</h3>					

Give a ⭐️ if this project helped you!

<h3>Donate to Our Project</h3>	

<h4>Bitcoin</h4>
1KtNLEEeUbTEK9PdN6Ya3ZAKXaqoKUuxCy
<h4>Ethereum</h4>
0xcD4Db18B6664A9662123D4307B074aE968535388
<h4>Litecoin</h4>
Ldnz5gMcEeV8BAdsyf8FstWDC6uyYR6pgZ
<h4>Doge</h4>
DDUnKpFQbBqLpFVZ9DfuVysBdr249HxVDh
<h4>Tron</h4>
TCZxzPZLcJHr2qR3uPUB1tXB6L3FDSSAx7
<h4>Ripple</h4>
rN7ZuRG7HDGHR5nof8nu5LrsbmSB61V1qq
<h4>Binance Coin</h4>
bnb1zglwcf0ac3d0s2f6ck5kgwvcru4tlctt4p5qef
<h4>Tether</h4>
0xcD4Db18B6664A9662123D4307B074aE968535388
<h4>Dash</h4>
Xd3Yn2qZJ7VE8nbKw2fS98aLxR5M6WUU3s
<h4>Stellar</h4>		

GALPOLPISRHIYHLQER2TLJRGUSZH52RYDK6C3HIU4PSMNAV65Q36EGNL						


