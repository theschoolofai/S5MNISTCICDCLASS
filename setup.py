from setuptools import setup, find_packages

setup(
    name="mnist_cicd",
    version="0.1",
    packages=find_packages(include=['model', 'model.*']),
    python_requires='>=3.8',
) 