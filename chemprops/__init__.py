import json
import sys

from rdkit import Chem
from rdkit.Chem import Descriptors, QED, rdMolDescriptors


def calc_properties(smiles: str) -> dict:
    """Calculate physicochemical properties for a SMILES string."""
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        raise ValueError(f'Invalid SMILES: {smiles}')
    return {
        'smiles': Chem.MolToSmiles(mol),
        'formula': rdMolDescriptors.CalcMolFormula(mol),
        'molecular_weight': round(Descriptors.MolWt(mol), 2),
        'logp': round(Descriptors.MolLogP(mol), 2),
        'tpsa': round(Descriptors.TPSA(mol), 2),
        'h_bond_donors': Descriptors.NumHDonors(mol),
        'h_bond_acceptors': Descriptors.NumHAcceptors(mol),
        'rotatable_bonds': Descriptors.NumRotatableBonds(mol),
        'ring_count': rdMolDescriptors.CalcNumRings(mol),
        'heavy_atoms': mol.GetNumHeavyAtoms(),
        'qed': round(QED.qed(mol), 3),
        'lipinski_violations': sum([
            Descriptors.MolWt(mol) > 500,
            Descriptors.MolLogP(mol) > 5,
            Descriptors.NumHDonors(mol) > 5,
            Descriptors.NumHAcceptors(mol) > 10,
        ]),
    }


def main():
    if len(sys.argv) != 2:
        print('usage: chemprops <smiles>', file=sys.stderr)
        sys.exit(1)
    print(json.dumps(calc_properties(sys.argv[1]), indent=2))
