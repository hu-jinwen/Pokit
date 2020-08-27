"""
Created by hu-jinwen on 2020/8/27
"""

from setuptools import setup

setup(
    name='Pokit',
    version='0.1.0',
    description='python toolkit',
    url='https://github.com/hu-jinwen/Pokit',
    author='hu-jinwen',
    author_email='hu-jinwen@outlook.com',
    license='MIT',
    keywords='python toolkit utils',
    packages=['pokit.utils', 'pokit.tools'],
    install_requires=['pycrypto==2.6.1'],
    python_requires='>=3'
)
