from setuptools import setup, find_packages

# Read the contents of your requirements.txt file
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="pycu",
    version="0.1.0",
    description="PyCU (Python Computing Unit) is an educational codebase to emulate a simple CPU inside python",
    author="Nicola Hermann",
    author_email="nicola.hermann@bluewin.ch",
    license="MIT",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.2",
        ],
    },
)
