# chemprops

Calculate chemical properties of a molecule from a SMILES string using RDKit.

Properties returned: canonical SMILES, molecular formula, molecular weight,
LogP, TPSA, H-bond donors/acceptors, rotatable bonds, ring count, heavy atom
count, QED drug-likeness score, and Lipinski rule-of-five violations.

## Install

```
pip install .
```

## Usage

As a library:

```python
from chemprops import calc_properties

props = calc_properties('CC(=O)Oc1ccccc1C(=O)O')  # aspirin
print(props['molecular_weight'], props['logp'])
```

As a CLI (prints JSON):

```
chemprops 'CC(=O)Oc1ccccc1C(=O)O'
```

## Use as a MARA tool

Import this repo via **Tools → Import from GitHub**. Example glue code:

```python
import json
from chemprops import calc_properties

def run(smiles):
    return json.dumps(calc_properties(smiles), indent=2)
```

with one string argument `smiles`.

This repo declares its RDKit dependency in `pyproject.toml`, but that is just
one way to do it. Import from GitHub also detects dependencies from
`setup.py`, `requirements.txt`, `environment.yml` (conda packages), and a
`Dockerfile` (apt packages).
