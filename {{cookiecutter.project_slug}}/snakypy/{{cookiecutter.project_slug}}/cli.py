"""CLI - Command Line Interface"""
{% if cookiecutter.use_cli == 'y' -%}
import click


@click.command()
def main():
    click.echo("Hello, World!"){% endif %}
