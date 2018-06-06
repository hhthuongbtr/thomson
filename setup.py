import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Thomson",
    version="0.0.2",
    author="Thuong Huynh",
    author_email="hhthuongbtr@gmail.com",
    description="Thomson API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hhthuongbtr/thomson.git",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
