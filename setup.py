from setuptools import setup, find_packages

# This setup file loads all the dependencies from a requirements.txt file

# Read requirements.txt
def load_requirements(filename):
    with open(filename) as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name="docparser",
    version="0.1.0",
    packages=find_packages(include=["docparser", "docparser.*"]),
    install_requires=load_requirements("requirements.txt"),
    author="Soumendra Daas",
    author_email="soumendra.daas@gmail.com",
    description="Package to parse financial documents from various financial instituions",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/docparser",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
