import json, os

base = r'c:\Users\isave\OneDrive\Documentos\Ciencia de datos\legal-text-classification\notebooks'

for nb_name in ['01_eda.ipynb', '02_baseline_analysis.ipynb']:
    path = os.path.join(base, nb_name)
    with open(path, 'rb') as f:
        nb = json.load(f)
    print(f'=== {nb_name} ({len(nb["cells"])} celdas) ===')
    for i, c in enumerate(nb['cells']):
        src = ''.join(c['source'])[:80].replace('\n',' ')
        print(f'  [{i}] {c["cell_type"]}: {src}')
    print()
