from setuptools import setup

with open("README.md") as f:
    long_description = f.read()

setup(
    name="probspellchecker",
    version="0.1.0",
    description="probabilistic spell checker",
    license="GPLv2",
    long_description=long_description,
    author="digitalarbeiter",
    author_email="digitalarbeiter@talbriefkasten.de",
    url="https://github.com/digitalarbeiter/probspellchecker",
    packages=["probspellchecker"],
    install_requires=[
        "logging",
    ],
    scripts=[
        "scripts/probdict-from-dewiki.py",
        "scripts/probdict-from-text.py",
    ]
)
