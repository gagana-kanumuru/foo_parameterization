from setuptools import setup, find_packages # type: ignore

setup(
    name="foo_parameterization",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    author="Gagana",
    author_email="gagana.kanumuru@gmail.com",
    description="A package for calculating the Foo et al. parameterization",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/foo_parameterization",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)