from setuptools import setup, find_packages

def read_files(files):
    data = []
    for file in files:
        with open(file, encoding='utf-8') as f:
            data.append(f.read())
    return "\n".join(data)

long_description = read_files(['README.md', 'CHANGELOG.md'])

requirements = []
with open('requirements.txt') as f:
    requirements = f.readlines()

meta = {}
with open('./stdocker/version.py', encoding='utf-8') as f:
    exec(f.read(), meta)

setup(
    name='stdocker',
    version=meta['__version__'],
    author='Jason Sun',
    author_email='sunf@shinetechsoftware.com',
    url='https://github.com/winds1983/stdocker',
    description='Shinetech Docker CLI.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=find_packages(),
    python_requires=">=3.8",
    extras_require={
        'cli': ['click>=5.0', ],
    },
    entry_points={
        'console_scripts': [
            'stdocker=stdocker.cli:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=['python package', 'stdocker', 'shinetech', 'docker', 'development environment'],
    install_requires=requirements,
    zip_safe=False
)
