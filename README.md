# LibIndic Shingling


[![Build Status](https://travis-ci.org/libindic/shingling.svg?branch=master)](https://travis-ci.org/libindic/shingling)
[![Coverage Status](https://coveralls.io/repos/github/libindic/shingling/badge.svg?branch=master)](https://coveralls.io/github/libindic/shingling?branch=master)


LibIndic's shingling module may be used to generate word shinglings from a text.
It is built on top of the N-Gram module.

## Installation
1. Clone the repository `git clone https://github.com/libindic/shingling.git`
2. Change to the cloned directory `cd shingling`
3. Run setup.py to create installable source `python setup.py sdist`
4. Install using pip `pip install dist/libindic-shingling*.tar.gz`

## Usage
```
>>> from libindic.shingling import Shingling
>>> instance = Shingling()
>>> shinglings = instance.wshingling(u"ഇത് ഒരു നല്ല കാര്യമാണ് ഇത് ഒരു", window_size = 2)
>>> for shingling in shinglings:
...     print(" ".join(shingling))
... 
ഇത് ഒരു
ഒരു നല്ല
നല്ല കാര്യമാണ്
കാര്യമാണ് ഇത്
```

For more details read the [docs](http://shingling.rtfd.org/)
