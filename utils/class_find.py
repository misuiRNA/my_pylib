import importlib
import inspect
from pkgutil import iter_modules


def find_classes(root_path, total_module_name):
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
