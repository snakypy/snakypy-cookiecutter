{%- if cookiecutter.add_badges|lower == 'y' -%}

{%- if cookiecutter.use_github_actions|lower == 'y' -%}
.. image:: https://github.com/{{ cookiecutter.github_profile }}/{{ cookiecutter.project_slug | replace("_", "-") }}/workflows/Tests/badge.svg
    :target: https://github.com/{{ cookiecutter.github_profile }}/{{ cookiecutter.project_slug | replace("_", "-") }}{% endif -%}

.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.project_slug | replace("_", "-") }}.svg
    :target: https://pypi.python.org/pypi/{{ cookiecutter.project_slug | replace("_", "-") }}

{%- if cookiecutter.use_travis|lower == 'y' -%}
.. image:: https://travis-ci.com/{{ cookiecutter.github_profile }}/{{ cookiecutter.project_slug | replace("_", "-") }}.svg?branch=master
    :target: https://travis-ci.com/{{ cookiecutter.github_profile }}/{{ cookiecutter.project_slug | replace("_", "-") }}{% endif -%}

.. image:: https://img.shields.io/pypi/wheel/{{ cookiecutter.project_slug | replace("_", "-") }}
    :alt: PyPI - Wheel

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black

.. image:: https://img.shields.io/github/issues-raw/{{ cookiecutter.github_profile }}/{{ cookiecutter.project_slug | replace("_", "-") }}
    :alt: GitHub issues

.. image:: https://img.shields.io/github/license/{{ cookiecutter.github_profile }}/{{ cookiecutter.project_slug | replace("_", "-") }}
    :alt: GitHub license
    :target: https://github.com/{{ cookiecutter.github_profile }}/{{ cookiecutter.project_slug | replace("_", "-") }}/blob/master/LICENSE
{% endif -%}

Requirements
------------

To work correctly, you will first need:

* `python`_ (v{{ cookiecutter.python_requires }} or recent) must be installed.
* `pip`_ (v20.0 or recent) must be installed.

Installing
----------

Globally:

.. code-block:: shell

    $ sudo pip install {{ cookiecutter.project_slug | replace("_", "-") }}

For the user:

.. code-block:: shell

    $ pip install {{ cookiecutter.project_slug | replace("_", "-") }} --user


Using
-----

Access the official page of the project where you can find a description of use:

Homepage: {{ cookiecutter.project_homepage }}

{%- if cookiecutter.use_sponsor|lower == 'y' -%}
Donation
--------

If you liked my work, buy me a coffee <3

Visit {{ cookiecutter.project_repository }} to learn more about donations.
{%- endif -%}

License
-------

The gem is available as open source under the terms of the `MIT License`_ ©

Credits
-------

See, `AUTHORS`_.

Links
-----

* Code: https://github.com/{{ cookiecutter.github_profile }}/{{ cookiecutter.project_slug | replace("_", "-") }}
* Documentation: https://github.com/{{ cookiecutter.github_profile }}/{{ cookiecutter.project_slug | replace("_", "-") }}/blob/master/README.md
* Releases: https://pypi.org/project/{{ cookiecutter.project_slug | replace("_", "-") }}/#history
* Issue tracker: https://github.com/{{ cookiecutter.github_profile }}/{{ cookiecutter.project_slug | replace("_", "-") }}/issues

.. _AUTHORS: https://github.com/{{ cookiecutter.github_profile }}/{{ cookiecutter.project_slug | replace("_", "-") }}/blob/master/AUTHORS.rst
.. _python: https://python.org
.. _pip: https://pip.pypa.io/en/stable/quickstart/
.. _MIT License: https://github.com/{{ cookiecutter.github_profile }}/{{ cookiecutter.project_slug | replace("_", "-") }}/blob/master/LICENSE
