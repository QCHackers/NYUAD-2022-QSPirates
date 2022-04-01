import io

from setuptools import find_packages, setup

name="QvsPy"

description="Quantum virus sensing on Python"

# README file as long_description.
long_description = io.open("README.md", encoding="utf-8").read()

# Read in requirements
requirements = open("requirements.txt").readlines()
requirements = [r.strip() for r in requirements]

qvspy_packages = ["qvspy"] + [
    "qvspy." + package for package in find_packages(where="qvspy")
]

setup(
    name=name,
    version='0.0.1',
    url="https://github.com/SupertechLabs/cirq-superstaq",
    author="Super.tech",
    author_email="victory@super.tech",
    python_requires=(">=3.7.0"),
    install_requires=requirements,
    license="Apache 2",
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=qvspy_packages,
)