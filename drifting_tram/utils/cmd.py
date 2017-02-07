from sys import argv


class Cmd:
    def __init__(self):
        """Class Cmd is used as API for starting correct
        scripts at program launch"""
        self.cli = argv
        self.obj = self.cli[1].capitalize()
        self.obj_method = self.cli[2]
        self._obj_method_kwargs = {}
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

    def get_import_string(self):
        import_string = self._import_string
        return import_string

    def get_obj_method_kwargs(self):
        method_kwargs = self._obj_method_kwargs
        return method_kwargs



