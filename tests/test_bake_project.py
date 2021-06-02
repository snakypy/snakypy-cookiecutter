import os
from os import listdir
# from tests.base_config import run_inside_dir
from tests.base import bake_in_temp_dir


# @pytest.fixture
# def result(cookies):
#     with bake_in_temp_dir(cookies, extra_context={"use_pytest": "y", "use_poetry": "y"}) as resul:
#         return resul


# @pytest.fixture
# def base(result):
#     return {
#         "pyproject_file": os.path.join(result.project_path, "pyproject.toml"),
#         "test_file": os.path.join(result.project_path, "tests/test_snakypy_cookiecutter.py")
#     }


def test_pytest_cookies(cookies):
    result = cookies.bake()
    assert result.exit_code == 0
    assert result.exception is None


def test_bake_with_defaults(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project_path.is_dir()
        assert result.exit_code == 0
        assert result.exception is None
        assert "README.md" in listdir(result.project_path)


def test_using_github_actions(cookies):
    with bake_in_temp_dir(cookies, extra_context={"use_github_actions": "y"}) as result:
        assert ".github" in listdir(result.project_path)
        assert "workflows" in listdir(os.path.join(result.project_path, ".github"))
        assert "tests.yml" in listdir(os.path.join(result.project_path, ".github/workflows"))


def test_using_sponsor(cookies):
    with bake_in_temp_dir(cookies, extra_context={"use_sponsor": "y"}) as result:
        assert ".github" in listdir(result.project_path)
        assert "FUNDING.yml" in listdir(os.path.join(result.project_path, ".github"))


def test_using_pytest(cookies):
    with bake_in_temp_dir(
        cookies, extra_context={"use_pytest": "y", "use_poetry": "y"}
    ) as result:
        test_file_path = os.path.join(result.project_path, "tests/test_snakypy_cookiecutter.py")

        with open(test_file_path) as f:
            lines = f.readlines()

        assert "import pytest" in "".join(lines)
        assert "pyproject.toml" in listdir(result.project_path)
        assert "tests" in listdir(result.project_path)

        pyproject_file = os.path.join(result.project_path, "pyproject.toml")

        with open(pyproject_file) as f:
            lines = f.readlines()
        assert "[tool.pytest.ini_options]" in "".join(lines)
        # # assert run_inside_dir("pytest", str(result.project)) == 0


def test_not_using_pytest(cookies):
    with bake_in_temp_dir(cookies, extra_context={"use_pytest": "n"}) as result:
        test_file_path = os.path.join(result.project_path, "tests/test_snakypy_cookiecutter.py")
        with open(test_file_path) as f:
            lines = f.readlines()
        assert "import unittest" in "".join(lines)
        assert "import pytest" not in "".join(lines)
        # assert (
        #     run_inside_dir(
        #         "python -m unittest tests/test_snakypy_cookiecutter.py",
        #         str(result.project),
        #     )
        #     == 0
        # )


def test_using_poetry(cookies):
    with bake_in_temp_dir(cookies, extra_context={"use_poetry": "y"}) as result:
        assert "pyproject.toml" in listdir(result.project_path)
        pyproject_file = os.path.join(result.project_path, "pyproject.toml")
        with open(pyproject_file) as f:
            lines = f.readlines()
        assert "[tool.poetry]" in "".join(lines)
        # assert run_inside_dir("poetry build", str(result.project)) == 0


def test_not_using_poetry(cookies):
    with bake_in_temp_dir(cookies, extra_context={"use_poetry": "n"}) as result:
        assert "setup.py" in listdir(result.project_path)
        setup_file = os.path.join(result.project_path, "setup.py")
        with open(setup_file) as f:
            lines = f.readlines()
        assert "from setuptools import setup, find_packages" in "".join(lines)
#       assert run_inside_dir("python setup.py test", str(result.project)) == 0
