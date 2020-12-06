import pandas
import matplotlib.pyplot as plt

url = "pypi_downloads.csv"
df = pandas.read_csv(url)
df.sort_values(["month", "Project"]).to_csv("pypi_downloads.sorted.csv", index=False)
df = df.groupby(["Project", "month"], as_index=False).sum()
df = df.sort_values(["Project", "month"])
df['month'] = df.month.astype(str)
df = df[df.month >= "2017"]
gr = df.groupby("Project", as_index=False).sum().sort_values(
    "num_downloads").reset_index(drop=True)
med = gr.iloc[gr.shape[0] // 2, 1]

sets = [
    {'skl2onnx', 'onnxruntime', 'onnxmltools',
     'keras2onnx', 'tensorflow-onnx', 'onnxconverter-common',
     'ort-customops'},
    {'onnx'},
    {'jyquickhelper', 'pymyinstall', 'pyquickhelper', 'pyensae'},
    {'manydataapi', 'cpyquickhelper', 'mlstatpy', },
    {'mlinsights', 'mlprodict', },
    {'csharpy', 'csharpyml', },
    {'lightmlboard', 'lightmlrestapi', 'pyrsslocal', 'pymmails', },
    {'sparkouille', 'ensae_projects', 'actuariat_python', 'code_beatrix', 'jupytalk'},
    {'papierstat', 'teachpyx', 'ensae_teaching_cs', 'ensae_teaching_dl', 'teachpyx',
     'aftercovid', 'onnxcustom'},
    {'tkinterquickhelper', 'pysqllike', 'pyenbc', },
    {'nimbusml', },
    {'numpy', 'pandas', 'jupyter', 'matplotlib'},
]

piv = df.pivot("month", "Project", "num_downloads").fillna(0)

fig, ax = plt.subplots(len(sets), 1, figsize=(12, 40))
colormaps = ['Accent', "tab10", "Paired", "tab20"]
for i in range(len(sets)):
    sub = sets[i].intersection(set(df['Project']))
    piv2 = piv[sub]
    piv2.plot.area(colormap=colormaps[i % len(colormaps)], ax=ax[i])
    ax[i].set_xticks(list(range(0, len(piv2.index), 2)))
    ax[i].set_xticklabels(list(piv2.index)[::2], rotation=30)

plt.show()
