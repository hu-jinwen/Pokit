"""
Created by joe on 2019/11/18
"""
import logging

LEVEL = logging.INFO

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def get_logger(name):
    """
    获取logger
    :param name:
    :return:
    """
    logger = logging.getLogger(name)
    logger.setLevel(LEVEL)
    return logger
