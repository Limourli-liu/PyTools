import os
from configparser import ConfigParser, SectionProxy
def _path(name, root=None):
    p =  os.path.join(root or os.getcwd(), name)
    return (os.path.exists(p) or not os.mkdir(p)) and p
def _fp(name):
    return os.path.join(_path('conf'), name)

def S__getitem__(self, key):
    if not self._parser.has_option(self._name, key): return None
    return self._parser.get(self._name, key)
SectionProxy.__getitem__ = S__getitem__

class Conf(ConfigParser):
    def __init__(self, name):
        super().__init__()
        p = self._path = _fp(name)
        if os.path.exists(p): super().read(p, encoding='utf-8')
        self._changed = False
    def __enter__(self):
        #print('__enter__')
        return self
    def setdefault(self, key, default):
        self._changed = True
        return super().setdefault(key, default)
    def __getitem__(self, section):
        if section not in self: self.add_section(section)
        return super().__getitem__(section)
    def add_section(self, section):
        self._changed = True
        return super().add_section(section)
    def set(self, section, option, value=None):
        self._changed = True
        if section not in self: super().add_section(section)
        return super().set(section, option, value)
    def remove_option(self, section, option):
        self._changed = True
        return super().remove_option(section, option)
    def remove_section(self, section):
        self._changed = True
        return super().remove_section(section)
    def clear(self):
        self._changed = True
        return super().clear()
    def __exit__(self, exc_type, exc_val, exc_tb):
        #print('__exit__')
        if not self._changed: return not (exc_type or exc_val or exc_tb)
        with open(self._path, 'w', encoding='utf-8') as f:
            super().write(f)
            #print(f'save {self._path}')
            return not (exc_type or exc_val or exc_tb)