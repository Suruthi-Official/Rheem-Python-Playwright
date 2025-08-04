# setup.py for RCS
from setuptools import setup, find_packages

setup(
    name='RCS',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pytest',
        'pytest-bdd',
        'playwright',
    ],
    description='BDD Playwright automation for SauceDemo in RCS',
    author='Your Name',
    author_email='your.email@example.com',
)
