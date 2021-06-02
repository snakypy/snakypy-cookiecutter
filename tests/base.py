# NOTE: Before testing, update the pip: pip install --upgrade pip

import os
import subprocess
import cookiecutter
from contextlib import contextmanager


@contextmanager
def inside_dir(dirpath):
    """
    Execute code from inside the given directory
    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


def run_inside_dir(command, dirpath):
    # import shlex
    """
    Run a command from inside a given directory, returning the exit status
    :param command: Command that will be executed
    :param dirpath: String, path of the directory the command is being run.
    """
    with inside_dir(dirpath):
        # return subprocess.check_call(shlex.split(command))
        return subprocess.run(
            command, shell=True, capture_output=True, universal_newlines=True
        ).returncode


@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    result = cookies.bake(*args, **kwargs)
    try:
        yield result
    finally:
        cookiecutter.utils.rmtree(str(result.project_path))
