import importlib

action = 'create'
kwargs = {'name' : 'my_vm', 'huyeim': 'not my vm'}
module = 'objects.objects'
module_name = importlib.import_module(module)
obj = module_name.Vms()
getattr(obj, action)(**kwargs)

