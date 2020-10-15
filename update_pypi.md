# How to upload your own Python package and have custom shortcuts for your data science projects - Pypi, Anaconda, Sublime REPL


I use Anaconda, Sublime and Sublime REPL.


## Before you start

1. Make sure to insert the correct version number in `setup.py`
2. delete previous distributions in ./dist


## Build distribution

```bash
	python setup.py sdist bdist_wheel
```

## Upload to test-pypi

```bash
	python -m twine upload --repository testpypi dist/*
```

## Activate testing environment in Anaconda

```bash
	# lists previously build environments
	conda info -e

	# (optional) create environment
	conda create -n test_pypi python=3.8

	# activate test_pypi environment
	conda activate test_pypi 
```

## Configure REPL, install new package and test


switch to environment with SublimeREPL, checkout: https://stackoverflow.com/questions/20861176/how-do-i-setup-sublimerepl-with-anacondas-interpreter. 


```bash
	# install newly create package
	python -m pip install --index-url https://test.pypi.org/simple/ --no-deps example-pkg-YOUR-USERNAME-HERE
```


## Updload to Pypi and install 

```bash
twine upload dist/*

pip install [your-package]
```

**Enjoy your newly built package!**
