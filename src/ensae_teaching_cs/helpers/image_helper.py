"""
@file
@brief image helpers
"""
import os
from PIL import Image


def collate_images(imgs, final=None):
    """
    Collates all images horizontally in one image (if not None --> image name).

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


def convert_image(imgs, ext, dest=None, fLOG=None):
    """
    Converts an image or a list of images into a different format.

    @param      imgs        list of images (filenames)
    @param      dest        destination folder, if None, the image is saved beside the orginal one
    @param      ext         new format
    @param      fLOG        logging function
    @return                 list of written images
    """
    if isinstance(imgs, str):
        imgs = [imgs]
    if not isinstance(ext, str):
        raise TypeError("ext must a string")
    if len(ext) == 0:
        raise ValueError("ext must not be empty")
    if ext.startswith("."):
        raise ValueError(f"ext must not start with a point '{ext}'")
    saved = []
    for img in imgs:
        if fLOG is not None:
            fLOG("[convert_image]", img)
        obj = Image.open(img)
        if dest is None:
            folder = os.path.dirname(img)
        else:
            folder = dest
        name = os.path.splitext(os.path.split(img)[-1])[0]
        new_name = os.path.join(folder, name + "." + ext)
        obj.save(new_name)
        saved.append(new_name)
    return saved
