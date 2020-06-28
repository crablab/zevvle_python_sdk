import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zevvle_python_sdk", 
    version="0.0.3",
    author="Hugh Wells",
    author_email="hugh@crablab.co.uk",
    description="The unofficial Python library and SDK for the Zevvle API. ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/crablab/zevvle_python_sdk",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)