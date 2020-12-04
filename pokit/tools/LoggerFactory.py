"""
Created by hu-jinwen on 2019/11/18
"""
import logging
import logging.config
import os
from logging import Logger

import yaml

from pokit.utils import PathUtils


def init():
    """
    初始化logging配置
    :return:
    """
    root_path = PathUtils.get_root_path()
    yaml_file_path = root_path + "/logging.yaml"
    if not os.path.exists(yaml_file_path):
        yaml_file_path = root_path + "/logging.yml"
    if os.path.exists(yaml_file_path):
        with open(yaml_file_path, "r") as fi:
            conf_dict = yaml.safe_load(fi.read())
            logging.config.dictConfig(conf_dict)
        return

    conf_file_path = root_path + "/logging.conf"
    if os.path.exists(conf_file_path):
        logging.config.fileConfig(fname=conf_file_path, disable_existing_loggers=True)
        return

    logger = get_logger("LoggerFactory.init")
    logger.warning("Can't find configuration file, logging.conf or logging.yaml or logging.yml")


def get_logger(name: str) -> Logger:
    """
    获取logger
    :param name:
    :return:
    """
    logger = logging.getLogger(name)
    return logger


init()
