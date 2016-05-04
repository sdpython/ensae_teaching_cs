"""
@file
@brief image helpers
"""
from PIL import Image


def collate_images(imgs, final=None):
    """
    collate all images horizontally in one image (if not None --> image name)

    @param      imgs        list of image files
    @param      final       final image (or None not to save)
    @return                 final image (PIL object)

    It uses the module `Pillow <http://python-imaging.github.io/>`_.
    """
    ims = [Image.open(pic) for pic in imgs]
    size = [_.size for _ in ims]
    fsize = (sum([_[0] for _ in size]),
             max([_[1] for _ in size]))
    blank = Image.new("RGB", fsize, (255, 255, 255))
    s = 0
    for im in ims:
        blank.paste(im, (s, 0))
        s += im.size[0]
    if final is not None:
        blank.save(final)
    return blank
