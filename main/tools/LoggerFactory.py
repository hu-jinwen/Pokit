"""
Created by joe on 2019/11/18
"""
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def get_logger(name):
    """
    获取logger
    :param name:
    :return:
    """
    return logging.getLogger(name)
