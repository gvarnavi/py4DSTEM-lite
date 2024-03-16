from setuptools import setup, find_packages
from distutils.util import convert_path

with open("README.md", "r") as f:
    long_description = f.read()

version_ns = {}
vpath = convert_path("py4DSTEM/version.py")
with open(vpath) as version_file:
    exec(version_file.read(), version_ns)

setup(
    name="py4DSTEM",
    version=version_ns["__version__"],
    packages=find_packages(),
    description="A lite version of the open-source python package, py4DSTEM -- used for processing and analysis of 4D STEM data.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gvarnavi/py4DSTEM-lite/",
    author="Georgios Varnavides",
    author_email="gvarnavides@berkeley.edu",
    license="GNU GPLv3",
    keywords="STEM 4DSTEM Pyodide",
    python_requires=">=3.10",
    install_requires=[
        "numpy >= 1.19",
        "scipy >= 1.5.2",
        "h5py >= 3.2.0",
        "ncempy >= 1.8.1",
        "matplotlib >= 3.2.2",
        "tqdm >= 4.46.1",
        "dill >= 0.3.3",
        "gdown >= 5.1.0",
        "emdfile >= 0.0.14",
        "pylops >= 2.1.0",
        "colorspacious >= 1.1.2",
    ],
    package_data={
        "py4DSTEM": [
            "process/utils/scattering_factors.txt",
        ]
    },
)
