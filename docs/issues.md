# Issues

### warnings.warn("urllib3 ({}) or chardet ({}) doesn't match a supported

```
/usr/lib/python3/dist-packages/requests/__init__.py:89: RequestsDependencyWarning: urllib3 (1.26.11) or chardet (3.0.4) doesn't match a supported version!
  warnings.warn("urllib3 ({}) or chardet ({}) doesn't match a supported
```

#### Solution

```bash
sudo pip3 install requests
```
or
```bash
sudo pip3 install --upgrade requests
```

### HTTPError: 400 Client Error: This filename has already been used, use a different version.

```
ERROR    HTTPError: 400 Bad Request from https://upload.pypi.org/legacy/                                                                                                                                                           
         This filename has already been used, use a different version. See https://pypi.org/help/#file-name-reuse for more information. 
```
The official website documentation explains the following:
```
PyPI will return these errors for one of these reasons:

Filename has been used and file exists
Filename has been used but file no longer exists
A file with the exact same content exists
PyPI does not allow for a filename to be reused, even once a project has been deleted and recreated.

To avoid this situation, use Test PyPI to perform and check your upload first, before uploading to pypi.org.
```

#### Solution

Update a new version and empty /dist/* then re-upload

```shell
sudo rm -fr dist/*
python3 setup.py sdist bdist_wheel
twine upload --repository pypi dist/*
```

* [Why am I getting a "Filename or contents already exists" or "Filename has been previously used" error?](https://pypi.org/help/#file-name-reuse)


### ERROR: Could not find a version that satisfies the requirement

```
ERROR: Could not find a version that satisfies the requirement stdocker==1.0.1 (from versions: none)
ERROR: No matching distribution found for stdocker==1.0.1
```

#### Solution

```shell
python3 -m pip install stdocker==1.0.1
```

* [Could not find a version that satisfies the requirement <package>](https://stackoverflow.com/questions/32302379/could-not-find-a-version-that-satisfies-the-requirement-package)


## Reference

* [Docker 命令大全](https://www.runoob.com/docker/docker-command-manual.html)

