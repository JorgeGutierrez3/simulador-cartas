from setuptools import setup, find_packages

setup(
    name="simulador-cartas",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    author="Jorge Gutierrez",
    author_email="jorgericardogutierrez4@gmail.com",
    description="Una librería para simular una baraja de cartas",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/JorgeGutierrez3/simulador-cartas",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
) 