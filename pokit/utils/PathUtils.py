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


def get_root_path(project_name: str) -> str:
    """
    获取项目根目录
    :param project_name: 项目名称
    :return:
    """
    # TODO 这里获取当前文件路径，通过项目名称截取一下
    # 获取当前文件名 __file__
    # __name__ 当前模块名，pokit.utils.PathUtils
