import os, random
class Fileset(list):
    def __init__(self, name,  ext='', _read=None, root=None):
        if isinstance(name, str)  :
            self.root = os.path.join(root or os.getcwd(), name)
            self.extend(f for f in os.listdir(self.root) if f.endswith(ext))
            self._read = _read
    def __getitem__(self, index):
        if isinstance(index, int):# index是索引
            return os.path.join(self.root, super().__getitem__(index))
        else:# index是切片
            fileset = Fileset(None)
            fileset.root = self.root
            fileset._read = self._read
            fileset.extend(super().__getitem__(index))
            return fileset
    def getFileName(self, index):
        fname, ext = os.path.splitext(super().__getitem__(index))
        return fname
    def __iter__(self):
        if self._read: return (self._read(os.path.join(self.root, f)) for f in super().__iter__())
        else: return (os.path.join(self.root, f) for f in super().__iter__())
    def __call__(self):
        retn = random.choice(self)
        if self._read: return self._read(retn)
        else: return retn