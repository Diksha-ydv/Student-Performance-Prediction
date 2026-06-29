from setuptools import setup,find_packages
from typing import List

Hyphen = "-e ."
def get_requirements(file_path:str)->List[str]:
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n","") for req in requirements]

    if Hyphen in requirements:
            requirements.remove(Hyphen)

    return requirements

setup(
    name="Student Performance Prediction",
    version="0.0.1",
    author="Diksha Yadav",
    author_email="dikshaydv2006@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements("requirements.txt")
)