"""
Setup file to make extensions package discoverable
"""
from setuptools import setup, find_packages

setup(
    name="mkdocs-milestone-extension",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "mkdocs",
        "PyYAML",
    ],
)

