"""
The following example was created using a cusom assembly 
written in C#: sample_csharp_dll. It contains 
a public static class (StaticClassExample) and an object (ObjectClass). The 
following code show how to call it from Python
using module clr.

@code
CLR.AddReference(filen.replace(".dll",""))
from sample_csharp_dll import StaticClassExample
x = StaticClassExample.PlusOne( 2)
pritn (x)

li = [ "d", "a", "c", "a" ]
so = StaticClassExample.SortStringArray(li)
so = [ s for s in so ]
print (so)

from sample_csharp_dll import ObjectClass
obj = ObjectClass("na")
s = str(obj)
@endcode
"""
def __bootstrap__():
   global __bootstrap__, __loader__, __file__
   """
   import sys, pkg_resources, imp
   __file__ = pkg_resources.resource_filename(__name__,'clr.pyd')
   __loader__ = None; del __bootstrap__, __loader__
   imp.load_dynamic(__name__,__file__)
   """
__bootstrap__()
