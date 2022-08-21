from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.readlines()

long_description = 'A more intelligent, user-friendly and advanced configurable local development environment built with Docker.'

setup(
    name='stdocker',
    version='1.0.0',
    author='Jason Sun',
    author_email='sunf@shinetechsoftware.com',
    url='https://github.com/winds1983/stdocker',
    description='Shinetech Docker CLI.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'gfg = stdocker.cli:main'
        ]
    },
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    keywords='python package stdocker shinetech docker',
    python_requires='>=3.8',
    install_requires=requirements,
    zip_safe=False
)
