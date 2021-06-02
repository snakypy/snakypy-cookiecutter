"""
{{ cookiecutter.project_name }}
~~~~~~~~~~~~~~~~~

{{ cookiecutter.project_short_description }}


For more information, access: 'https://github.com/{{ cookiecutter.github_profile }}/{{ cookiecutter.project_slug.replace("_","-") }}'

:copyright: Copyright 2020-present, see AUTHORS.
:license: {{ cookiecutter.open_source_license }}, see LICENSE for details.
"""
from snakypy.helpers.files import eqversion
from os.path import abspath, dirname, join
from snakypy.helpers.files import eqversion


__info__ = {
    "name": "{{ cookiecutter.project_name }}",
    "version": "{{ cookiecutter.project_version }}"
}


# Keep the versions the same on pyproject.toml and __init__.py
pyproject = join(dirname(abspath(__file__)), "../..", "pyproject.toml")
eqversion(pyproject, __info__["version"])
