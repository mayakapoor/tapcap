import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "TaPCAP",
    version = "1.0",
    author = "Maya Kapoor",
    author_email = "mkapoor1@uncc.edu",
    description = "A network packet tabularization tool",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/mayakapoor/tapcap",
    project_urls = {
        "Bug Tracker": "https://github.com/mayakapoor/tapcap/issues",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "tapcap = tapcap:main"
        ]
    },
    package_dir = {""},
    packages = setuptools.find_packages(where=""),
    python_requires = ">=3.6"
)
