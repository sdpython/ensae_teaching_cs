
Convert a notebook into a document
==================================

First, we need to retrieve the notebook name (see `How to I get the
current IPython Notebook
name <http://stackoverflow.com/questions/12544056/how-to-i-get-the-current-ipython-notebook-name>`__):

.. code:: python

    %%javascript
    var kernel = IPython.notebook.kernel;
    var body = document.body,  
        attribs = body.attributes;
    var command = "theNotebook = " + "'"+attribs['data-notebook-name'].value+"'";
    kernel.execute(command);


.. parsed-literal::

    <IPython.core.display.Javascript at 0x76c4d70>


.. code:: python

    theNotebook



.. parsed-literal::

    'notebook_convert.ipynb'



On Windows, you need to execute the following trick (see `Pywin32 does
not find its
DLL <http://www.xavierdupre.fr/blog/2014-07-01_nojs.html>`__).

.. code:: python

    from pyquickhelper.helpgen.utils_pywin32 import import_pywin32
    import_pywin32()
Then, we call the following code:

.. code:: python

    from IPython.nbconvert import HTMLExporter
    exportHtml = HTMLExporter()
    body,resources = exportHtml.from_filename(theNotebook)
    with open("conv_notebook.html","w",encoding="utf8") as f : f.write(body)
We can do it with the RST format (see
`RSTExporter <http://ipython.org/ipython-doc/2/api/generated/IPython.nbconvert.exporters.rst.html>`__
or in Python with
`PythonExporter <http://ipython.org/ipython-doc/2/api/generated/IPython.nbconvert.exporters.python.html?highlight=pythonexporter#IPython.nbconvert.exporters.python.PythonExporter>`__).

.. code:: python

    from IPython.nbconvert import RSTExporter
    exportRst = RSTExporter()
    body,resources = exportRst.from_filename(theNotebook)
    with open("conv_notebook.rst","w",encoding="utf8") as f : f.write(body)
If you need to add custom RST instructions, you could add HTML comments:

.. raw:: html

   <!--RST..index:: conversion,nbconvert -->

``<!--RST ..index:: conversion,nbconvert -->``

And write custom code to add it to your RST file.

Finally, if you want to retrieve the download a local file such as the
RST conversion for example:

.. code:: python

    from IPython.display import FileLink
    FileLink("conv_notebook.rst")



.. raw:: html

    <a href='conv_notebook.rst' target='_blank'>conv_notebook.rst</a><br>



