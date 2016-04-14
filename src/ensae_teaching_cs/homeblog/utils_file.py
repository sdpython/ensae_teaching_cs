"""
@file
@brief Reasonably inefficient functions about files.
"""
import hashlib


def checksum_md5(filename):
    """computes MD5 for a file
    @param      filename        filename
    @return                     string or None if there was an error
    """
    fname = filename
    block_size = 0x10000

    def upd(m, data):
        m.update(data)
        return m
    fd = open(fname, "rb")
    try:
        block = [fd.read(block_size)]
        while len(block[-1]) > 0:
            block.append(fd.read(block_size))
        contents = block
        zero = hashlib.md5()
        i = 0
        for el in contents:
            i += 1
            zero.update(el)
        m = zero
        return m.hexdigest()
    finally:
        fd.close()
    return None
