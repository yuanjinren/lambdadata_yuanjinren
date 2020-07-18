from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdadata_yuanjinren", # the name that you will install via pip
    version="1.4.1",
    author="Yuanjin Ren",
    author_email="yuanjinren@gmail.com",
    description="A Litter Helper for Dataframe",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/yuanjinren/lambdadata_yuanjinren",
    #keywords="",
    packages=find_packages() # ["lambdadata"]
)