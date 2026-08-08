"""
Funciones de validación de compuestos químicos usando RDKit.
Paso 1: Curación del true-positive set.
"""
from rdkit import Chem
from rdkit.Chem import rdMolDescriptors


def validar_compuesto(smiles: str):
    """
    Valida un SMILES y devuelve fórmula molecular, InChIKey y SMILES canónico.

    Parameters
    ----------
    smiles : str
        Cadena SMILES a validar.

    Returns
    -------
    tuple
        (formula, inchikey, smiles_canonico) o (None, None, None) si es inválido.
    """
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return None, None, None

    formula = rdMolDescriptors.CalcMolFormula(mol)
    inchi = Chem.MolToInchi(mol)
    inchikey = Chem.InchiToInchiKey(inchi)
    canon_smiles = Chem.MolToSmiles(mol)

    return formula, inchikey, canon_smiles


def verificar_formula(formula_calculada: str, formula_reportada: str) -> bool:
    """Compara la fórmula calculada contra la reportada en el paper."""
    return formula_calculada == formula_reportada
