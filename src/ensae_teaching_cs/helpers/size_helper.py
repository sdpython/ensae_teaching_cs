"""
@file
@brief Functions to measure the size of an object.
"""

from sys import getsizeof
from itertools import chain
from collections import deque


def object_size(o):
    """
    Call `getsizeof <https://docs.python.org/3/library/sys.html#sys.getsizeof>`_.

    @param      o       object
    @return             size of the object, that excludes references objects.
    """
    return getsizeof(o)


def total_size(o, handlers=None):
    """
    Returns the approximate memory footprint an object and all of its contents.

    @param      o           object to measure
    @param      handlers    for recursivity purpose
    @return                 total size

    Automatically finds the contents of the following builtin containers and
    their subclasses:  tuple, list, deque, dict, set and frozenset.
    To search other containers, add handlers to iterate over their contents:

    ::

        handlers = {SomeContainerClass: iter,
                    OtherContainerClass: OtherContainerClass.get_elements}

    Source : `activestate <https://code.activestate.com/recipes/577504/>`_
    referenced by function `getsizeof <https://docs.python.org/3/library/sys.html#sys.getsizeof>`_.
    """
    if handlers is None:
        handlers = {}

    def dict_handler(d): return chain.from_iterable(d.items())
    all_handlers = {tuple: iter, list: iter, deque: iter, dict: dict_handler,
                    set: iter, frozenset: iter}
    all_handlers.update(handlers)     # user handlers take precedence
    seen = set()                      # track which object id's have already been seen
    # estimate sizeof object without __sizeof__
    default_size = getsizeof(0)

    def sizeof(o):
        if id(o) in seen:       # do not double count the same object
            return 0
        seen.add(id(o))
        s = getsizeof(o, default_size)

        for typ, handler in all_handlers.items():
            if isinstance(o, typ):
                s += sum(map(sizeof, handler(o)))
                break
        return s

    return sizeof(o)
