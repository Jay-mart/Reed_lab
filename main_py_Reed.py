import requests
from rdkit import Chem
from rdkit.Chem import Descriptors
from rdkit.Chem import Draw

"""
A script to explore using pubchem API
"""

# adding a new molecule
mol = Chem.MolFromSmiles("C1CC2=C3C(=CC=C2)C(=CN3C1)[C@H]4[C@@H](C(=O)NC4=O)C5=CNC6=CC=CC=C65")

logp = Descriptors.MolLogP(mol, includeHs=True)
print('This is the logp from smile', logp)

response = requests.get('https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/vioxx/property/InChI/TXT')
inchi_input = response.text.strip('\n')
inchi_mol = Chem.MolFromInchi(inchi_input)  # , sanitize=False, removeHs=False)

logp = Descriptors.MolLogP(inchi_mol, includeHs=True)
print('This is the logp of vioxx', logp)
mol_list = []
mol_list.append(inchi_mol)
Draw.MolsToGridImage(mol_list)
img = Draw.MolsToGridImage(mol_list)
img.save('output.png')

# This is my attempt using the drug Testosterone-cypionate ##########################################################
# most common ester used in US half-life approx 7-8 days

response = requests.get(f'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/Testosterone-cypionate/property'
                        f'/InChI/TXT')
inchi_input = response.text.strip('\n')
inchi_mol = Chem.MolFromInchi(inchi_input)

logp = Descriptors.MolLogP(inchi_mol, includeHs=True)
print('This is the logp of Testosterone cypionate', logp)
mol_list_oxaliplatin = []
mol_list.append(inchi_mol)
Draw.MolsToGridImage(mol_list)
img = Draw.MolsToGridImage(mol_list)
img.save('output.png')

# This is my attempt using the drug Testosterone-propionate  #########################################################
# Shorts acting ester half-life of approx 2 days

response = requests.get(f'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/Testosterone-propionate/property'
                        f'/InChI/TXT')
inchi_input = response.text.strip('\n')
inchi_mol = Chem.MolFromInchi(inchi_input)

logp = Descriptors.MolLogP(inchi_mol, includeHs=True)
print('This is the logp of Testosterone propionate', logp)
mol_list_cisplatin = []
mol_list.append(inchi_mol)
Draw.MolsToGridImage(mol_list)
img = Draw.MolsToGridImage(mol_list)
img.save('output.png')

# This is my attempt using the drug Testosterone-enanthate #########################################################
# This is used most commonly cross the world. Especially Europe. Very similar to TC similar half-life, very similar logp

response = requests.get(f'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/Testosterone-enanthate/property'
                        f'/InChI/TXT')
inchi_input = response.text.strip('\n')
inchi_mol = Chem.MolFromInchi(inchi_input)

logp = Descriptors.MolLogP(inchi_mol, includeHs=True)
print('This is the logp of Testosterone enanthate', logp)
mol_list_cisplatin = []
mol_list.append(inchi_mol)
Draw.MolsToGridImage(mol_list)
img = Draw.MolsToGridImage(mol_list)
img.save('output.png')
