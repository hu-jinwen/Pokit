"""
Created by hu-jinwen on 2020/10/21
"""
import logging
import os
import sys

logger = logging.getLogger("PathUtils")


def get_py_env_path() -> str:
    """
    获取python环境的根目录
    :return:
    """
    return sys.prefix


def get_launch_path() -> str:
    """
    获取启动程序所在目录
    :return:
    """
    return os.path.dirname(os.path.abspath(sys.argv[0]))


def get_root_path(project_name: str = None) -> str:
    """
    获取项目根目录
    FIXME 未测试 Windows 系统
    :param project_name: 项目名称
    :return:
    """
    # 传入了项目路径，使用项目路径从当前文件目录截取
    abs_file = os.path.abspath(__file__)
    if project_name:
        index = abs_file.index(project_name)
        return abs_file[:index + len(project_name)]
    # 未传入项目路径，根据虚拟环境截取。
    env_path = sys.prefix
    assumed_path = env_path[0:env_path.rindex("/")]
    if assumed_path in abs_file:
        return assumed_path
    # 未传入项目名称 且 未使用虚拟环境。则获取目录失败
    logger.warning("Unable to get the root directory automatically! Please enter the project name or use 'virtualenv'.")
    return ""
