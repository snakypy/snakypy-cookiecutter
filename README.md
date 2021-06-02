# Snakypy Cookiecutter

[![Tests](https://github.com/snakypy/snakypy-cookiecutter/actions/workflows/tests.yml/badge.svg)](https://github.com/snakypy/snakypy-cookiecutter/actions/workflows/tests.yml)
[![GitHub license](https://img.shields.io/github/license/snakypy/snakypy-cookiecutter)](https://github.com/snakypy/snakypy-cookiecutter/blob/main/LICENSE)

With **Snakypy Cookiecutter**, you can create your Python packages with a professional structure and with a lot of resources available.

## Requirements

| Required        | Required version    |   How to verify     | How to install  |
| --------------- | ------------------- | ------------------- | --------------- |
| Git             |   >= 2.25.0         | `git --version`     | [Git](http://git-scm.com/) |
| Python          |   >= 3.9            | `python --version`  | [Python](https://www.python.org/about/gettingstarted/) |
| *Poetry         |   >= 1.1.6          | `poetry --version`     | [Poetry](https://python-poetry.org/docs/#installation) |


\* If chosen at creation

## Using:

First time using:

```
$ pip install cookiecutter --user
$ cookiecutter https://github.com/snakypy/snakypy-cookiecutter.git
```

Using too many times:

```
$ cookiecutter snakypy-cookiecutter
```

After that, go to the folder with the name of the project that you entered at the time of the questions. Example:

```
$ cd my_package
```

**Create the virtual machine, activate it and install the requirements:**

```
$ python -m venv .venv
$ . .venv/bin/activate
$ pip install --upgrade pip
$ pip install -r requeriments.txt
```

or

**Create the virtual machine, activate it and install the requirements using Poetry:**

```
$ poetry shell
$ poetry install
```

There, you can start to develop your Python package.

## Developers of Snakypy Cookiecutter

If you want to build something more in this project, prepare the environment like this:

```
$ git clone https://github.com/snakypy/snakypy-cookiecutter.git
$ cd snakypy-cookiecutter
$ poetry shell
$ poetry install
```

**Tests**

Using Poetry:
```
$ poetry run tox
```

Not using Poetry:

```
$ tox
```

## License

The gem is available as open source under the terms of the [MIT License](https://github.com/snakypy/snakypy-cookiecutter/blob/master/LICENSE).
