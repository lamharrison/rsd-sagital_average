from setuptools import setup, find_packages

setup(
    name="sagital_average",
    version="0.1.0",
    packages=find_packages(exclude=['*test']),
    install_requires=['numpy'],
    entry_points={
        'console_scripts': [
            'sagverage = sagital_average.command:process'
        ]},
)