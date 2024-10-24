# __init__.py

from .core import (
    type_data, getGene_info, getGenes_by_coord, getProtein_info, getPhenotype,
    getCRM_info, getCRM_add_info, getCRMs_by_coord, getTAD_info,
    getTAD_add_info, getTADs_by_coord, gene2protein, protein2gene,
    gene2phen, phen2gene, prot2bp, bp2prot, prot2cc, cc2prot, prot2mf,
    mf2prot, gene2crm, crm2gene, tfac2crm, crm2tfac, crm2phen, phen2crm,
    tfac2gene, gene2tfac, prot2prot, prot2ortho, prot_regulates, prot_regulated_by
)
from .utils import data_processing, translate_chr

__all__ = [
    'type_data', 'getGene_info', 'getGenes_by_coord', 'data_processing',
    'translate_chr', 'getPhenotype', 'getProtein_info', 'getCRM_info',
    'getCRM_add_info', 'getCRMs_by_coord', 'getTAD_info',
    'getTAD_add_info', 'getTADs_by_coord', 'gene2protein', 'protein2gene',
    'gene2phen', 'phen2gene', 'prot2bp', 'bp2prot', 'prot2cc', 'cc2prot',
    'prot2mf', 'mf2prot', 'gene2crm', 'crm2gene', 'tfac2crm', 'crm2tfac',
    'crm2phen', 'phen2crm', 'tfac2gene', 'gene2tfac', 'prot2prot', 'prot2ortho', 'prot_regulates', 'prot_regulated_by' 
]