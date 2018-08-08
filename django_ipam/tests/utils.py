import os


class FileMixin(object):
    def _get_path(self, file):
        d = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(d, file)
