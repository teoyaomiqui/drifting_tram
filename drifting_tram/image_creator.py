import os
import shutil
import subprocess
from importlib import import_module


class ImageCreator:
    def __init__(self, image_path=None, env_name='Default_Env', image_storage='storage.image.Local'):
        self.base_image_path = image_path
        self.env_name = env_name
        self.copied_image = None
        self.image_storage_driver = image_storage

    def format_image_to_qcow2(self, image_to_format):
        if not image_to_format:
            image_to_format = self.copied_image
        subprocess.call(['qemu-img', 'convert', '-O', '-q' 'qcow2', image_to_format, ])

        pass

    def copy_image(self):
        # if self.storage == 'local':
        file_name = os.path.split(self.base_image_path)[-1]
        dest = 'volumes/{0}_{1}'.format(self.env_name, file_name)
        if os.path.isfile(self.base_image_path) and not os.path.isfile(dest):
            shutil.copy(self.base_image_path, dest)
        else:
            print 'image {0} already exists'.format(dest)
        self.copied_image = dest
        return self.copied_image


class StorageAdapter:
    def __init__(self, storage_driver, storage_driver_module='storage.image'):
        self.storage_driver_module = import_module(storage_driver_module)
        self.storage_driver_cls = storage_driver

    def call_driver(self, action, action_kwargs):
        driver = getattr(self.storage_driver_module, self.storage_driver_cls)()
        getattr(driver, action)(**action_kwargs)

pull_kwargs = {'image_uri': 'https://cloud-images.ubuntu.com/xenial/current/xenial-server-cloudimg-amd64-disk1.img'}
adapter = StorageAdapter('Local')
adapter.call_driver('pull', pull_kwargs)
#getattr(adapter, 'init_dir_structure')(**pull_kwargs)
