import os, re

sep = re.compile(r'\s+')
def _sep(s):
    s = sep.sub(' ', s).strip()
    return s.split(' ')

def getDict():
    alllib = os.popen('pip3 list').read() 
    alist = alllib.splitlines()
    assert len(alist) > 2, alllib
    alist = alist.__iter__()
    assert next(alist).startswith('Package'), alllib
    assert next(alist).startswith('---'), alllib
    return dict(map(_sep, alist))

def keepInstalled(libset):
    libdict = getDict()
    for lib in libset:
        if lib not in libdict:
                print(os.popen(f"pip3 install {lib}").read())
