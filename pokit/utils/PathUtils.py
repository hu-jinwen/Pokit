"""
Created by hu-jinwen on 2020/10/21
"""
import os
import sys


def get_env_path() -> str:
    """
    获取环境路径
    :return:
    """
    return sys.prefix


def get_launch_path() -> str:
    """
    获取启动程序的路径
    :return:
    """
    return os.path.dirname(os.path.abspath(sys.argv[0]))
