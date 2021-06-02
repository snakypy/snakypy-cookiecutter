import os


requirementstxt_content = {"requirements.txt": """-r requirements-dev.txt
tomlkit==0.7.2
snakypy-helpers==0.2.0
{% if cookiecutter.use_cli|lower == 'y' -%}
click==8.0.1
{%- endif -%}
"""}

requirementstxt_dev_content = {"requirements-dev.txt": """twine==3.4.1
wheel==0.34.2
flake8==3.9.2
tox==3.23.1
black==21.5b2
imake==0.1.2
pre-commit==2.13.0
{% if cookiecutter.use_pytest|lower == 'y' -%}
pytest==6.2.4
pytest-runner==5.3.1
{%- endif -%}
"""}


setup_content = {"setup.py": """from setuptools import setup, find_packages
from os.path import dirname, abspath, join
from setuptools.command.develop import develop
from setuptools.command.install import install
from snakypy.{{ cookiecutter.project_slug }} import __name__, __info__


ROOT = dirname(abspath(__file__))


class PostDevelopCommand(develop):
    # Post-installation for development mode.
    def run(self):
        # PUT YOUR POST-INSTALL SCRIPT HERE or CALL A FUNCTION
        develop.run(self)


class PostInstallCommand(install):
    # Post-installation for installation mode.
    def run(self):
        # PUT YOUR POST-INSTALL SCRIPT HERE or CALL A FUNCTION
        install.run(self)


readme_rst = join(ROOT, 'README.rst')
with open(readme_rst) as f:
    long_description = f.read()

requirements = join(ROOT, 'requirements.txt')
with open(requirements) as f:
    install_requires = [i.strip().split('#', 1)[0].strip()
                        for i in f.read().strip().split('\\n')]

requirements_dev = join(ROOT, 'requirements-dev.txt')
extras_require = {}
with open(requirements_dev) as f:
    extras_require['dev'] = [i.strip().split('#', 1)[0].strip()
                             for i in f.read().strip().split('\\n')]

{%- set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
} %}

# Variables setup
{%- if cookiecutter.open_source_license in license_classifiers %}
license_ = '{{ cookiecutter.open_source_license }}',
license_classifiers = '{{ license_classifiers[cookiecutter.open_source_license] }}'
{%- endif %}
command = f'{__name__}={__name__}.cli:main'
# entry_points_line = {'console_scripts': [command]}

setup(
    name='{{ cookiecutter.project_slug | replace("_", "-") }}',
    version=__info__['version'],
    description='{{ cookiecutter.project_short_description }}',
    author='{{ cookiecutter.your_full_name }}',
    author_email='{{ cookiecutter.email }}',
    license=license_,
    maintainer='{{ cookiecutter.your_full_name }}',
    # Types: text/plain, text/x-rst, text/markdown
    long_description_content_type='text/x-rst',
    long_description=long_description,
    url='{{ cookiecutter.project_homepage }}',
    packages=find_packages(include=['{{ cookiecutter.project_slug }}',
                                    '{{ cookiecutter.project_slug }}.*']),
    install_requires=install_requires,
    scripts=[],
    extras_require=extras_require,
    classifiers=[
            'Intended Audience :: Developers',
            license_classifiers,
            {%- if cookiecutter.system == 'Posix (Linux | Mac OS X | BSD | Solaris)' %}
            'Operating System :: POSIX',{%- endif %}
            {%- if cookiecutter.system == 'DOS (Windows)' %}
            'Operating System :: Microsoft',{%- endif %}
            {%- if cookiecutter.system == 'Both' %}
            'Operating System :: POSIX',
            'Operating System :: Microsoft',{%- endif %}
            'Programming Language :: Python :: {{ cookiecutter.python_requires.split('.')[0] }}'
        ],
    python_requires='>= {{ cookiecutter.python_requires }}',
    keywords='{{ cookiecutter.project_slug.replace("_", " ") }}',
    # entry_points=entry_points_line,
    entry_points=f'''
        [console_scripts]
            {command}
    ''',
    cmdclass={
        'develop': PostDevelopCommand,
        'install': PostInstallCommand
    },
    package_data={
        '': ['LICENSE', 'requirements.txt']}
)"""}


mypy_content = """{%- if cookiecutter.use_mypy|lower == 'y/n' or cookiecutter.use_mypy|lower == 'y'-%}
[mypy]
ignore_missing_imports = True{%- endif -%}
"""


pyproject_poetry_content = """
[tool.poetry]
name = '{{ cookiecutter.project_slug }}'
version = '{{ cookiecutter.project_version }}'
description = '{{ cookiecutter.project_short_description }}'
readme = 'README.md'
authors = ['{{ cookiecutter.your_full_name }} <{{ cookiecutter.email }}>']
license = '{{ cookiecutter.open_source_license }}'
keywords=['{{ cookiecutter.keywords }}']
homepage = '{{ cookiecutter.project_homepage }}'
repository = '{{ cookiecutter.project_repository }}'
include = ['LICENSE']

packages = [
    { include = 'snakypy' }
]

{%- set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
} %}

classifiers = [
    'Intended Audience :: Developers',
    '{{ license_classifiers[cookiecutter.open_source_license] }}',
    {%- if cookiecutter.system == 'Posix (Linux | Mac OS X | BSD | Solaris)' %}
    'Operating System :: POSIX',{%- endif %}
    {%- if cookiecutter.system == 'DOS (Windows)' %}
    'Operating System :: Microsoft',{%- endif %}
    {%- if cookiecutter.system == 'Both' %}
    'Operating System :: POSIX',
    'Operating System :: Microsoft',{%- endif %}
    'Programming Language :: Python :: {{ cookiecutter.python_requires.split('.')[0] }}'
]

{% if cookiecutter.use_cli|lower == 'y' -%}
[tool.poetry.scripts]
{{ cookiecutter.project_slug }} = '{{ cookiecutter.project_slug }}.cli:main'
{% endif -%}

[tool.poetry.urls]
'Bug Tracker' = '{{ cookiecutter.project_repository }}/issues'

[tool.poetry.dependencies]
python = '^{{ cookiecutter.python_requires }}'
snakypy-helpers = '^0.2.0'
{% if cookiecutter.use_cli|lower == 'y' -%}
click = '^8.0.1'{%- endif %}

[tool.poetry.dev-dependencies]
{% if cookiecutter.use_pre_commit|lower == 'y' -%}pre-commit = '^2.13.0'{%- endif %}
flake8 = '^3.9.2'
black = '^21.5b2'
tox = '^3.23.1'
imake = '^0.1.2'
{% if cookiecutter.use_pytest|lower == 'y' -%}
pytest = '^6.2.4'
pytest-runner = '^5.3.1'{%- endif %}

[tool.black]
line-length = {{ cookiecutter.black_line_length }}
target-version = ['py38']
include = '\.pyi?$'
exclude = '''

(
  /(
      \.eggs         # exclude a few common directories in the
    | \.git          # root of the project
    | \.hg
    | \.mypy_cache
    | \.pytest_cache
    | \.tox
    | \\venv
    | build
    | venv
    | dist
    | docs
    | tmp
  )/
)
'''
{% if cookiecutter.use_isort|lower == 'y' %}
[tool.isort]
profile = "black"
multi_line_output = 3
src_paths = ["snakypy", "tests"]
line_length = 88
include_trailing_comma = true
force_grid_wrap = 0
use_parentheses = true
{% endif -%}
{% if cookiecutter.use_pytest|lower == 'y' %}

[tool.pytest.ini_options]
minversion = "6.0"
cache_dir = ".pytest_cache"
# addopts = "-ra -q"
testpaths = ["tests"]{%- endif %}

[build-system]
requires = ['poetry-core>=1.0.0']
build-backend = 'poetry.core.masonry.api'
"""

dockerfile_content = """FROM python:{{ "".join(cookiecutter.python_requires.split(".")[0]) }}
USER root
WORKDIR /snakypy/{{ cookiecutter.project_slug }}
ENV LOCAL_BIN=/root/.local/bin
RUN apt-get update \\
&& apt-get install zsh vim -y \\
&& export PATH=$PATH:$LOCAL_BIN \\
&& pip install poetry \\
&& rm -rf /var/cache/apt/*
ADD . /snakypy/{{ cookiecutter.project_slug }}
RUN cd /snakypy/{{ cookiecutter.project_slug }} \\
&& poetry install \\
CMD poetry shell
"""

travis_content = """
# Config file for automatic testing at travis-ci.com

language: python
python:
  - {{ cookiecutter.python_requires }}

# Command to install dependencies, e.g. pip install -r requirements.txt --use-mirrors
install: pip install -U tox-travis

# Command to run tests, e.g. python setup.py test
script: tox
"""

pytest_ini_content = {"pytest.ini": """
[pytest]
testpaths = tests/
"""}

pre_commit_content = """
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v3.4.0
    hooks:
    -   id: check-yaml
-   repo: https://github.com/psf/black
    rev: 20.8b1
    hooks:
    -   id: black
        types: [file]
        files: ^snakypy/*
-   repo: https://gitlab.com/pycqa/flake8
    rev: 3.9.1
    hooks:
    -   id: flake8
        types: [file]
        files: ^snakypy/

"""

manifest_in_content = {"MANIFEST.in": """include {{ cookiecutter.project_slug }}/*
include AUTHORS.rst
include CODE_OF_CONDUCT.md
include CONTRIBUTING.rst
include LICENSE
include README.rst
include requirements-dev.txt
include requirements.txt

recursive-include tests *
recursive-exclude * __pycache__
recursive-exclude * *.py[co]

recursive-include docs *.rst conf.py *.jpg *.png *.gif
"""}


setup_cfg_content = {"setup.cfg": """
[bdist_wheel]
universal = 1

[egg_info]
tag_build =
tag_svn_revision = 0
tag_date = 0

[flake8]
exclude = docs
"""}

sponsors_content = """
# These are supported funding model platforms

github: # Replace with up to 4 GitHub Sponsors-enabled usernames e.g., [user1, user2]
patreon: # Replace with a single Patreon username
open_collective: # Replace with a single Open Collective username
ko_fi: # Replace with a single Ko-fi username
tidelift: # Replace with a single Tidelift platform-name/package-name e.g., npm/babel
community_bridge: # Replace with a single Community Bridge project-name e.g., cloud-foundry
liberapay: # Replace with a single Liberapay username
issuehunt: # Replace with a single IssueHunt username
otechie: # Replace with a single Otechie username
custom: # Replace with up to 4 custom sponsorship URLs e.g., ['link1', 'link2']
"""

github_tests_content = """
name: Tests

on: [push]

jobs:
  build:

    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [{{ cookiecutter.python_requires }}]

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v1
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        {% if cookiecutter.use_poetry|lower == 'y' or cookiecutter.use_poetry == 'Y/n' -%}
        python -m pip install poetry
        poetry install{% else -%}
        pip install -r requirements.txt{%- endif %}
    - name: Test with Tox
      run: |
        {% if cookiecutter.use_poetry|lower == 'y' -%}poetry run tox{% else -%}tox{%- endif %}

"""


def formatting_code():
    """
    Formatting code with Black lib
    """
    from subprocess import check_output
    from shutil import which

    objects = (
        "snakypy.{{ cookiecutter.project_slug }}/",
        "tests/",
        "setup.py"
    )

    if which("black"):
        for element in objects:
            if os.path.exists(element):
                check_output(f"black  {element} -q",
                             shell=True, universal_newlines=True)
        return True
    return


def create_file(hook, filename, content, *args, create_path=False, path_name=""):
    """
    Function to create files template
    """
    from pathlib import Path

    if (
        hook == "Y/n"
        or hook.lower() == "y"
    ):
        if create_path:
            path = Path(path_name)
            path.mkdir(parents=True, exist_ok=True)
        with open(filename, "w") as f:
            f.write(content)
    else:
        if args:
            for obj in args:
                if (
                    hook != "Y/n"
                    or hook.lower() != "y"
                ):
                    for key in obj:
                        with open(os.path.join(key), "w") as f:
                            f.write(obj[key])


# Create Dockerfile
create_file(
    "{{ cookiecutter.use_docker }}",
    "Dockerfile",
    dockerfile_content
)

# Create travis.yml
create_file(
    "{{ cookiecutter.use_travis }}",
    "travis.yml",
    travis_content
)

# Create .github/workflows/tests.yml
create_file(
    "{{ cookiecutter.use_github_actions }}",
    ".github/workflows/tests.yml",
    github_tests_content,
    create_path=True,
    path_name=".github/workflows"
)

# Create mypy.ini
create_file(
    "{{ cookiecutter.use_mypy }}",
    "mypy.ini",
    mypy_content
)

# Create FUNDING.yml
create_file(
    "{{ cookiecutter.use_sponsor }}",
    ".github/FUNDING.yml",
    sponsors_content,
    create_path=True,
    path_name=".github"
)

# Create .pre-commit-config.yml
create_file(
    "{{ cookiecutter.use_pre_commit }}",
    ".pre-commit-config.yml",
    pre_commit_content
)

# Create pyproject.toml
create_file(
    "{{ cookiecutter.use_poetry }}",
    "pyproject.toml",
    pyproject_poetry_content,
    setup_content,
    pytest_ini_content,
    requirementstxt_content,
    requirementstxt_dev_content,
    manifest_in_content,
    setup_cfg_content
)


# Auto formatting code
formatting_code()
