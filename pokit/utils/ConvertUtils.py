"""
Created by hu-jinwen on 2020/10/16
"""
import atexit
import os
from signal import signal, SIGTERM

import jpype

# 使用 signal 捕获关闭信号
from pokit.tools import LoggerFactory
from pokit.utils import PathUtils

signal(SIGTERM, lambda signum, stack_frame: exit(1))

base_path = PathUtils.get_env_path()
if "/Pokit/" in PathUtils.get_env_path():
    cwd = os.getcwd()
    base_path = cwd[0:cwd.rindex("/Pokit/") + 6]

jar_path = "{0}/resources/transfer.jar".format(base_path)
jpype.startJVM(jpype.getDefaultJVMPath(), "-ea", "-Djava.class.path={0}".format(jar_path))

logger = LoggerFactory.get_logger("ConvertUtils")


def bytes_str_to_str(bytes_str):
    """
    byte数组字符串 转 字符串
    例如：[72, 101, 108, 108, 111] 转 字符串的结果是：Hello
    :param bytes_str:
    :return:
    """
    transfer = jpype.JClass("com.hujinwen.Transfer")
    transfer = transfer()
    return transfer.bytesStrToString(bytes_str, "utf-8")


@atexit.register
def __on_close():
    """
    退出时执行的方法
    :return:
    """
    try:
        jpype.shutdownJVM()
    except Exception as e:
        logger.warn(e)
