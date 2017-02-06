import os
import logging
import wget
import shutil


#LOG = logging.getLogger(__name__)


class Local:
    def __init__(self, root_path=os.environ['HOME']):
        self.root_path = root_path + ('/wirt-wrap/volumes/')
        self.cache_dir = self.root_path + 'cache/'
        self.image_dir = self.root_path + 'images/'
        self.containers_dir = self.root_path + 'containers/'

    def _init_dir_structure(self):
        try:
            os.makedirs(self.root_path)
            os.mkdir(self.cache_dir)
            os.mkdir(self.containers_dir)
            os.mkdir(self.image_dir)
            print('directories created')
        except OSError as e:
            if e.errno == 17:
                pass
                #LOG.debug(m='directory exists')
            else:
                #LOG.error(m=os.strerror(e.errno))
                raise

    def pull(self, image_uri, upgrade=False):
        self._init_dir_structure()
        file_name = image_uri.split('/')[-1]
        file_path = self.image_dir + file_name

        if os.path.isfile(file_path) and not upgrade:
            #LOG.debug(msg='image file {0} already exists'.format(file_path))
            return file_path
        print('downloading image')
        wget.download(image_uri, out=self.cache_dir+file_name)
        print('moving image to correct location')
        shutil.move(self.cache_dir+file_name, file_path)
        return file_path

