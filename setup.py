
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='ryczdft',  
     version='0.1',
     scripts=[] ,
     author="Kevin Ryczko",
     author_email="kevin.ryczko@uottawa.ca",
     description="A density functional theory package for Pythonic physicists. Allows for 1-3 dimensional systems, algorithm and data transparency. Get your hands dirty.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/kryczko/ryczdft.git",
     packages=setuptools.find_packages(),
     install_requires=[
        'ase',
        'argparse',
        'h5py'
     ],
     classifiers=[
         "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
     ],
 )
