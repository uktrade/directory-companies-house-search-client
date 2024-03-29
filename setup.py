from setuptools import find_packages, setup

setup(
    name="directory_ch_client",
    version="4.0.2",
    url="https://github.com/uktrade/directory-companies-house-search-client",
    license="MIT",
    author="Department for Business and Trade",
    description="Python API client for Export Directory Companies House.",
    packages=find_packages(exclude=["tests.*", "tests"]),
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=[
        "django>=4.2.10,<5.0",
        "requests>=2.18.4,<3.0.0",
        "monotonic>=1.2,<3.0",
        "directory_client_core>=7.2.12,<8.0.0",
    ],
    extras_require={
        "test": [
            "pytest==7.1.3",
            "pytest-cov",
            "pytest-codecov",
            "GitPython",
            "flake8==5.0.4",
            "requests_mock==1.1.0",
            "twine",
            "wheel>=0.31.0,<1.0.0",
            "setuptools>=38.6.0,<39.0.0",
        ]
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 4.2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
