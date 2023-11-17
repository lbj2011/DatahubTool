# DatahubTool
Toolkit for batch management of data in [DuraMAT Datahub](https://datahub.duramat.org/), like upload and delete.

NOTE: only **authorised users** (API Key required) can manage its owned project data in Datahub. The API Key is shown on user page of Datahub.




## Installation
```
pip install datahubtool
```

## Package overview
Here's a high level overview of the important functions of the package.

- 'get_local_file_names': Get the names of local files to upload in a given path
- 'get_Datahub_file_names': Get all existing files's name in a given package in Datahub
- 'upload_files': Upload files to Datahub
- 'delete_Datahub_files': Delete files in Datahub


## Authors
Baojie Li (LBNL)