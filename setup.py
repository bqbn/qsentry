"""
For references of this file, see
    * https://github.com/pypa/sampleproject
    * https://packaging.python.org/en/latest/
"""

from setuptools import setup, find_packages


setup(
    # packages=find_packages(exclude=["contrib", "docs", "tests"]),
    # install_requires=[
    #     "click~=8.0",
    #     "jmespath~=1.0",
    #     "requests~=2.27",
    # ],
    # Additional groups of dependencies. They can be install by using
    # the "extras" syntax, for example:
    #
    #   $ pip install <module-name>[dev]
    # extras_require={
    #     "dev": [
    #         "build~=0.7.0",
    #         "pipenv-setup~=3.2",
    #         "twine~=3.2",
    #         "wheel~=0.34",
    #     ],
    #     "test": [],
    # },
    # Needed by the pipenv-setup tool.
    # dependency_links=[],
    # entry_points={
    #     "console_scripts": [
    #         "qsentry=qsentry.qsentry:main",
    #     ],
    # },
)
