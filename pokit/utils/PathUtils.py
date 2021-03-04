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
    # 传入了项目名称，尝试使用项目名称从启动路径截取。
    launch_path = get_launch_path()
    if project_name and project_name in launch_path:
        index = launch_path.index(project_name)
        return launch_path[:index + len(project_name)]
    # 未传入项目路径，尝试根据虚拟环境截取。
    abs_file_path = os.path.abspath(__file__)
    env_path = sys.prefix
    assumed_path = env_path[0:env_path.rindex("/")]
    if assumed_path in abs_file_path:
        return assumed_path
    # 未传入项目名称 且 未使用虚拟环境。则获取目录失败
    logger.warning("Unable to get the root directory automatically! Please enter the project name or use 'virtualenv'.")
    return ""
