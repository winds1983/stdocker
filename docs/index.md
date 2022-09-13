# Shinetech Docker CLI

## Build a Python package


### Steps

1. Create your Command Line Script.
2. Set-up files and folder structure for Packaging.
3. Modify your setup.py file to incorporate your CLI scripts.
4. Test your package before publishing and then Build.
5. Upload on pypi and publish your package.
6. Install your newly-published package.

Reference:

* [Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
* [Command Line Scripts | Python Packaging](https://www.geeksforgeeks.org/command-line-scripts-python-packaging/)
* [How to Build a Python package?](https://www.geeksforgeeks.org/how-to-build-a-python-package/)
* [Python中使用setup.py和console_scripts参数创建安装包和shell命令](https://blog.csdn.net/lslxdx/article/details/73131664)
* [命令行脚本](https://python-packaging-zh.readthedocs.io/zh_CN/latest/command-line-scripts.html#scripts)
* [Python Apps the Right Way: entry points and scripts](https://chriswarrick.com/blog/2014/09/15/python-apps-the-right-way-entry_points-and-scripts/)
* [创建Python包并上传至PyPI](https://zhuanlan.zhihu.com/p/106166278)

### Test and Debug package

```bash
sudo python3 setup.py install
```

If cannot install latest package, please uninstall then try again:
```shell
sudo pip3 uninstall stdocker
sudo python3 setup.py install
```

### Publish package

Build package:

```bash
python3 setup.py sdist bdist_wheel
```

Upload package to https://pypi.org/project/stdocker/

```bash
twine upload --repository pypi dist/*
```

You can upload your distributions to TestPyPI using twine by specifying the `--repository` flag:

```bash
twine upload --repository testpypi dist/*
```

```
Uploading distributions to https://upload.pypi.org/legacy/
Enter your username: sunfeng
Enter your password: 
Uploading stdocker-1.0.0-py3-none-any.whl
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 9.5/9.5 kB • 00:02 • 2.9 MB/s
Uploading stdocker-1.0.0-py3.8.egg
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 16.6/16.6 kB • 00:00 • 14.5 MB/s
Uploading stdocker-1.0.0.tar.gz
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.0/8.0 kB • 00:00 • ?

View at:
https://pypi.org/project/stdocker/1.0.0/
```

### Debug on local 

```bash
stdocker start
stdocker -d /var/www/html/Shinetech/shinetech-docker start
```
