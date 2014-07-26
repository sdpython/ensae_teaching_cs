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