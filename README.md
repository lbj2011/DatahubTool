# DatahubTool

[![PyPI - Version](https://img.shields.io/pypi/v/datahubtool)](https://pypi.org/project/datahubtool/)
[![DOI](https://zenodo.org/badge/719921081.svg)](https://zenodo.org/doi/10.5281/zenodo.10150399)

<img src="https://github.com/lbj2011/DatahubTool/blob/main/doc_img/duramat_logo.png" width="200"/>

Toolkit for batch management of data in [DuraMAT Datahub](https://datahub.duramat.org/), like upload and delete.

NOTE: only **authorised users** (API Key required, shown on user page of Datahub) can manage its owned project data in Datahub. 


## Installation
```
pip install datahubtool
```

## Package overview
Here is a high level overview of the important functions of the package.

- 'run_upload_pipeline': Pipeline to realize the data upload
- 'get_local_file_names': Get the names of local files to upload in a given path
- 'get_Datahub_file_names': Get all existing files's name in a given package in Datahub
- 'upload_files': Upload files to Datahub
- 'delete_Datahub_files': Delete files in Datahub

## Example of upload files
```
from DatahubTool import run_upload_pipeline

headers = {'Authorization': [your API key]}
folder_path = 'Path of the folder to upload'
datahub_package_name = 'Datahub package name'
file_format = '.csv'

run_upload_pipeline(folder_path, datahub_package_name, headers, 
                    file_format = file_format)
```

When complete, it will print:

```
2/2 file(s) uploaded on 2023-11-17 14:20:24
```

## Authors
Baojie Li (LBNL)