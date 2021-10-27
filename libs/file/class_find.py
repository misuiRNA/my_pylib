import importlib
import inspect
from pkgutil import iter_modules


def find_classes(root_path, total_module_name):
    """
    递归查询指定模块下的所有类
    :param root_path: 工程跟路径
    :param total_module_name: 目标模块名（全名）
    :return: 查询到的类列表
    """
    cls_list = list()
    total_path = root_path + "/" + total_module_name.replace(".", "/")
    for module in iter_modules([total_path]):
        sub_module = total_module_name + "." + module.name
        if module.ispkg:
            cls_list.extend(find_classes(root_path, sub_module))
        else:
            for key, cls in inspect.getmembers(importlib.import_module(sub_module), inspect.isclass):
                if str(cls.__module__).find(sub_module) != -1:
                    cls_list.append(cls)
    return cls_list
