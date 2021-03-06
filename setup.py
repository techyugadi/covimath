import pathlib
from setuptools import find_packages, setup

cd = pathlib.Path(__file__).parent

# The text of the README file
readme = (cd / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="covimath",
    packages=find_packages(exclude=("tests",)),
    version="0.1.2",
    description="Some mathematical models on epidemiology / Covid-19 infections",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/techyugadi/covimath",
    download_url='https://github.com/techyugadi/covimath/archive/refs/tags/v0.1.2.tar.gz',
    author="TechYugadi",
    author_email="techyugadi@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    install_requires=["numpy", "scipy", "matplotlib"],
    entry_points={
        "console_scripts": [
            "covimath=covimath.__main__:main",
        ]
    },
)
