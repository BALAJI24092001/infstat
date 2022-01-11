from setuptools import setup
import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
        name="infstat",
        version="0.0.3",
        description="A module for testing statistical inferences built on multiple data samples based on pre-detemined hypothesis.",
        long_description=long_description,
        long_description_content_type="text/markdown",
        package_dir={"":"src/"},
        packages= setuptools.find_packages(where='src/'),
        url="",
        author="DEGA BALAJI VARA PRASAD",
        author_email="dbalajivaraprasad@gmail.com",
        license="BSD 3-Clause License",
        zip_safe=False,
        classifiers=[
            "Intended Audience :: Education",
            "License :: OSI Approved :: BSD License",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.10",
        ],
        python_requires=">=3.6" ,
        # install_requires=[
            # "Click",
            # "requests",
            # ],
        )
