#-*- coding: utf-8 -*-
"""
@file
@brief Helpers autour de C#
"""
import os, sys, copy, random

def create_cs_function(name, code, dependencies = None, usings = None):
    """
    creates a C# function from a string
    
    @param      name            function name
    @param      code            function code
    @param      dependencies    dependencies, ex: 'System.Draw.dll'
    @param      usings          usings to add
    @return                     function object
    """
    from ..pythonnet import import_magic_cs
    MagicCS = import_magic_cs()
    from System import String
    from System.Collections.Generic import List

    if dependencies is not None and len(dependencies) > 0 :
        myarray = List[String]()
        for i,d in enumerate(dependencies):
            myarray.Add( d )
        myarray = myarray.ToArray()
    else:
        myarray = List[String]().ToArray()
    
    if usings is not None and len(usings) > 0 :
        myusings = List[String]()
        for i,d in enumerate(usings):
            myusings.Add( d )
        myusings = myusings.ToArray()
    else:
        myusings = List[String]().ToArray()
    
    obj = MagicCS.CreateFunction(name, code, myarray, myusings)
    return lambda *params: run_cs_function(obj, params)

def run_cs_function(func, params):
    """
    runs a C# function with the given parameters
    
    @param      func        object created by function @see fn create_cs_function
    @param      params      list of parameters
    @return                 result of the function ``func``
    """
    from ..pythonnet import import_magic_cs
    MagicCS = import_magic_cs()
    from System.Collections.Generic import List
    from System import Object

    par = List[Object]()
    for p in params :
        par.Add ( p )
    return MagicCS.RunFunction(func, par.ToArray())

def list2arrayint(li):
    """
    converts a list into a C# array of int
    """
    from ..pythonnet import import_magic_cs
    MagicCS = import_magic_cs()
    par = MagicCS.NewListIntLong()
    for i in li :
        par.Add(i)
    return par.ToArray()
    