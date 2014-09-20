#-*- coding: utf-8 -*-
"""
@file
@brief Helpers autour de C#
"""
import os, sys, copy, random

def create_cs_function(name, code, dependencies = None):
    """
    creates a C# function from a string
    
    @param      name            function name
    @param      code            function code
    @param      dependencies    dependencies, ex: 'System.Draw.dll'
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
    
    obj = MagicCS.CreateFunction(name, code, myarray)
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
