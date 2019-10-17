from setuptools import setup, find_packages

with open('README.md') as rfh:
    long_description = rfh.read()

setup(
    author='siznax',
    author_email='steve@siznax.net',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    description='Human readable numbers',
    long_description=long_description,
    long_description_content_type="text/markdown",
    name='khnum',
    packages=find_packages(),
    tests_require=['pytest'],
    url='https://github.com/siznax/khnum/',
    version='0.0.2'
)
