Shinetech Docker CLI
===

A more intelligent, user-friendly and advanced configurable local development environment built with Docker.

1. Create your Command Line Script.
2. Set-up files and folder structure for Packaging.
3. Modify your setup.py file to incorporate your CLI scripts.
4. Test your package before publishing and then Build.
5. Upload on pypi and publish your package.
6. Install your newly-published package.


* [Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
* [Command Line Scripts | Python Packaging](https://www.geeksforgeeks.org/command-line-scripts-python-packaging/)
* [How to Build a Python package?](https://www.geeksforgeeks.org/how-to-build-a-python-package/)
* [Python中使用setup.py和console_scripts参数创建安装包和shell命令](https://blog.csdn.net/lslxdx/article/details/73131664)
* [命令行脚本](https://python-packaging-zh.readthedocs.io/zh_CN/latest/command-line-scripts.html#scripts)
* [Python Apps the Right Way: entry points and scripts](https://chriswarrick.com/blog/2014/09/15/python-apps-the-right-way-entry_points-and-scripts/)


```bash
python3 setup.py sdist bdist_wheel
```

```bash
twine upload --repository pypi dist/*
```


## Issues

/usr/lib/python3/dist-packages/requests/__init__.py:89: RequestsDependencyWarning: urllib3 (1.26.11) or chardet (3.0.4) doesn't match a supported version!
  warnings.warn("urllib3 ({}) or chardet ({}) doesn't match a supported

```bash
sudo pip3 install requests
```
or
```bash
sudo pip3 install --upgrade requests
```


* [Docker 命令大全](https://www.runoob.com/docker/docker-command-manual.html)
