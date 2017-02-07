from importlib import import_module
from utils import cmd


class CliAdapter:
    def __init__(self):
        command = cmd.Cmd()
        self._module_import_string = command.get_import_string()
        self._obj_cls = command.obj
        self._cls_method = command.obj_method
        self._cls_method_kwargs = command.get_obj_method_kwargs()
        self._imported_module = self._import_module()
        self._cls_init_kwargs = {}
        self._created_object = self._create_object(**self._cls_init_kwargs)

    def _import_module(self):
        return import_module(self._module_import_string)

    def _create_object(self, kwargs={}):
        created_object = getattr(self._imported_module, self._obj_cls)(**kwargs)
        return created_object

    def run(self):
        getattr(self._created_object, self._cls_method)(**self._cls_method_kwargs)



