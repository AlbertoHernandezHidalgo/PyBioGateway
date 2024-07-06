# tests/test_core.py
import unittest
from PyBioGateway import *

class TestBioGatewayQuery(unittest.TestCase):

    def test_type_data(self):
        self.assertEqual(type_data("INSR_HUMAN"), "protein")
        self.assertEqual(type_data("INSR"), "gene")
        self.assertEqual(type_data("crm/CRMHS00000003514"), "cis_regulatory_module (crm)")
        self.assertEqual(type_data("tad/TADHS00000020654"), "topologically_associated_domain (tad)")
        self.assertEqual(type_data("GO:0034703"), "cellular_component")
        self.assertEqual(type_data("GO:0043524"), "biological_process")
        self.assertEqual(type_data("GO:0003723"), "molecular_function")
        self.assertEqual(type_data("World"), 'No data available for this instance')
        
    def test_getGene_info(self):
        expected= {'start': '52436415',
 'end': '52547802',
 'strand': 'ReverseStrandPosition',
 'chr': 'NC_000016.10',
 'assembly': 'GCF_000001405.26',
 'alt_gene_sources': 'ensembl/ENSG00000103460.17; ncbigene/27324',
 'definition': 'gene 9606/TOX3 encoding [H3BTZ9_HUMAN J3QQQ6_HUMAN TOX3_HUMAN]'}
        self.assertEqual(getGene_info("TOX3", "9606"), expected)
        self.assertEqual(getGene_info("TOX3", "Homo sapiens"), expected)
        self.assertEqual(getGene_info("INVALID", "9606"), "No data available for the introduced gene or you may have introduced an instance that is not a gene. Check your data type with type_data function.")
    
    def test_getGenes_by_coord(self):
        expected_1=[{'gene_name': 'Fzd8', 'start': '57312924', 'end': '57320551'},
 {'gene_name': 'Hist2h3c2', 'start': '183797721', 'end': '41378877'},
 {'gene_name': 'Hist2h3c2', 'start': '183837311', 'end': '41532577'},
 {'gene_name': 'Hist2h3c2', 'start': '183797721', 'end': '41532577'},
 {'gene_name': 'Hist2h3c2', 'start': '183837311', 'end': '41426735'},
 {'gene_name': 'Hist2h3c2', 'start': '183837311', 'end': '41378877'},
 {'gene_name': 'Hist2h3c2', 'start': '183797721', 'end': '41426735'},
 {'gene_name': 'Hnrnpk', 'start': '91756628', 'end': '6275001'},
 {'gene_name': 'Lgals8', 'start': '58024652', 'end': '58052764'},
 {'gene_name': 'Map3k8', 'start': '53382908', 'end': '53403216'},
 {'gene_name': 'Mtr', 'start': '58219998', 'end': '58308560'},
 {'gene_name': 'Actn2', 'start': '58143334', 'end': '58210622'},
 {'gene_name': 'Crem', 'start': '54238889', 'end': '54305989'},
 {'gene_name': 'RGD1560860', 'start': '54808184', 'end': '54847675'},
 {'gene_name': 'RGD1564129', 'start': '54151572', 'end': '54808145'},
 {'gene_name': 'RGD1564129', 'start': '54151572', 'end': '54154198'},
 {'gene_name': 'RGD1564129', 'start': '54800565', 'end': '54154198'},
 {'gene_name': 'RGD1564129', 'start': '54800565', 'end': '54808145'},
 {'gene_name': 'Rab18', 'start': '54944099', 'end': '54976093'},
 {'gene_name': 'Wac', 'start': '55922686', 'end': '55984286'}]
        expected_2=[{'gene_name': 'Hist2h3c2',
  'start': '183837311',
  'end': '41426735',
  'strand': 'ForwardStrandPosition'},
 {'gene_name': 'Hist2h3c2',
  'start': '183837311',
  'end': '41426735',
  'strand': 'ReverseStrandPosition'},
 {'gene_name': 'Hist2h3c2',
  'start': '183837311',
  'end': '41378877',
  'strand': 'ForwardStrandPosition'},
 {'gene_name': 'Hist2h3c2',
  'start': '183837311',
  'end': '41378877',
  'strand': 'ReverseStrandPosition'},
 {'gene_name': 'Hist2h3c2',
  'start': '183797721',
  'end': '41532577',
  'strand': 'ForwardStrandPosition'},
 {'gene_name': 'Hist2h3c2',
  'start': '183797721',
  'end': '41532577',
  'strand': 'ReverseStrandPosition'},
 {'gene_name': 'Hist2h3c2',
  'start': '183797721',
  'end': '41378877',
  'strand': 'ForwardStrandPosition'},
 {'gene_name': 'Hist2h3c2',
  'start': '183797721',
  'end': '41378877',
  'strand': 'ReverseStrandPosition'},
 {'gene_name': 'Hist2h3c2',
  'start': '183797721',
  'end': '41426735',
  'strand': 'ForwardStrandPosition'},
 {'gene_name': 'Hist2h3c2',
  'start': '183797721',
  'end': '41426735',
  'strand': 'ReverseStrandPosition'},
 {'gene_name': 'Hist2h3c2',
  'start': '183837311',
  'end': '41532577',
  'strand': 'ForwardStrandPosition'},
 {'gene_name': 'Hist2h3c2',
  'start': '183837311',
  'end': '41532577',
  'strand': 'ReverseStrandPosition'},
 {'gene_name': 'Hnrnpk',
  'start': '91756628',
  'end': '6275001',
  'strand': 'ForwardStrandPosition'},
 {'gene_name': 'Hnrnpk',
  'start': '91756628',
  'end': '6275001',
  'strand': 'ReverseStrandPosition'},
 {'gene_name': 'Rplp1',
  'start': '62394008',
  'end': '8432740',
  'strand': 'ReverseStrandPosition'}]
        
        self.assertEqual(getGenes_by_coord("NC_051352.1", 52565276 , 58596412 ,"ForwardStrandPosition"),expected_1)
        self.assertEqual(getGenes_by_coord("NC_051352.1", 58500000 , 58500900 ,None),expected_2)
        self.assertEqual(getGenes_by_coord("WORLD", 58500000 , 58500900 ,None),"No data available for the introduced genomic coordinates.")
        
    def test_getProtein_info(self):
        expected= {'protein_alt_ids': 'O15405; TOX3; TNRC9; CAGF9', 'definition': 'TOX high mobility group box family member 3 (CAG trinucleotide repeat-containing gene F9 protein) (Trinucleotide repeat-containing gene 9 protein)', 'evidence_level': '5.0', 'alt_sources': 'ensembl/ENSP00000219746.9; ensembl/ENSP00000385705.3; refseq/NP_001073899.2; refseq/NP_001139660.1', 'articles': 'pubmed/15616553; pubmed/9225980; pubmed/21172805; pubmed/14702039'}
        self.assertEqual(getProtein_info("TOX3_HUMAN"),expected)
        self.assertEqual(getProtein_info("WORLD"), "No data available for the introduced protein or you may have introduced an instance that is not a protein. Check your data type with type_data function.")
        
    def test_getPhenotype(self):
        expected_1=[{'omim_id': 'MTHU052262',
  'label': 'Increased risk of other cancers (e.g., kidney cancer, lung cancer, and leukemia)'},
 {'omim_id': 'MTHU074383', 'label': 'Increased risk for lung cancer'},
 {'omim_id': '608935', 'label': 'LUNG CANCER SUSCEPTIBILITY 1'},
 {'omim_id': '211980', 'label': 'LUNG CANCER'},
 {'omim_id': 'MTHU063395', 'label': 'Nonsmall cell lung cancer'},
 {'omim_id': 'MTHU001565',
  'label': 'Statistical association of extensive metabolism (EM, wildtype) and malignancy, especially smoking-induced lung cancer'},
 {'omim_id': '614210', 'label': 'LUNG CANCER SUSCEPTIBILITY 5'},
 {'omim_id': '612571', 'label': 'LUNG CANCER SUSCEPTIBILITY 3'},
 {'omim_id': '618190',
  'label': 'LUNG CANCER-ASSOCIATED TRANSCRIPT 1, NONCODING'},
 {'omim_id': '612593', 'label': 'LUNG CANCER SUSCEPTIBILITY 4'},
 {'omim_id': '211980', 'label': 'LUNG CANCER, PROTECTION AGAINST'},
 {'omim_id': '211980', 'label': 'NONSMALL CELL LUNG CANCER'},
 {'omim_id': '118503', 'label': 'LUNG CANCER SUSCEPTIBILITY 2'},
 {'omim_id': '118505', 'label': 'LUNG CANCER SUSCEPTIBILITY 2'},
 {'omim_id': '122720', 'label': 'LUNG CANCER, PROTECTION AGAINST'},
 {'omim_id': '131550',
  'label': 'NONSMALL CELL LUNG CANCER, RESPONSE TO TYROSINE KINASE INHIBITOR IN, SOMATIC'},
 {'omim_id': '131550',
  'label': 'NONSMALL CELL LUNG CANCER, RESISTANCE TO TYROSINE KINASE INHIBITOR IN'},
 {'omim_id': '134637', 'label': 'LUNG CANCER, SUSCEPTIBILITY TO'},
 {'omim_id': '134638', 'label': 'LUNG CANCER, SUSCEPTIBILITY TO'},
 {'omim_id': '147575', 'label': 'NONSMALL CELL LUNG CANCER, SOMATIC'},
 {'omim_id': '164757', 'label': 'NONSMALL CELL LUNG CANCER, SOMATIC'},
 {'omim_id': '171834', 'label': 'NONSMALL CELL LUNG CANCER, SOMATIC'},
 {'omim_id': '190070', 'label': 'LUNG CANCER, SQUAMOUS CELL, SOMATIC'},
 {'omim_id': '190070', 'label': 'LUNG CANCER, SOMATIC'},
 {'omim_id': '300625', 'label': 'KITA-KYUSHU LUNG CANCER ANTIGEN 1'},
 {'omim_id': '601763', 'label': 'LUNG CANCER, PROTECTION AGAINST'},
 {'omim_id': '602631', 'label': 'LUNG CANCER, SOMATIC'},
 {'omim_id': '603040', 'label': 'NONSMALL CELL LUNG CANCER SUPPRESSOR'},
 {'omim_id': '603113', 'label': 'LUNG CANCER, SOMATIC'},
 {'omim_id': '603963',
  'label': 'ALPHA RELATED TO THE DEVELOPMENT OF LUNG CANCER'},
 {'omim_id': '605686', 'label': 'TUMOR SUPPRESSOR IN LUNG CANCER 1'},
 {'omim_id': '606989', 'label': 'LUNG CANCER, PROTECTION AGAINST, IN SMOKERS'},
 {'omim_id': '609413', 'label': 'LUNG CANCER, SUSCEPTIBILITY TO'},
 {'omim_id': '612052', 'label': 'LUNG CANCER SUSCEPTIBILITY 2'},
 {'omim_id': '612385', 'label': 'LUNG CANCER METASTASIS-RELATED PROTEIN 1'},
 {'omim_id': '616203', 'label': 'UPREGULATED IN LUNG CANCER 11'},
 {'omim_id': '619277', 'label': 'LOST IN LUNG CANCER 1'},
 {'omim_id': '164850', 'label': 'MYC-RELATED GENE FROM LUNG CANCER'},
 {'omim_id': '610958', 'label': 'LUNG CANCER METASTASIS-ASSOCIATED GENE 1'}]
        expected_2= [{'phen_label': 'BREAST CANCER ANTIESTROGEN RESISTANCE 3'}]
        self.assertEqual(getPhenotype("lung cancer"),expected_1)
        self.assertEqual(getPhenotype("604704"), expected_2)
        self.assertEqual(getPhenotype("WORLD"), "No data available for the introduced phenotype or you may have introduced an instance that is not a phenotype. Check your data type with type_data function.")
    
    def test_getCRM_info(self):
        
        expected=[{'start': '355447',
      'end': '358949',
      'chromosome': 'NC_000011.10',
      'assembly': 'GCF_000001405.26',
      'taxon': 'NCBITaxon_9606',
      'definition': 'Cis-regulatory module located in Homo sapiens chr11 between 355447 and 358949'}]

        self.assertEqual(getCRM_info("crm/CRMHS00000005387"),expected)
        self.assertEqual(getCRM_info("WORLD"), "No data available for the introduced crm or you may have introduced an instance that is not a crm. Check your data type with type_data function.")
    
    def test_getCRM_add_info(self):
        
        expected={'evidence': 'http://www.licpathway.net/ENdb/search/Detail.php?Species=Human&Enhancer_id=E_01_273',
 'database': 'http://www.licpathway.net/ENdb/',
 'biological_samples': 'BTO_0000007; BTO_0000018; CLO_0001230; CLO_0001601; CL_0002518; CL_0000082; UBERON_0002048; UBERON_0002113',
 'articles': 'pubmed/28511927'}

        self.assertEqual(getCRM_add_info("crm/CRMHS00000005387"),expected)
        self.assertEqual(getCRM_add_info("WORLD"), "No data available for the introduced crm or you may have introduced an instance that is not a crm. Check your data type with type_data function.")
        
    def test_getCRMs_by_coord(self):
        expected=[{'crm_name': 'crm/CRMHS00003545627', 'start': '46337', 'end': '47537'},
 {'crm_name': 'crm/CRMHS00003504423', 'start': '40537', 'end': '41937'},
 {'crm_name': 'crm/CRMHS00003521541', 'start': '43137', 'end': '43337'},
 {'crm_name': 'crm/CRMHS00003519683', 'start': '42537', 'end': '43137'},
 {'crm_name': 'crm/CRMHS00003513523', 'start': '41937', 'end': '42537'},
 {'crm_name': 'crm/CRMHS00003533514', 'start': '45137', 'end': '45537'},
 {'crm_name': 'crm/CRMHS00003523619', 'start': '43337', 'end': '43537'},
 {'crm_name': 'crm/CRMHS00001259162', 'start': '46644', 'end': '47040'}]
        self.assertEqual(getCRMs_by_coord("chr-1",40000, 50000), expected)
        self.assertEqual(getCRMs_by_coord("chr-1", 4000000000, 5000000000),"No data available for the introduced genomic coordinates.")
    
    def test_getTAD_info(self):
        expected=[{'start': '34120000',
  'end': '35840000',
  'chromosome': 'NC_000013.11',
  'assembly': 'GCF_000001405.26',
  'taxon': 'NCBITaxon_9606',
  'definition': 'Topologically associated domain located in Homo sapiens chr13 between 34120000 and 35840000'}]
        
        self.assertEqual(getTAD_info("tad/TADHS00000038004"),expected)
        self.assertEqual(getTAD_info("WORLD"), "No data available for the introduced tad or you may have introduced an instance that is not a tad. Check your data type with type_data function.")
    
    def test_getTAD_add_info(self): 
        expected={'evidence': None,
 'database': 'http://3dgenome.fsm.northwestern.edu/index.html',
 'biological_samples': 'BTO_0002914; CLO_0009058; CL_0000031; UBERON_0000955',
 'articles': 'pubmed/30286773'}
        
        self.assertEqual(getTAD_add_info("tad/TADHS00000038004"),expected)
        self.assertEqual(getTAD_add_info("WORLD"), "No data available for the introduced tad or you may have introduced an instance that is not a tad. Check your data type with type_data function.")
        
    def test_getTADs_by_coord(self):
        expected= [{'tad_id': 'tad/TADHS00000038004', 'start': '34120000', 'end': '35840000'},
 {'tad_id': 'tad/TADHS00000029314', 'start': '35200000', 'end': '35840000'},
 {'tad_id': 'tad/TADHS00000071459', 'start': '34125863', 'end': '35175863'},
 {'tad_id': 'tad/TADHS00000071460', 'start': '34165863', 'end': '35825863'},
 {'tad_id': 'tad/TADHS00000071461', 'start': '34185863', 'end': '35155863'},
 {'tad_id': 'tad/TADHS00000071462', 'start': '34305863', 'end': '35455863'},
 {'tad_id': 'tad/TADHS00000071463', 'start': '34325863', 'end': '35025863'},
 {'tad_id': 'tad/TADHS00000071465', 'start': '35150863', 'end': '35800863'},
 {'tad_id': 'tad/TADHS00000071468', 'start': '35170863', 'end': '35810863'},
 {'tad_id': 'tad/TADHS00000071479', 'start': '35195863', 'end': '35815863'},
 {'tad_id': 'tad/TADHS00000071484', 'start': '35215863', 'end': '35825863'},
 {'tad_id': 'tad/TADHS00000071485', 'start': '35225863', 'end': '35825863'},
 {'tad_id': 'tad/TADHS00000071489', 'start': '35375863', 'end': '35725863'},
 {'tad_id': 'tad/TADHS00000071490', 'start': '35375863', 'end': '35775863'},
 {'tad_id': 'tad/TADHS00000071491', 'start': '35375863', 'end': '35825863'},
 {'tad_id': 'tad/TADHS00000071492', 'start': '35425863', 'end': '35725863'}]
        
        self.assertEqual(getTADs_by_coord("chr-13",34120000, 35840000), expected)
        self.assertEqual(getTADs_by_coord("chr-13",3412000000, 3584000000), "No data available for the introduced genomic coordinates.")
      
    def test_gene2protein(self):
        expected=[{'prot_name': 'H3BTZ9_HUMAN'},
 {'prot_name': 'J3QQQ6_HUMAN'},
 {'prot_name': 'TOX3_HUMAN'}]
        self.assertEqual(gene2protein("TOX3","9606"),expected)
        self.assertEqual(gene2protein("TOX3","Homo sapiens"),expected)
        self.assertEqual(gene2protein("WORLD","9606"),"No data available for the introduced gene. Check that the gene id is correct or if you have introduced the taxon correctly.")
        
    def test_protein2gene(self):
        expected=[{'gene_id': 'BRCA1'}]
        
        self.assertEqual(protein2gene("P38398"), expected)
        self.assertEqual(protein2gene("BRCA1_HUMAN"),expected)
        self.assertEqual(protein2gene("WORLD"),"No data available for the introduced protein or you may have introduced an instance that is not a protein. Check your data type with type_data function.")
        
    def test_gene2phen(self):
        expected=[{'omim_id': '114480', 'phen_label': 'Breast cancer (BC)'},
 {'omim_id': '167000', 'phen_label': 'Ovarian cancer (OC)'},
 {'omim_id': '604370',
  'phen_label': 'Breast-ovarian cancer, familial, 1 (BROVCA1)'},
 {'omim_id': '617883',
  'phen_label': 'Fanconi anemia, complementation group S (FANCS)'}]
        
        self.assertEqual(gene2phen("BRCA1"),expected)
        self.assertEqual(gene2phen("WORLD"),"No data available for the introduced gene or you may have introduced an instance is not a gene. Check your data type with type_data function")
    
    def test_phen2gene(self):
        expected=[{'gene_name': 'MXRA5'}, {'gene_name': 'BRAF'}, {'gene_name': 'ERBB2'}, {'gene_name': 'SLC22A18'}]
        
        self.assertEqual(phen2gene("lung cancer"),expected)
        self.assertEqual(phen2gene("211980"),expected)
        self.assertEqual(phen2gene("21198888"),"No data available for the introduced phenotype or you may have introduced an instance that is not a phenotype. Check your data type with type_data function")
        
    def test_prot2bp(self):
        expected=[{'bp_id': 'GO:0006357',
  'bp_label': 'regulation of transcription by RNA polymerase II',
  'relation_label': 'O15405--GO:0006357',
  'database': 'goa/',
  'articles': 'pubmed/21873635'},
 {'bp_id': 'GO:0042981',
  'bp_label': 'regulation of apoptotic process',
  'relation_label': 'O15405--GO:0042981',
  'database': 'goa/',
  'articles': 'pubmed/21172805'},
 {'bp_id': 'GO:0043524',
  'bp_label': 'negative regulation of neuron apoptotic process',
  'relation_label': 'O15405--GO:0043524',
  'database': 'goa/',
  'articles': 'pubmed/21172805'},
 {'bp_id': 'GO:0045944',
  'bp_label': 'positive regulation of transcription by RNA polymerase II',
  'relation_label': 'O15405--GO:0045944',
  'database': 'goa/',
  'articles': 'pubmed/21172805'}]
        
        self.assertEqual(prot2bp("TOX3_HUMAN"),expected)
        self.assertEqual(prot2bp("WORLD"), "No data available for the introduced protein or you may have introduced an instance that is not a protein. Check your data type with type_data function.")
        
    def test_bp2prot(self):
        expected=[{'protein_name': 'AGAP2_HUMAN', 'relation_label': 'Q99490--GO:0043524', 'database': 'goa/', 'articles': 'pubmed/18374643; pubmed/21873635'}, {'protein_name': 'APOE_HUMAN', 'relation_label': 'P02649--GO:0043524', 'database': 'goa/', 'articles': 'pubmed/21873635'}, {'protein_name': 'BCL2_HUMAN', 'relation_label': 'P10415--GO:0043524', 'database': 'goa/', 'articles': 'pubmed/7546744'}, {'protein_name': 'BDNF_HUMAN', 'relation_label': 'P23560--GO:0043524', 'database': 'goa/', 'articles': 'pubmed/21873635'}, {'protein_name': 'BIRC1_HUMAN', 'relation_label': 'Q13075--GO:0043524', 'database': 'goa/', 'articles': 'pubmed/18414036'}, {'protein_name': 'CCL2_HUMAN', 'relation_label': 'P13500--GO:0043524', 'database': 'goa/', 'articles': 'pubmed/12753088'}, {'protein_name': 'CITE1_HUMAN', 'relation_label': 'Q99966--GO:0043524', 'database': 'goa/', 'articles': 'pubmed/21172805'}, {'protein_name': 'CLCF1_HUMAN', 'relation_label': 'Q9UBD9--GO:0043524', 'database': 'goa/', 'articles': 'pubmed/10966616; pubmed/11285233'}, {'protein_name': 'CNTFR_HUMAN', 'relation_label': 'P26992--GO:0043524', 'database': 'goa/', 'articles': 'pubmed/19386761'}, {'protein_name': 'CNTF_HUMAN', 'relation_label': 'P26441--GO:0043524', 'database': 'goa/', 'articles': 'pubmed/10966616; pubmed/21873635'}, {'protein_name': 'CRLF1_HUMAN', 'relation_label': 'O75462--GO:0043524', 'database': 'goa/', 'articles': 'pubmed/10966616'}, {'protein_name': 'FGF20_HUMAN', 'relation_label': 'Q9NP95--GO:0043524', 'database': 'goa/', 'articles': 'pubmed/16988046'}, {'protein_name': 'FOXQ1_HUMAN', 'relation_label': 'Q9C009--GO:0043524', 'database': 'goa/', 'articles': 'pubmed/28947385'}, {'protein_name': 'FZD9_HUMAN', 'relation_label': 'O00144--GO:0043524', 'database': 'goa/', 'articles': 'pubmed/27509850'}, {'protein_name': 'GDNF_HUMAN', 'relation_label': 'P39905--GO:0043524', 'database': 'goa/', 'articles': 'pubmed/21873635; pubmed/8493557'}, {'protein_name': 'GRN_HUMAN', 'relation_label': 'P28799--GO:0043524', 'database': 'goa/', 'articles': 'pubmed/18378771'}, {'protein_name': 'HTRA2_HUMAN', 'relation_label': 'O43464--GO:0043524', 'database': 'goa/', 'articles': 'pubmed/18221368'}, {'protein_name': 'HUNIN_HUMAN', 'relation_label': 'Q8IVG9--GO:0043524', 'database': 'goa/', 'articles': 'pubmed/12787071; pubmed/19386761'}, {'protein_name': 'I27RA_HUMAN', 'relation_label': 'Q6UWB1--GO:0043524', 'database': 'goa/', 'articles': 'pubmed/19386761'}, {'protein_name': 'IL6RB_HUMAN', 'relation_label': 'P40189--GO:0043524', 'database': 'goa/', 'articles': 'pubmed/19386761'}, {'protein_name': 'KPCI_HUMAN', 'relation_label': 'P41743--GO:0043524', 'database': 'goa/', 'articles': 'pubmed/10467349'}, {'protein_name': 'LGMN_HUMAN', 'relation_label': 'Q99538--GO:0043524', 'database': 'goa/', 'articles': 'pubmed/18374643'}, {'protein_name': 'MK_HUMAN', 'relation_label': 'P21741--GO:0043524', 'database': 'goa/', 'articles': 'pubmed/12573468'}, {'protein_name': 'NDNF_HUMAN', 'relation_label': 'Q8TB73--GO:0043524', 'database': 'goa/', 'articles': 'pubmed/20969804'}, {'protein_name': 'NGF_HUMAN', 'relation_label': 'P01138--GO:0043524', 'database': 'goa/', 'articles': 'pubmed/21873635'}, {'protein_name': 'NTF3_HUMAN', 'relation_label': 'P20783--GO:0043524', 'database': 'goa/', 'articles': 'pubmed/21873635'}, {'protein_name': 'NTF4_HUMAN', 'relation_label': 'P34130--GO:0043524', 'database': 'goa/', 'articles': 'pubmed/21873635'}, {'protein_name': 'PA2G3_HUMAN', 'relation_label': 'Q9NZ20--GO:0043524', 'database': 'goa/', 'articles': 'pubmed/17868035'}, {'protein_name': 'PARK7_HUMAN', 'relation_label': 'Q99497--GO:0043524', 'database': 'goa/', 'articles': 'pubmed/22511790; pubmed/22683601'}, {'protein_name': 'PINK1_HUMAN', 'relation_label': 'Q9BXM7--GO:0043524', 'database': 'goa/', 'articles': 'pubmed/18560593'}, {'protein_name': 'PO4F1_HUMAN', 'relation_label': 'Q01851--GO:0043524', 'database': 'goa/', 'articles': 'pubmed/17239249'}, {'protein_name': 'PPT1_HUMAN', 'relation_label': 'P50897--GO:0043524', 'database': 'goa/', 'articles': 'pubmed/10737604; pubmed/11020216'}, {'protein_name': 'PRKN_HUMAN', 'relation_label': 'O60260--GO:0043524', 'database': 'goa/', 'articles': 'pubmed/12628165; pubmed/22511790; pubmed/23985028'}, {'protein_name': 'RETR1_HUMAN', 'relation_label': 'Q9H6L5--GO:0043524', 'database': 'goa/', 'articles': 'pubmed/21873635; pubmed/26040720'}, {'protein_name': 'SEM3E_HUMAN', 'relation_label': 'O15041--GO:0043524', 'database': 'goa/', 'articles': 'pubmed/25985275'}, {'protein_name': 'SET_HUMAN', 'relation_label': 'Q01105--GO:0043524', 'database': 'goa/', 'articles': 'pubmed/18374643'}, {'protein_name': 'SNX6_HUMAN', 'relation_label': 'Q9UNH7--GO:0043524', 'database': 'goa/', 'articles': 'pubmed/27541017'}, {'protein_name': 'SODM_HUMAN', 'relation_label': 'P04179--GO:0043524', 'database': 'goa/', 'articles': 'pubmed/17251466'}, {'protein_name': 'TOX3_HUMAN', 'relation_label': 'O15405--GO:0043524', 'database': 'goa/', 'articles': 'pubmed/21172805'}, {'protein_name': 'UNC5B_HUMAN', 'relation_label': 'Q8IZJ1--GO:0043524', 'database': 'goa/', 'articles': 'pubmed/18469807'}, {'protein_name': 'VTM2L_HUMAN', 'relation_label': 'Q96N03--GO:0043524', 'database': 'goa/', 'articles': 'pubmed/21393573'}, {'protein_name': 'WFS1_HUMAN', 'relation_label': 'O76024--GO:0043524', 'database': 'goa/', 'articles': 'pubmed/9771706; pubmed/9817917'}]
        self.assertEqual(bp2prot("GO:0043524","Homo sapiens"),expected)
        self.assertEqual(bp2prot("GO:0043524","9606"),expected)
        self.assertEqual(bp2prot("negative regulation of neuron apoptotic process","Homo sapiens"),expected)
        self.assertEqual(bp2prot("negative regulation of neuron apoptotic process","9606"),expected)
        self.assertEqual(bp2prot("WORLD", "TAXON"),"No data available for the introduced biological process. Check that the biological process id is correct or if you have introduced the taxon correctly.")
     
    def test_prot2cc(self):
        expected=[{'cc_id': 'GO:0005634',
  'cc_label': 'nucleus',
  'relation_label': 'O15405--GO:0005634',
  'database': 'goa/',
  'articles': 'pubmed/21873635'}]
        self.assertEqual(prot2cc("TOX3_HUMAN"),expected)
        self.assertEqual(prot2cc("WORLD"),"No data available for the introduced protein or you may have introduced an instance that is not a protein. Check your data type with type_data function.")
    
    def test_cc2prot(self):
        expected_1=[{'protein_name': 'PKD1_HUMAN', 'relation_label': 'P98161--GO:0034703', 'database': 'goa/', 'articles': 'pubmed/30093605'}, {'protein_name': 'PKD2_HUMAN', 'relation_label': 'Q13563--GO:0034703', 'database': 'goa/', 'articles': 'pubmed/30093605'}, {'protein_name': 'TRPC1_HUMAN', 'relation_label': 'P48995--GO:0034703', 'database': 'goa/', 'articles': 'pubmed/21873635'}, {'protein_name': 'TRPC3_HUMAN', 'relation_label': 'Q13507--GO:0034703', 'database': 'goa/', 'articles': 'pubmed/21873635'}, {'protein_name': 'TRPC4_HUMAN', 'relation_label': 'Q9UBN4--GO:0034703', 'database': 'goa/', 'articles': 'pubmed/21873635'}, {'protein_name': 'TRPC5_HUMAN', 'relation_label': 'Q9UL62--GO:0034703', 'database': 'goa/', 'articles': 'pubmed/21873635'}, {'protein_name': 'TRPC6_HUMAN', 'relation_label': 'Q9Y210--GO:0034703', 'database': 'goa/', 'articles': 'pubmed/21873635'}, {'protein_name': 'TRPC7_HUMAN', 'relation_label': 'Q9HCX4--GO:0034703', 'database': 'goa/', 'articles': 'pubmed/21873635'}, {'protein_name': 'UNC80_HUMAN', 'relation_label': 'Q8N2C7--GO:0034703', 'database': 'goa/', 'articles': 'pubmed/21873635'}]
        expected_2=[{'protein_name': 'CNGA1_HUMAN', 'relation_label': 'P29973--GO:0017071', 'database': 'goa/', 'articles': 'pubmed/21873635'}, {'protein_name': 'CNGA2_HUMAN', 'relation_label': 'Q16280--GO:0017071', 'database': 'goa/', 'articles': 'pubmed/21873635'}, {'protein_name': 'CNGA3_HUMAN', 'relation_label': 'Q16281--GO:0017071', 'database': 'goa/', 'articles': 'pubmed/21873635'}, {'protein_name': 'CNGA4_HUMAN', 'relation_label': 'Q8IV77--GO:0017071', 'database': 'goa/', 'articles': 'pubmed/21873635'}, {'protein_name': 'CNGB1_HUMAN', 'relation_label': 'Q14028--GO:0017071', 'database': 'goa/', 'articles': 'pubmed/21873635'}, {'protein_name': 'CNGB3_HUMAN', 'relation_label': 'Q9NQW8--GO:0017071', 'database': 'goa/', 'articles': 'pubmed/21873635'}, {'protein_name': 'PKD1_HUMAN', 'relation_label': 'P98161--GO:0034703', 'database': 'goa/', 'articles': 'pubmed/30093605'}, {'protein_name': 'PKD2_HUMAN', 'relation_label': 'Q13563--GO:0034703', 'database': 'goa/', 'articles': 'pubmed/30093605'}, {'protein_name': 'TRPC1_HUMAN', 'relation_label': 'P48995--GO:0034703', 'database': 'goa/', 'articles': 'pubmed/21873635'}, {'protein_name': 'TRPC3_HUMAN', 'relation_label': 'Q13507--GO:0034703', 'database': 'goa/', 'articles': 'pubmed/21873635'}, {'protein_name': 'TRPC4_HUMAN', 'relation_label': 'Q9UBN4--GO:0034703', 'database': 'goa/', 'articles': 'pubmed/21873635'}, {'protein_name': 'TRPC5_HUMAN', 'relation_label': 'Q9UL62--GO:0034703', 'database': 'goa/', 'articles': 'pubmed/21873635'}, {'protein_name': 'TRPC6_HUMAN', 'relation_label': 'Q9Y210--GO:0034703', 'database': 'goa/', 'articles': 'pubmed/21873635'}, {'protein_name': 'TRPC7_HUMAN', 'relation_label': 'Q9HCX4--GO:0034703', 'database': 'goa/', 'articles': 'pubmed/21873635'}, {'protein_name': 'UNC80_HUMAN', 'relation_label': 'Q8N2C7--GO:0034703', 'database': 'goa/', 'articles': 'pubmed/21873635'}]

        
        self.assertEqual(cc2prot("GO:0034703","Homo sapiens"),expected_1)
        self.assertEqual(cc2prot("GO:0034703","9606"),expected_1)
        self.assertEqual(cc2prot("cation channel complex","Homo sapiens"),expected_2)
        self.assertEqual(cc2prot("cation channel complex","9606"),expected_2)
        self.assertEqual(cc2prot("WORLD","taxon"),"No data available for the introduced cellular component. Check that the cellular component id is correct or if you have introduced the taxon correctly.")
        
    def test_prot2mf(self):
        expected=[{'mf_id': 'GO:0003682',
  'mf_label': 'chromatin binding',
  'relation_label': 'O15405--GO:0003682',
  'database': 'goa/',
  'articles': 'pubmed/21172805'},
 {'mf_id': 'GO:0003713',
  'mf_label': 'transcription coactivator activity',
  'relation_label': 'O15405--GO:0003713',
  'database': 'goa/',
  'articles': 'pubmed/21172805'},
 {'mf_id': 'GO:0005515',
  'mf_label': 'protein binding',
  'relation_label': 'O15405--GO:0005515',
  'database': 'goa/',
  'articles': 'pubmed/21172805'},
 {'mf_id': 'GO:0031490',
  'mf_label': 'chromatin DNA binding',
  'relation_label': 'O15405--GO:0031490',
  'database': 'goa/',
  'articles': 'pubmed/21873635'},
 {'mf_id': 'GO:0042803',
  'mf_label': 'protein homodimerization activity',
  'relation_label': 'O15405--GO:0042803',
  'database': 'goa/',
  'articles': 'pubmed/21172805'},
 {'mf_id': 'GO:0051219',
  'mf_label': 'phosphoprotein binding',
  'relation_label': 'O15405--GO:0051219',
  'database': 'goa/',
  'articles': 'pubmed/21172805'}]
        
        self.assertEqual(prot2mf("TOX3_HUMAN"),expected)
        self.assertEqual(prot2mf("WORLD"),"No data available for the introduced protein or you may have introduced an instance that is not a protein. Check your data type with type_data function.")
                         
    def test_mf2prot(self):
        expected=[{'protein_name': '1433B_HUMAN', 'relation_label': 'P31946--GO:0051219', 'database': 'goa/', 'articles': 'pubmed/10869435'}, {'protein_name': '1433E_HUMAN', 'relation_label': 'P62258--GO:0051219', 'database': 'goa/', 'articles': 'pubmed/10869435'}, {'protein_name': 'APTX_HUMAN', 'relation_label': 'Q7Z2E3--GO:0051219', 'database': 'goa/', 'articles': 'pubmed/20008512'}, {'protein_name': 'EPB41_HUMAN', 'relation_label': 'P11171--GO:0051219', 'database': 'goa/', 'articles': 'pubmed/20109190'}, {'protein_name': 'GLU2B_HUMAN', 'relation_label': 'P14314--GO:0051219', 'database': 'goa/', 'articles': 'pubmed/19801576'}, {'protein_name': 'LRP11_HUMAN', 'relation_label': 'Q86VZ4--GO:0051219', 'database': 'goa/', 'articles': 'pubmed/17620599'}, {'protein_name': 'MEN1_HUMAN', 'relation_label': 'O00255--GO:0051219', 'database': 'goa/', 'articles': 'pubmed/14992727'}, {'protein_name': 'MPRI_HUMAN', 'relation_label': 'P11717--GO:0051219', 'database': 'goa/', 'articles': 'pubmed/10900005'}, {'protein_name': 'MTOR_HUMAN', 'relation_label': 'P42345--GO:0051219', 'database': 'goa/', 'articles': 'pubmed/11853878'}, {'protein_name': 'PHF6_HUMAN', 'relation_label': 'Q8IWS0--GO:0051219', 'database': 'goa/', 'articles': 'pubmed/22720776'}, {'protein_name': 'PIHD1_HUMAN', 'relation_label': 'Q9NWS0--GO:0051219', 'database': 'goa/', 'articles': 'pubmed/20864032'}, {'protein_name': 'PIN1_HUMAN', 'relation_label': 'Q13526--GO:0051219', 'database': 'goa/', 'articles': 'pubmed/23362255'}, {'protein_name': 'PKD2_HUMAN', 'relation_label': 'Q13563--GO:0051219', 'database': 'goa/', 'articles': 'pubmed/19801576'}, {'protein_name': 'RB_HUMAN', 'relation_label': 'P06400--GO:0051219', 'database': 'goa/', 'articles': 'pubmed/16360038'}, {'protein_name': 'RMP_HUMAN', 'relation_label': 'O94763--GO:0051219', 'database': 'goa/', 'articles': 'pubmed/20864032'}, {'protein_name': 'RRAGA_HUMAN', 'relation_label': 'Q7L523--GO:0051219', 'database': 'goa/', 'articles': 'pubmed/8995684'}, {'protein_name': 'SRC_HUMAN', 'relation_label': 'P12931--GO:0051219', 'database': 'goa/', 'articles': 'pubmed/16441665'}, {'protein_name': 'SYUA_HUMAN', 'relation_label': 'P37840--GO:0051219', 'database': 'goa/', 'articles': 'pubmed/21127069'}, {'protein_name': 'TBK1_HUMAN', 'relation_label': 'Q9UHD2--GO:0051219', 'database': 'goa/', 'articles': 'pubmed/14530355'}, {'protein_name': 'TBL2_HUMAN', 'relation_label': 'Q9Y4P3--GO:0051219', 'database': 'goa/', 'articles': 'pubmed/25393282'}, {'protein_name': 'TOX3_HUMAN', 'relation_label': 'O15405--GO:0051219', 'database': 'goa/', 'articles': 'pubmed/21172805'}, {'protein_name': 'TPA_HUMAN', 'relation_label': 'P00750--GO:0051219', 'database': 'goa/', 'articles': 'pubmed/8186264'}, {'protein_name': 'TR150_HUMAN', 'relation_label': 'Q9Y2W1--GO:0051219', 'database': 'goa/', 'articles': 'pubmed/20932480'}, {'protein_name': 'TRI18_HUMAN', 'relation_label': 'O15344--GO:0051219', 'database': 'goa/', 'articles': 'pubmed/11806752'}, {'protein_name': 'TRIM1_HUMAN', 'relation_label': 'Q9UJV3--GO:0051219', 'database': 'goa/', 'articles': 'pubmed/11806752'}, {'protein_name': 'TRPV1_HUMAN', 'relation_label': 'Q8NER1--GO:0051219', 'database': 'goa/', 'articles': 'pubmed/19801576'}] 
        
        self.assertEqual(mf2prot("GO:0051219","Homo sapiens"),expected)
        self.assertEqual(mf2prot("GO:0051219","9606"),expected)
        self.assertEqual(mf2prot("phosphoprotein binding","Homo sapiens"),expected)
        self.assertEqual(mf2prot("phosphoprotein binding","9606"),expected)
        self.assertEqual(mf2prot("WORLD","taxon"),"No data available for the introduced molecular function. Check that the molecular function id is correct or if you have introduced the taxon correctly.")

    def test_gene2crm(self):
        expected=[{'crm_name': 'crm/CRMHS00000140196',
  'database': 'http://acgt.cs.tau.ac.il/focs/; http://bioinfo.vanderbilt.edu/AE/HACER; http://enhanceratlas.net/scenhancer/; http://www.enhanceratlas.org/indexv2.php; https://fantom.gsc.riken.jp/5/; https://genome.ucsc.edu/cgi-bin/hgTrackUi?db=hg38&g=geneHancer',
  'articles': 'pubmed/24670763; pubmed/28605766; pubmed/29716618; pubmed/30247654; pubmed/31740966; pubmed/34761274'},
 {'crm_name': 'crm/CRMHS00000140197',
  'database': 'http://acgt.cs.tau.ac.il/focs/; http://bioinfo.vanderbilt.edu/AE/HACER; http://enhanceratlas.net/scenhancer/; http://www.enhanceratlas.org/indexv2.php; https://fantom.gsc.riken.jp/5/; https://genome.ucsc.edu/cgi-bin/hgTrackUi?db=hg38&g=geneHancer',
  'articles': 'pubmed/24670763; pubmed/28605766; pubmed/29716618; pubmed/30247654; pubmed/31740966; pubmed/34761274'},
 {'crm_name': 'crm/CRMHS00005432070',
  'database': 'http://acgt.cs.tau.ac.il/focs/; http://bioinfo.vanderbilt.edu/AE/HACER; http://enhanceratlas.net/scenhancer/; http://www.enhanceratlas.org/indexv2.php; https://fantom.gsc.riken.jp/5/; https://genome.ucsc.edu/cgi-bin/hgTrackUi?db=hg38&g=geneHancer',
  'articles': 'pubmed/24670763; pubmed/28605766; pubmed/29716618; pubmed/30247654; pubmed/31740966; pubmed/34761274'},
 {'crm_name': 'crm/CRMHS00005432071',
  'database': 'http://acgt.cs.tau.ac.il/focs/; http://bioinfo.vanderbilt.edu/AE/HACER; http://enhanceratlas.net/scenhancer/; http://www.enhanceratlas.org/indexv2.php; https://fantom.gsc.riken.jp/5/; https://genome.ucsc.edu/cgi-bin/hgTrackUi?db=hg38&g=geneHancer',
  'articles': 'pubmed/24670763; pubmed/28605766; pubmed/29716618; pubmed/30247654; pubmed/31740966; pubmed/34761274'},
 {'crm_name': 'crm/CRMHS00007355907',
  'database': 'http://acgt.cs.tau.ac.il/focs/; http://bioinfo.vanderbilt.edu/AE/HACER; http://enhanceratlas.net/scenhancer/; http://www.enhanceratlas.org/indexv2.php; https://fantom.gsc.riken.jp/5/; https://genome.ucsc.edu/cgi-bin/hgTrackUi?db=hg38&g=geneHancer',
  'articles': 'pubmed/24670763; pubmed/28605766; pubmed/29716618; pubmed/30247654; pubmed/31740966; pubmed/34761274'},
 {'crm_name': 'crm/CRMHS00007376453',
  'database': 'http://acgt.cs.tau.ac.il/focs/; http://bioinfo.vanderbilt.edu/AE/HACER; http://enhanceratlas.net/scenhancer/; http://www.enhanceratlas.org/indexv2.php; https://fantom.gsc.riken.jp/5/; https://genome.ucsc.edu/cgi-bin/hgTrackUi?db=hg38&g=geneHancer',
  'articles': 'pubmed/24670763; pubmed/28605766; pubmed/29716618; pubmed/30247654; pubmed/31740966; pubmed/34761274'},
 {'crm_name': 'crm/CRMHS00007376454',
  'database': 'http://acgt.cs.tau.ac.il/focs/; http://bioinfo.vanderbilt.edu/AE/HACER; http://enhanceratlas.net/scenhancer/; http://www.enhanceratlas.org/indexv2.php; https://fantom.gsc.riken.jp/5/; https://genome.ucsc.edu/cgi-bin/hgTrackUi?db=hg38&g=geneHancer',
  'articles': 'pubmed/24670763; pubmed/28605766; pubmed/29716618; pubmed/30247654; pubmed/31740966; pubmed/34761274'},
 {'crm_name': 'crm/CRMHS00007376455',
  'database': 'http://acgt.cs.tau.ac.il/focs/; http://bioinfo.vanderbilt.edu/AE/HACER; http://enhanceratlas.net/scenhancer/; http://www.enhanceratlas.org/indexv2.php; https://fantom.gsc.riken.jp/5/; https://genome.ucsc.edu/cgi-bin/hgTrackUi?db=hg38&g=geneHancer',
  'articles': 'pubmed/24670763; pubmed/28605766; pubmed/29716618; pubmed/30247654; pubmed/31740966; pubmed/34761274'},
 {'crm_name': 'crm/CRMHS00007376456',
  'database': 'http://acgt.cs.tau.ac.il/focs/; http://bioinfo.vanderbilt.edu/AE/HACER; http://enhanceratlas.net/scenhancer/; http://www.enhanceratlas.org/indexv2.php; https://fantom.gsc.riken.jp/5/; https://genome.ucsc.edu/cgi-bin/hgTrackUi?db=hg38&g=geneHancer',
  'articles': 'pubmed/24670763; pubmed/28605766; pubmed/29716618; pubmed/30247654; pubmed/31740966; pubmed/34761274'},
 {'crm_name': 'crm/CRMHS00011073603',
  'database': 'http://acgt.cs.tau.ac.il/focs/; http://bioinfo.vanderbilt.edu/AE/HACER; http://enhanceratlas.net/scenhancer/; http://www.enhanceratlas.org/indexv2.php; https://fantom.gsc.riken.jp/5/; https://genome.ucsc.edu/cgi-bin/hgTrackUi?db=hg38&g=geneHancer',
  'articles': 'pubmed/24670763; pubmed/28605766; pubmed/29716618; pubmed/30247654; pubmed/31740966; pubmed/34761274'},
 {'crm_name': 'crm/CRMHS00011073608',
  'database': 'http://acgt.cs.tau.ac.il/focs/; http://bioinfo.vanderbilt.edu/AE/HACER; http://enhanceratlas.net/scenhancer/; http://www.enhanceratlas.org/indexv2.php; https://fantom.gsc.riken.jp/5/; https://genome.ucsc.edu/cgi-bin/hgTrackUi?db=hg38&g=geneHancer',
  'articles': 'pubmed/24670763; pubmed/28605766; pubmed/29716618; pubmed/30247654; pubmed/31740966; pubmed/34761274'},
 {'crm_name': 'crm/CRMHS00011073626',
  'database': 'http://acgt.cs.tau.ac.il/focs/; http://bioinfo.vanderbilt.edu/AE/HACER; http://enhanceratlas.net/scenhancer/; http://www.enhanceratlas.org/indexv2.php; https://fantom.gsc.riken.jp/5/; https://genome.ucsc.edu/cgi-bin/hgTrackUi?db=hg38&g=geneHancer',
  'articles': 'pubmed/24670763; pubmed/28605766; pubmed/29716618; pubmed/30247654; pubmed/31740966; pubmed/34761274'},
 {'crm_name': 'crm/CRMHS00011074117',
  'database': 'http://acgt.cs.tau.ac.il/focs/; http://bioinfo.vanderbilt.edu/AE/HACER; http://enhanceratlas.net/scenhancer/; http://www.enhanceratlas.org/indexv2.php; https://fantom.gsc.riken.jp/5/; https://genome.ucsc.edu/cgi-bin/hgTrackUi?db=hg38&g=geneHancer',
  'articles': 'pubmed/24670763; pubmed/28605766; pubmed/29716618; pubmed/30247654; pubmed/31740966; pubmed/34761274'},
 {'crm_name': 'crm/CRMHS00011074125',
  'database': 'http://acgt.cs.tau.ac.il/focs/; http://bioinfo.vanderbilt.edu/AE/HACER; http://enhanceratlas.net/scenhancer/; http://www.enhanceratlas.org/indexv2.php; https://fantom.gsc.riken.jp/5/; https://genome.ucsc.edu/cgi-bin/hgTrackUi?db=hg38&g=geneHancer',
  'articles': 'pubmed/24670763; pubmed/28605766; pubmed/29716618; pubmed/30247654; pubmed/31740966; pubmed/34761274'},
 {'crm_name': 'crm/CRMHS00011074127',
  'database': 'http://acgt.cs.tau.ac.il/focs/; http://bioinfo.vanderbilt.edu/AE/HACER; http://enhanceratlas.net/scenhancer/; http://www.enhanceratlas.org/indexv2.php; https://fantom.gsc.riken.jp/5/; https://genome.ucsc.edu/cgi-bin/hgTrackUi?db=hg38&g=geneHancer',
  'articles': 'pubmed/24670763; pubmed/28605766; pubmed/29716618; pubmed/30247654; pubmed/31740966; pubmed/34761274'},
 {'crm_name': 'crm/CRMHS00027474404',
  'database': 'http://acgt.cs.tau.ac.il/focs/; http://bioinfo.vanderbilt.edu/AE/HACER; http://enhanceratlas.net/scenhancer/; http://www.enhanceratlas.org/indexv2.php; https://fantom.gsc.riken.jp/5/; https://genome.ucsc.edu/cgi-bin/hgTrackUi?db=hg38&g=geneHancer',
  'articles': 'pubmed/24670763; pubmed/28605766; pubmed/29716618; pubmed/30247654; pubmed/31740966; pubmed/34761274'},
 {'crm_name': 'crm/CRMHS00027474405',
  'database': 'http://acgt.cs.tau.ac.il/focs/; http://bioinfo.vanderbilt.edu/AE/HACER; http://enhanceratlas.net/scenhancer/; http://www.enhanceratlas.org/indexv2.php; https://fantom.gsc.riken.jp/5/; https://genome.ucsc.edu/cgi-bin/hgTrackUi?db=hg38&g=geneHancer',
  'articles': 'pubmed/24670763; pubmed/28605766; pubmed/29716618; pubmed/30247654; pubmed/31740966; pubmed/34761274'},
 {'crm_name': 'crm/CRMHS00027474406',
  'database': 'http://acgt.cs.tau.ac.il/focs/; http://bioinfo.vanderbilt.edu/AE/HACER; http://enhanceratlas.net/scenhancer/; http://www.enhanceratlas.org/indexv2.php; https://fantom.gsc.riken.jp/5/; https://genome.ucsc.edu/cgi-bin/hgTrackUi?db=hg38&g=geneHancer',
  'articles': 'pubmed/24670763; pubmed/28605766; pubmed/29716618; pubmed/30247654; pubmed/31740966; pubmed/34761274'},
 {'crm_name': 'crm/CRMHS00027484292',
  'database': 'http://acgt.cs.tau.ac.il/focs/; http://bioinfo.vanderbilt.edu/AE/HACER; http://enhanceratlas.net/scenhancer/; http://www.enhanceratlas.org/indexv2.php; https://fantom.gsc.riken.jp/5/; https://genome.ucsc.edu/cgi-bin/hgTrackUi?db=hg38&g=geneHancer',
  'articles': 'pubmed/24670763; pubmed/28605766; pubmed/29716618; pubmed/30247654; pubmed/31740966; pubmed/34761274'},
 {'crm_name': 'crm/CRMHS00027535561',
  'database': 'http://acgt.cs.tau.ac.il/focs/; http://bioinfo.vanderbilt.edu/AE/HACER; http://enhanceratlas.net/scenhancer/; http://www.enhanceratlas.org/indexv2.php; https://fantom.gsc.riken.jp/5/; https://genome.ucsc.edu/cgi-bin/hgTrackUi?db=hg38&g=geneHancer',
  'articles': 'pubmed/24670763; pubmed/28605766; pubmed/29716618; pubmed/30247654; pubmed/31740966; pubmed/34761274'},
 {'crm_name': 'crm/CRMHS00027535562',
  'database': 'http://acgt.cs.tau.ac.il/focs/; http://bioinfo.vanderbilt.edu/AE/HACER; http://enhanceratlas.net/scenhancer/; http://www.enhanceratlas.org/indexv2.php; https://fantom.gsc.riken.jp/5/; https://genome.ucsc.edu/cgi-bin/hgTrackUi?db=hg38&g=geneHancer',
  'articles': 'pubmed/24670763; pubmed/28605766; pubmed/29716618; pubmed/30247654; pubmed/31740966; pubmed/34761274'},
 {'crm_name': 'crm/CRMHS00029020228',
  'database': 'http://acgt.cs.tau.ac.il/focs/; http://bioinfo.vanderbilt.edu/AE/HACER; http://enhanceratlas.net/scenhancer/; http://www.enhanceratlas.org/indexv2.php; https://fantom.gsc.riken.jp/5/; https://genome.ucsc.edu/cgi-bin/hgTrackUi?db=hg38&g=geneHancer',
  'articles': 'pubmed/24670763; pubmed/28605766; pubmed/29716618; pubmed/30247654; pubmed/31740966; pubmed/34761274'},
 {'crm_name': 'crm/CRMHS00029020231',
  'database': 'http://acgt.cs.tau.ac.il/focs/; http://bioinfo.vanderbilt.edu/AE/HACER; http://enhanceratlas.net/scenhancer/; http://www.enhanceratlas.org/indexv2.php; https://fantom.gsc.riken.jp/5/; https://genome.ucsc.edu/cgi-bin/hgTrackUi?db=hg38&g=geneHancer',
  'articles': 'pubmed/24670763; pubmed/28605766; pubmed/29716618; pubmed/30247654; pubmed/31740966; pubmed/34761274'},
 {'crm_name': 'crm/CRMHS00029020235',
  'database': 'http://acgt.cs.tau.ac.il/focs/; http://bioinfo.vanderbilt.edu/AE/HACER; http://enhanceratlas.net/scenhancer/; http://www.enhanceratlas.org/indexv2.php; https://fantom.gsc.riken.jp/5/; https://genome.ucsc.edu/cgi-bin/hgTrackUi?db=hg38&g=geneHancer',
  'articles': 'pubmed/24670763; pubmed/28605766; pubmed/29716618; pubmed/30247654; pubmed/31740966; pubmed/34761274'},
 {'crm_name': 'crm/CRMHS00029020242',
  'database': 'http://acgt.cs.tau.ac.il/focs/; http://bioinfo.vanderbilt.edu/AE/HACER; http://enhanceratlas.net/scenhancer/; http://www.enhanceratlas.org/indexv2.php; https://fantom.gsc.riken.jp/5/; https://genome.ucsc.edu/cgi-bin/hgTrackUi?db=hg38&g=geneHancer',
  'articles': 'pubmed/24670763; pubmed/28605766; pubmed/29716618; pubmed/30247654; pubmed/31740966; pubmed/34761274'}]
        self.assertEqual(gene2crm("RPS4Y1"),expected)
        self.assertEqual(gene2crm("WORLD"),"No data available for the introduced gene or you may have introduced an instance that is not a gene. Check your data type with type_data function.")
        
    def test_crm2gene(self):
        expected=[{'gene_name': 'C9orf78',
  'database': 'http://bioinfo.vanderbilt.edu/AE/HACER; http://yiplab.cse.cuhk.edu.hk/jeme/; https://fantom.gsc.riken.jp/5/; https://webs.iiitd.edu.in/raghava/cancerend/',
  'articles': 'pubmed/24670763; pubmed/28869592; pubmed/30247654; pubmed/32360910'},
 {'gene_name': 'CRAT',
  'database': 'http://bioinfo.vanderbilt.edu/AE/HACER; http://yiplab.cse.cuhk.edu.hk/jeme/; https://fantom.gsc.riken.jp/5/; https://webs.iiitd.edu.in/raghava/cancerend/',
  'articles': 'pubmed/24670763; pubmed/28869592; pubmed/30247654; pubmed/32360910'},
 {'gene_name': 'DOLPP1',
  'database': 'http://bioinfo.vanderbilt.edu/AE/HACER; http://yiplab.cse.cuhk.edu.hk/jeme/; https://fantom.gsc.riken.jp/5/; https://webs.iiitd.edu.in/raghava/cancerend/',
  'articles': 'pubmed/24670763; pubmed/28869592; pubmed/30247654; pubmed/32360910'},
 {'gene_name': 'IER5L',
  'database': 'http://bioinfo.vanderbilt.edu/AE/HACER; http://yiplab.cse.cuhk.edu.hk/jeme/; https://fantom.gsc.riken.jp/5/; https://webs.iiitd.edu.in/raghava/cancerend/',
  'articles': 'pubmed/24670763; pubmed/28869592; pubmed/30247654; pubmed/32360910'},
 {'gene_name': 'NTMT1',
  'database': 'http://bioinfo.vanderbilt.edu/AE/HACER; http://yiplab.cse.cuhk.edu.hk/jeme/; https://fantom.gsc.riken.jp/5/; https://webs.iiitd.edu.in/raghava/cancerend/',
  'articles': 'pubmed/24670763; pubmed/28869592; pubmed/30247654; pubmed/32360910'},
 {'gene_name': 'NTNG2',
  'database': 'http://bioinfo.vanderbilt.edu/AE/HACER; http://yiplab.cse.cuhk.edu.hk/jeme/; https://fantom.gsc.riken.jp/5/; https://webs.iiitd.edu.in/raghava/cancerend/',
  'articles': 'pubmed/24670763; pubmed/28869592; pubmed/30247654; pubmed/32360910'},
 {'gene_name': 'PTPA',
  'database': 'http://bioinfo.vanderbilt.edu/AE/HACER; http://yiplab.cse.cuhk.edu.hk/jeme/; https://fantom.gsc.riken.jp/5/; https://webs.iiitd.edu.in/raghava/cancerend/',
  'articles': 'pubmed/24670763; pubmed/28869592; pubmed/30247654; pubmed/32360910'}]
            
        self.assertEqual(crm2gene("crm/CRMHS00000137026"),expected)
        self.assertEqual(crm2gene("WORLD"), "No data available for the introduced crm or you may have introduced an instance that is not a crm. Check your data type with type_data function.")
    
    
    def test_tfac2crm(self):
        expected=[{'crm_name': 'crm/CRMHS00000005333',
  'database': 'http://www.licpathway.net/ENdb/',
  'articles': 'pubmed/23273978',
  'evidence': 'http://www.licpathway.net/ENdb/search/Detail.php?Species=Human&Enhancer_id=E_01_119',
  'biological_samples': 'BTO_0000093; CLO_0007606; CL_0002327; UBERON_0000310'},
 {'crm_name': 'crm/CRMHS00000005334',
  'database': 'http://www.licpathway.net/ENdb/',
  'articles': 'pubmed/26754925',
  'evidence': 'http://www.licpathway.net/ENdb/search/Detail.php?Species=Human&Enhancer_id=E_01_239',
  'biological_samples': 'BTO_0001109; CLO_0003665; CL_0011108; UBERON_0001155'},
 {'crm_name': 'crm/CRMHS00000005630',
  'database': 'http://www.licpathway.net/ENdb/',
  'articles': 'pubmed/20061391',
  'evidence': 'http://www.licpathway.net/ENdb/search/Detail.php?Species=Human&Enhancer_id=E_01_031',
  'biological_samples': 'BTO_0001061; CLO_0008395; CL_0002231; UBERON_0002367'},
 {'crm_name': 'crm/CRMHS00000005658',
  'database': 'http://www.licpathway.net/ENdb/',
  'articles': 'pubmed/26751173',
  'evidence': 'http://www.licpathway.net/ENdb/search/Detail.php?Species=Human&Enhancer_id=E_01_005',
  'biological_samples': 'BTO_0003807; CLO_0001980; CL_1001608; UBERON_0001332'},
 {'crm_name': 'crm/CRMHS00000005659',
  'database': 'http://www.licpathway.net/ENdb/',
  'articles': 'pubmed/24797517',
  'evidence': 'http://www.licpathway.net/ENdb/search/Detail.php?Species=Human&Enhancer_id=E_01_172',
  'biological_samples': 'BTO_0003807; CLO_0001980; CL_1001608; UBERON_0001332'},
 {'crm_name': 'crm/CRMHS00000005660',
  'database': 'http://www.licpathway.net/ENdb/',
  'articles': 'pubmed/26751173',
  'evidence': 'http://www.licpathway.net/ENdb/search/Detail.php?Species=Human&Enhancer_id=E_01_006',
  'biological_samples': 'BTO_0003807; CLO_0001980; CL_1001608; UBERON_0001332'},
 {'crm_name': 'crm/CRMHS00000005661',
  'database': 'http://www.licpathway.net/ENdb/',
  'articles': 'pubmed/26745862',
  'evidence': 'http://www.licpathway.net/ENdb/search/Detail.php?Species=Human&Enhancer_id=E_01_383',
  'biological_samples': 'BTO_0000018; BTO_0000093; BTO_0000567; BTO_0002181; CLO_0001601; CLO_0003684; CLO_0007606; CLO_0037372; CL_0000082; CL_0002327; CL_0002518; CL_0002535; UBERON_0000002; UBERON_0000310; UBERON_0002048; UBERON_0002113'},
 {'crm_name': 'crm/CRMHS00000005662',
  'database': 'http://www.licpathway.net/ENdb/',
  'articles': 'pubmed/26745862',
  'evidence': 'http://www.licpathway.net/ENdb/search/Detail.php?Species=Human&Enhancer_id=E_01_384',
  'biological_samples': 'BTO_0000018; BTO_0000093; BTO_0000567; BTO_0002181; CLO_0001601; CLO_0003684; CLO_0007606; CLO_0037372; CL_0000082; CL_0002327; CL_0002518; CL_0002535; UBERON_0000002; UBERON_0000310; UBERON_0002048; UBERON_0002113'},
 {'crm_name': 'crm/CRMHS00000005714',
  'database': 'http://www.licpathway.net/ENdb/',
  'articles': 'pubmed/24797517',
  'evidence': 'http://www.licpathway.net/ENdb/search/Detail.php?Species=Human&Enhancer_id=E_01_173',
  'biological_samples': 'BTO_0003807; CLO_0001980; CL_1001608; UBERON_0001332'},
 {'crm_name': 'crm/CRMHS00000005725',
  'database': 'http://www.licpathway.net/ENdb/',
  'articles': 'pubmed/23273978',
  'evidence': 'http://www.licpathway.net/ENdb/search/Detail.php?Species=Human&Enhancer_id=E_01_120',
  'biological_samples': 'BTO_0000093; CLO_0007606; CL_0002327; UBERON_0000310'},
 {'crm_name': 'crm/CRMHS00000005739',
  'database': 'http://www.licpathway.net/ENdb/',
  'articles': 'pubmed/26776159',
  'evidence': 'http://www.licpathway.net/ENdb/search/Detail.php?Species=Human&Enhancer_id=E_01_406',
  'biological_samples': 'BTO_0003807; CLO_0001980; CL_1001608; UBERON_0001332'}]
        
        self.assertEqual(tfac2crm("P53_HUMAN"),expected)
        self.assertEqual(tfac2crm("WORLD"),"No data available for the introduced transcription factor or you may have introduced an instance that is not a transcirption factor. Check your data type with type_data function")
    
    def test_crm2tfac(self):
        expected=[{'tfac_name': 'RAD21_HUMAN',
  'database': 'http://lcbb.swjtu.edu.cn/EnhFFL/',
  'articles': 'pubmed/35694152',
  'evidence': 'http://lcbb.swjtu.edu.cn/EnhFFL/details/?term=enH58066&subtype=enhancer&species=human',
  'biological_samples': 'BTO_0000887; CL_0000187; UBERON_0005090'},
 {'tfac_name': 'SRF_HUMAN',
  'database': 'http://lcbb.swjtu.edu.cn/EnhFFL/',
  'articles': 'pubmed/35694152',
  'evidence': 'http://lcbb.swjtu.edu.cn/EnhFFL/details/?term=enH58066&subtype=enhancer&species=human',
  'biological_samples': 'BTO_0000887; CL_0000187; UBERON_0005090'},
 {'tfac_name': 'TAF1_HUMAN',
  'database': 'http://lcbb.swjtu.edu.cn/EnhFFL/',
  'articles': 'pubmed/35694152',
  'evidence': 'http://lcbb.swjtu.edu.cn/EnhFFL/details/?term=enH58066&subtype=enhancer&species=human',
  'biological_samples': 'BTO_0000887; CL_0000187; UBERON_0005090'},
 {'tfac_name': 'RPB1_HUMAN',
  'database': 'http://lcbb.swjtu.edu.cn/EnhFFL/',
  'articles': 'pubmed/35694152',
  'evidence': 'http://lcbb.swjtu.edu.cn/EnhFFL/details/?term=enH58066&subtype=enhancer&species=human',
  'biological_samples': 'BTO_0000887; CL_0000187; UBERON_0005090'},
 {'tfac_name': 'NR2C2_HUMAN',
  'database': 'http://lcbb.swjtu.edu.cn/EnhFFL/',
  'articles': 'pubmed/35694152',
  'evidence': 'http://lcbb.swjtu.edu.cn/EnhFFL/details/?term=enH58066&subtype=enhancer&species=human',
  'biological_samples': 'BTO_0000887; CL_0000187; UBERON_0005090'},
 {'tfac_name': 'CTCF_HUMAN',
  'database': 'http://lcbb.swjtu.edu.cn/EnhFFL/',
  'articles': 'pubmed/35694152',
  'evidence': 'http://lcbb.swjtu.edu.cn/EnhFFL/details/?term=enH58066&subtype=enhancer&species=human',
  'biological_samples': 'BTO_0000887; CL_0000187; UBERON_0005090'},
 {'tfac_name': 'MAX_HUMAN',
  'database': 'http://lcbb.swjtu.edu.cn/EnhFFL/',
  'articles': 'pubmed/35694152',
  'evidence': 'http://lcbb.swjtu.edu.cn/EnhFFL/details/?term=enH58066&subtype=enhancer&species=human',
  'biological_samples': 'BTO_0000887; CL_0000187; UBERON_0005090'},
 {'tfac_name': 'REST_HUMAN',
  'database': 'http://lcbb.swjtu.edu.cn/EnhFFL/',
  'articles': 'pubmed/35694152',
  'evidence': 'http://lcbb.swjtu.edu.cn/EnhFFL/details/?term=enH58066&subtype=enhancer&species=human',
  'biological_samples': 'BTO_0000887; CL_0000187; UBERON_0005090'},
 {'tfac_name': 'RUNX3_HUMAN',
  'database': 'http://lcbb.swjtu.edu.cn/EnhFFL/',
  'articles': 'pubmed/35694152',
  'evidence': 'http://lcbb.swjtu.edu.cn/EnhFFL/details/?term=enH58066&subtype=enhancer&species=human',
  'biological_samples': 'BTO_0000887; CL_0000187; UBERON_0005090'},
 {'tfac_name': 'PHF8_HUMAN',
  'database': 'http://lcbb.swjtu.edu.cn/EnhFFL/',
  'articles': 'pubmed/35694152',
  'evidence': 'http://lcbb.swjtu.edu.cn/EnhFFL/details/?term=enH58066&subtype=enhancer&species=human',
  'biological_samples': 'BTO_0000887; CL_0000187; UBERON_0005090'},
 {'tfac_name': 'SMC3_HUMAN',
  'database': 'http://lcbb.swjtu.edu.cn/EnhFFL/',
  'articles': 'pubmed/35694152',
  'evidence': 'http://lcbb.swjtu.edu.cn/EnhFFL/details/?term=enH58066&subtype=enhancer&species=human',
  'biological_samples': 'BTO_0000887; CL_0000187; UBERON_0005090'}]
        
        self.assertEqual(crm2tfac("crm/CRMHS00000007832"),expected)
        self.assertEqual(crm2tfac("WORLD"),"No data available for the introduced crm or you may have introduced an instance that is not a crm. Check your data type with type_data function.")
        
    def test_crm2phen(self):
        expected=[{'phen_id': 'OMIM/181500',
  'database': 'http://biocc.hrbmu.edu.cn/DiseaseEnhancer/; http://health.tsinghua.edu.cn/jianglab/endisease/',
  'articles': 'pubmed/25453756'},
 {'phen_id': 'MESH/D012559',
  'database': 'http://biocc.hrbmu.edu.cn/DiseaseEnhancer/; http://health.tsinghua.edu.cn/jianglab/endisease/',
  'articles': 'pubmed/25453756'},
 {'phen_id': 'DOID/DOID_5419',
  'database': 'http://biocc.hrbmu.edu.cn/DiseaseEnhancer/; http://health.tsinghua.edu.cn/jianglab/endisease/',
  'articles': 'pubmed/25453756'}]
        self.assertEqual(crm2phen("crm/CRMHS00000005764"),expected)
        self.assertEqual(crm2phen("WORLD"),"No data available for the introduced crm or you may have introduced an instance that is not a crm. Check your data type with type_data function.")
        
    def test_phen2crm(self):
        expected=[{'crm_name': 'crm/CRMHS00000005764', 'database': 'http://biocc.hrbmu.edu.cn/DiseaseEnhancer/; http://health.tsinghua.edu.cn/jianglab/endisease/', 'articles': 'pubmed/25453756'}, {'crm_name': 'crm/CRMHS00000005770', 'database': 'http://biocc.hrbmu.edu.cn/DiseaseEnhancer/; http://health.tsinghua.edu.cn/jianglab/endisease/', 'articles': 'pubmed/25453756'}, {'crm_name': 'crm/CRMHS00000005771', 'database': 'http://biocc.hrbmu.edu.cn/DiseaseEnhancer/; http://health.tsinghua.edu.cn/jianglab/endisease/', 'articles': 'pubmed/25434007'}, {'crm_name': 'crm/CRMHS00000005773', 'database': 'http://biocc.hrbmu.edu.cn/DiseaseEnhancer/; http://health.tsinghua.edu.cn/jianglab/endisease/', 'articles': 'pubmed/25453756'}, {'crm_name': 'crm/CRMHS00000005816', 'database': 'http://biocc.hrbmu.edu.cn/DiseaseEnhancer/; http://health.tsinghua.edu.cn/jianglab/endisease/', 'articles': 'pubmed/25453756; pubmed/27276213'}, {'crm_name': 'crm/CRMHS00000005892', 'database': 'http://biocc.hrbmu.edu.cn/DiseaseEnhancer/; http://health.tsinghua.edu.cn/jianglab/endisease/', 'articles': 'pubmed/25453756'}, {'crm_name': 'crm/CRMHS00000005893', 'database': 'http://biocc.hrbmu.edu.cn/DiseaseEnhancer/; http://health.tsinghua.edu.cn/jianglab/endisease/', 'articles': 'pubmed/25453756'}, {'crm_name': 'crm/CRMHS00000005907', 'database': 'http://biocc.hrbmu.edu.cn/DiseaseEnhancer/; http://health.tsinghua.edu.cn/jianglab/endisease/', 'articles': 'pubmed/25453756'}, {'crm_name': 'crm/CRMHS00000005918', 'database': 'http://biocc.hrbmu.edu.cn/DiseaseEnhancer/; http://health.tsinghua.edu.cn/jianglab/endisease/', 'articles': 'pubmed/25453756'}, {'crm_name': 'crm/CRMHS00000005997', 'database': 'http://biocc.hrbmu.edu.cn/DiseaseEnhancer/; http://health.tsinghua.edu.cn/jianglab/endisease/', 'articles': 'pubmed/25453756'}, {'crm_name': 'crm/CRMHS00000005998', 'database': 'http://biocc.hrbmu.edu.cn/DiseaseEnhancer/; http://health.tsinghua.edu.cn/jianglab/endisease/', 'articles': 'pubmed/25453756'}, {'crm_name': 'crm/CRMHS00000005999', 'database': 'http://biocc.hrbmu.edu.cn/DiseaseEnhancer/; http://health.tsinghua.edu.cn/jianglab/endisease/', 'articles': 'pubmed/25453756'}, {'crm_name': 'crm/CRMHS00027685953', 'database': 'http://biocc.hrbmu.edu.cn/DiseaseEnhancer/', 'articles': 'pubmed/25910213'}, {'crm_name': 'crm/CRMHS00027685954', 'database': 'http://biocc.hrbmu.edu.cn/DiseaseEnhancer/', 'articles': 'pubmed/25910213'}, {'crm_name': 'crm/CRMHS00027685955', 'database': 'http://biocc.hrbmu.edu.cn/DiseaseEnhancer/', 'articles': 'pubmed/25910213'}, {'crm_name': 'crm/CRMHS00027685956', 'database': 'http://biocc.hrbmu.edu.cn/DiseaseEnhancer/', 'articles': 'pubmed/25910213'}, {'crm_name': 'crm/CRMHS00027685957', 'database': 'http://biocc.hrbmu.edu.cn/DiseaseEnhancer/', 'articles': 'pubmed/25910213'}]
        
        self.assertEqual(phen2crm("181500"),expected)
        self.assertEqual(phen2crm("SCHIZOPHRENIA"),expected)
        self.assertEqual(phen2crm("WORLD"),"No data available for the introduced phenotype or you may have introduced an instance that is not a phenotype. Check your data type with type_data function.")
        
    def test_tfac2gene(self):
        expected= tfac2gene("CREB1_HUMAN")
        self.assertEqual(tfac2gene("CREB1_HUMAN"),expected)
        self.assertEqual(tfac2gene("WORLD"),"No data available for the introduced transcription factor or you may have introduced an instance that is not a transcription factor. Check your data type with type_data function")
        
        
    def test_gene2tfac(self):
        expected= gene2tfac("TP53")
        self.assertEqual(gene2tfac("TP53"),expected)
        self.assertEqual(gene2tfac("WORLD"),"No data available for the introduced gene or you may have introduced an instance that is not a gene. Check your data type with type_data function.")
if __name__ == '__main__':
    unittest.main()