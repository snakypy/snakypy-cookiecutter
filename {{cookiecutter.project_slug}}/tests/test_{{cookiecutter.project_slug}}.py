"""Tests for `{{ cookiecutter.project_slug | replace("_", "-") }}` package."""

{% if cookiecutter.use_pytest == 'y' %}
import pytest
{% else %}
import unittest
{% endif %}
from snakypy.{{ cookiecutter.project_slug }} import __info__, {{ cookiecutter.project_slug }}
{% if cookiecutter.use_cli == 'y' %}
from snakypy.{{ cookiecutter.project_slug }} import cli
{% endif %}
{% if cookiecutter.use_cli == 'y' -%}
from click.testing import CliRunner
{% endif %}

{% if cookiecutter.use_pytest == 'y' %}


def test_version():
    assert __info__["version"] == "0.1.0"


def test_something_000():
    """Test Something"""
    assert (25 / 5) == 5
    with pytest.raises(ZeroDivisionError):
        assert (1 / 0) == 0


{% if cookiecutter.use_cli == 'y' -%}
def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'Hello, World!' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output{%- endif %}
{% else %}


class Test{{ cookiecutter.project_slug|title }}(unittest.TestCase):
    """Tests for `{{ cookiecutter.project_slug }}` package."""

    def test_version(self):
        self.assertEqual(__info__["version"], "0.1.0")

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_something_000(self):
        """Test Something"""
        self.assertEqual((25 / 5), 5)
        with self.assertRaises(ZeroDivisionError):
            self.assertEqual((25 / 0), 5)

    {% if cookiecutter.use_cli == 'y' -%}def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Hello, World!", result.output)
        help_result = runner.invoke(cli.main, ['--help'])
        self.assertEqual(help_result.exit_code, 0)
        self.assertIn("--help  Show this message and exit.", help_result.output){%- endif %}
{% endif %}
