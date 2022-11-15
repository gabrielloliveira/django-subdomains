import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="django-subdomains",
    version="0.0.1",
    description="Subdomains middleware for django project",
    url="https://github.com/gabrielloliveira/django-subdomains",
    author="Gabriell Oliveira",
    author_email="gabrielloliveira097@gmail.com",
    packages=setuptools.find_packages(),
    include_package_data=True,
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django :: 4.0",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.8",
)
