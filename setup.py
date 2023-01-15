from setuptools import find_packages,setup

def get_requirements():
    pass

setup(
    name="Stock Market Prediction",
    version = "0.0.1",
    author = "Swastic",
    author_email= "swastic.singh@gmail.com",
    packages= find_packages(),
    install_requires = get_requirements(),
)