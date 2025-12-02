from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="fuzzy_gi_classification",
    version="1.0.0",
    author="Kethan Reddy",
    author_email="your.email@example.com",
    description="Fuzzy-Based GI Image Classification with Ensemble Deep Learning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kethanreddy407-create/Fuzzy_Based_GI_Image_Classification",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "Development Status :: 4 - Beta",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    keywords="medical image classification deep learning fuzzy logic",
    project_urls={
        "Bug Reports": "https://github.com/kethanreddy407-create/Fuzzy_Based_GI_Image_Classification/issues",
        "Documentation": "https://github.com/kethanreddy407-create/Fuzzy_Based_GI_Image_Classification",
        "Source Code": "https://github.com/kethanreddy407-create/Fuzzy_Based_GI_Image_Classification",
    },
)
