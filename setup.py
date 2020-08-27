import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="annyong-pkg-hyeryung-yun",
    version="0.0.1",
    author="Hye Ryung Yun",
    author_email="hyeryung@outlook.sg",
    description="2nd attempt at packaging, 1st failed!",
    long_description=long_description,
    long_description_content_type="Will try again if this fails again!",
    url="https://github.com/hyeryung-jeon/annyong.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
