"""
Created by hu-jinwen on 2020/9/4
"""
import importlib


def for_name(class_name):
    """
    参考java Class.forName()
    :param class_name: 类名
    :return: 类实例
    """
    index = class_name.rindex(".")
    package_name = class_name[0: index]
    simple_class_name = class_name[index + 1:]
    package = importlib.import_module(package_name)
    return getattr(package, simple_class_name)


def new_instance(class_name, *args, **kwargs):
    """
    根据类名创建实例
    :param class_name: 类名
    :return: 实例
    """
    clazz = for_name(class_name)
    return clazz(*args, **kwargs)
