from setuptools import setup, find_packages




requirements: list = open("requirements.txt", encoding="utf-8").read().splitlines()
version: str = open(".version", encoding="utf-8").read()
long_description: str = open("README.md", encoding="utf-8").read()

setup(
    name= "data_structure_implementations",
    version= version,
    packages=find_packages(),
    description="Implementations of Popular Data Structures",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="berkaytrhn",
    author_email="berkaytrhn@gmail.com",
    url="https://github.com/berkaytrhn/data-structure-implementations",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11.8',
    requires=requirements
)


