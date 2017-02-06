import os
import logging
import wget
import shutil
import hashlib



LOG = logging.getLogger(__name__)


class Local:
    def __init__(self, root_path=os.environ['HOME']):
        self.root_path = root_path + '/wirt-wrap/volumes/'
        self.cache_dir = self.root_path + 'cache/'
        self.image_dir = self.root_path + 'images/'
        self.containers_dir = self.root_path + 'containers/'
        self.image_registry = ['1']

    def _init_dir_structure(self):
        try:
            os.makedirs(self.root_path)
            os.mkdir(self.cache_dir)
            os.mkdir(self.containers_dir)
            os.mkdir(self.image_dir)
            LOG.info('directory structure at initialized', self.root_path)
        except OSError as e:
            if e.errno == 17:
                LOG.debug('directory structure at %s already exists, moving on',
                          self.root_path)
                pass
            else:
                LOG.error('Got an error when creating initial directory structure: %s',
                          os.strerror(e.errno)
                          )
                raise

    def pull(self, image_uri, upgrade=False):
        self._init_dir_structure()
        file_name = image_uri.split('/')[-1]
        file_path = self.image_dir + file_name
        if os.path.isfile(file_path) and not upgrade:
            LOG.info('Image file %s already exists', file_path)
            return file_path
        try:
            wget.download(image_uri, out=self.cache_dir+file_name)
        except:
            for tmp_file in os.listdir(self.cache_dir):
                if tmp_file.startswith(file_name) and tmp_file.endswith('.tmp'):
                    tmp_file_path = self.cache_dir + tmp_file
                    LOG.error('Got exception while downloading image file: {0}, '
                              'attempting to remove temporary file: %s'.format(file_path),
                              tmp_file_path)
                    os.remove(tmp_file_path)
            raise
        LOG.info('moving image to correct location: %s', file_path)
        shutil.move(self.cache_dir+file_name, file_path)

        return file_path

    def register_image(self, image_path, image_name, buffer_size=2**20):
        if os.path.isfile(image_path):
            md5 = hashlib.md5()
            with open(image_path, "rb") as fd:
                while True:
                    data = fd.read(buffer_size)
                    if not data:
                        break
                    md5.update(data)
            image = {'name': image_name, 'path': image_path, 'md5sum': md5.hexdigest()}
            self.image_registry.append(image)
            return self.image_registry





    def list_images(self):

        pass



