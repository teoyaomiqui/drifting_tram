from sys import argv
from importlib import import_module


class Cmd:
    def __init__(self):
        """Class Cmd is used as API for starting correct
        scripts at program launch"""
        self.cli = argv
        self.obj = self.cli[1].capitalize()
        self.obj_method = self.cli[2]
        self._obj_method_kwargs = {}
        self._obj_kwargs = {}
        self._import_string = ''
        self._set_method_kwargs()
        self._set_import_string()

    def _set_method_kwargs(self):
        i = 0
        argvs = self.cli[3:]
        while i < len(argvs)-1:
            key = argvs[i][2:]
            self._obj_method_kwargs[key] = argvs[i+1]
            i += 2

    def _set_import_string(self, base_module='objects'):
        import_file = self.obj.lower()
        self._import_string = '.'.join([base_module, import_file])

    def _get_import_string(self):
        return self._import_string

    def _get_obj_kwargs(self):
        return self._obj_kwargs or {}

    def _get_obj_method_kwargs(self):
        return self._obj_method_kwargs or {}

    def run(self):
        imported_module = import_module(self._get_import_string())
        obj_cls = self.obj
        cls_method = self.obj_method
        created_object = getattr(imported_module, obj_cls)(**self._get_obj_kwargs())
        getattr(created_object, cls_method)(**self._get_obj_method_kwargs())


