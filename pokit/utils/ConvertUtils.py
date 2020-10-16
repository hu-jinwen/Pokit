"""
Created by hu-jinwen on 2020/10/16
"""
import atexit
import os
from signal import signal, SIGTERM

import jpype

# 使用 signal 捕获关闭信号
signal(SIGTERM, lambda signum, stack_frame: exit(1))

jar_path = os.path.join(os.path.abspath('.'), 'libs/test.jar')
jpype.startJVM(jpype.getDefaultJVMPath(), "-ea", "-Djava.class.path=%s" % jar_path)


def bytes_str_to_str(bytes_str):
    """
    byte数组字符串 转 字符串
    例如：[72, 101, 108, 108, 111] 转 字符串的结果是：Hello
    :param bytes_str:
    :return:
    """
    try:
        Transfer = jpype.JClass("com.hujinwen.Transfer")
        transfer = Transfer()
        return transfer.bytesStrToString(bytes_str, "utf-8")
    finally:
        pass


@atexit.register
def __on_close():
    """
    退出时执行的方法
    :return:
    """
    try:
        jpype.shutdownJVM()
    except Exception:
        pass
