from setuptools import setup, find_packages

setup(
    name="lib-ml",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "nltk",
    ],
    author="Ibrahim Badr",
    description="Preprocessing data",
)
