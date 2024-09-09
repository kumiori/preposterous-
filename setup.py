from setuptools import setup, find_packages

setup(
    name='Preposterous: postprocessing',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
    ],
    description='A package for postprocessing evolutionary FEM numerical computations',
    author='Your Name',
    author_email='leon.baldelli@cnrs.fr',
    url='https://github.com/kumiori/preposterous',  # Update with your GitHub URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)