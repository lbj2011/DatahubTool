import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="datahubtool",
    version="0.0.1",
    author="baojieli",
    author_email="lbjxx2011@gmail.com",
    description="Data management toolkit of Duramat Datahub",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lbj2011/DatahubTool",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=['numpy','pandas','scipy'],
    license='BSD License',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)