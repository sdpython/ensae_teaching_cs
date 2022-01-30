
Pypi download
=============

.. index:: pypi, pypi download

Le nombre de téléchargements peut être
obtenu en exécutant la requête suivante sur
`Google BigQuery <https://console.cloud.google.com/bigquery>`_.
On peut retrouver la plupart de ces résultats sur
`pypistat <https://pypistats.org/>`_. Exemple avec
`pypistat/mlinsights <https://pypistats.org/packages/mlinsights>`_.

.. runpython::
    :showcode:

    query = """
    SELECT
        file.project AS Project,
        COUNT(*) AS num_downloads,
        FORMAT_DATE("%Y%m", DATE(timestamp)) AS Month
    FROM `bigquery-public-data.pypi.file_downloads`
    WHERE
      (__CONDITION__)
      AND DATE(timestamp)
        BETWEEN DATE_TRUNC(DATE_SUB(CURRENT_DATE(), INTERVAL 2 MONTH), MONTH)
        AND CURRENT_DATE()
     GROUP BY `Project`, `Month`
     ORDER BY `Month`, `Project`
    """

    from ensae_teaching_cs.automation import get_teaching_modules
    modules = get_teaching_modules(branch=False)
    modules.extend([
        'onnx', 'onnxruntime', 'skl2onnx', 'keras2onnx', 'nimbusml',
        'scikit-learn', 'pandas', 'numpy', 'jupyter', 'matplotlib',
        'protobuf', 'nimbusml', 'aftercovid', 'onnxruntime-training',
        'onnxconverter-common', 'tf2onnx', 'onnxruntime-extensions'])
    modules = [m.split(':')[0] for m in modules]
    dont = {'numpy', 'matplotlib', 'pandas', 'jupyter'}
    modules = [_ for _ in modules if _ not in dont]
    conds = ["file.project = '{0}'".format(m) for m in modules]
    cond = " OR ".join(conds)
    print(query.replace('__CONDITION__', cond))

.. plot::

    import pandas
    import matplotlib.pyplot as plt

    url = "pypi_downloads.csv"
    df = pandas.read_csv(url)
    df = df.groupby(["Project", "month"], as_index=False).sum()
    df = df.sort_values(["Project", "month"])
    df['month'] = df.month.astype(str)
    df = df[df.month >= "2017"]
    gr = df.groupby("Project", as_index=False).sum().sort_values(
        "num_downloads").reset_index(drop=True)
    med = gr.iloc[gr.shape[0]//2, 1]

    sets = [
        {'skl2onnx', 'onnxmltools',
         'tf2onnx', 'onnxconverter-common',
         'onnxruntime-extensions'},
        {'onnx'},
        {'onnxruntime'},
        {'onnxruntime-training'},
        {'jyquickhelper', 'pymyinstall', 'pyquickhelper', 'pyensae'},
        {'manydataapi', 'cpyquickhelper', 'mlstatpy', },
        {'mlinsights', 'mlprodict', 'onnxortext'},
        {'csharpy', 'csharpyml', },
        {'lightmlboard', 'lightmlrestapi', 'pyrsslocal', 'pymmails', },
        {'sparkouille', 'ensae_projects', 'actuariat_python', 'code_beatrix', 'jupytalk'},
        {'papierstat', 'teachpyx', 'ensae_teaching_cs', 'ensae_teaching_dl', 'teachpyx',
         'aftercovid', 'onnxcustom', 'deeponnxcustom'},
        {'tkinterquickhelper', 'pysqllike', 'pyenbc', },
        {'nimbusml', },
        {'scikit-learn'},
    ]

    piv = df.pivot("month", "Project", "num_downloads").fillna(0)

    fig, ax = plt.subplots(len(sets), 1, figsize=(12,40))
    colormaps = ['Accent', "tab10", "Paired", "tab20"]
    for i in range(len(sets)):
        sub = sets[i].intersection(set(df['Project']))
        piv2 = piv[sub]
        piv2.plot.area(colormap=colormaps[i % len(colormaps)], ax=ax[i])
        ax[i].set_xticks(list(range(0, len(piv2.index), 2)))
        ax[i].set_xticklabels(list(piv2.index)[::2], rotation=30)

    plt.show()
