"""
Created by hu-jinwen on 2020/8/27
"""

from setuptools import setup

setup(
    name='pokit',
    version='0.1.9',
    description='python toolkit',
    url='https://github.com/hu-jinwen/Pokit',
    author='hu-jinwen',
    author_email='hu-jinwen@outlook.com',
    license='MIT',
    keywords='python toolkit utils',
    packages=['pokit.utils', 'pokit.tools'],
    data_files=[
        ("resources", ["resources/Transfer.jar"])
    ],
    install_requires=[
        # 'pycrypto==2.6.1',
        "mysqlclient==2.0.1",
        "redis==3.5.3",
        "greenstalk==2.0.0",
        "JPype1==1.0.2",
        "PyYAML==5.3.1"
    ],
    python_requires='>=3'
)
