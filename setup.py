from setuptools import setup, find_packages
import os

setup(
    name='revenewCC',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_dir=os.getcwd(),
    install_requires=[
        'Click',
        'pandas',
        'sqlalchemy',
        'tqdm',
        'fuzzywuzzy',
        'gooey',
        'xlsxwriter',
        'pyodbc',
        'wxpython',
    ],
    entry_points='''
        [console_scripts]
        ranking=revenewCC.ranking:main
    ''',
)
