import os, re

sep = re.compile(r'\s+')
def _sep(s):
    s = sep.sub(' ', s).strip()
    return s.split(' ')

def getDict():
    all = os.popen('pip3 list').read() 
    alist = all.splitlines()
    assert len(alist) > 2, all
    alist = alist.__iter__()
    assert next(alist).startswith('Package'), all
    assert next(alist).startswith('---'), all
    return {k:v for k,v in (_sep(line) for line in alist)}

def keepInstalled(libset):
    libdict = getDict()
    for lib in libset:
        if not libdict.get(lib, None):
                print(os.popen(f"pip3 install {lib}").read())
