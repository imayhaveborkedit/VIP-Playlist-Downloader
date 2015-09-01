import struct
from ctypes import windll, create_string_buffer

def get_term_size():
    h = windll.kernel32.GetStdHandle(-12)
    csbi = create_string_buffer(22)
    res = windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)
    (bufx, bufy, curx, cury, wattr,
        left, top, right, bottom, maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
    sizex = right - left + 1
    sizey = bottom - top + 1
    return sizex, sizey

def getPrettyFileSizes(fsize, size = None):
    frd = lambda s,d: round(float(s)/1000**d,2)
    sizelist = { 'B' : fsize, 'KB' : frd(fsize,1), 'MB' : frd(fsize,2), 'GB' : frd(fsize,3)}
    if size is None:
        if fsize < 1.0: return 0, 'B'
        for sls in sizelist:
            if 1 <= sizelist[sls] <= 1000:
                return '%d %s' % (sizelist[sls], sls)
        return '%d %s' % (sizelist['MB'], 'MB')
    else:
        return sizelist.get(size)

