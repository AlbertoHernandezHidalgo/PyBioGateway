# test_script.py

from BioGatewayQuery import type_data, getGene_info, getProtein_info

# Llama a las funciones para asegurarte de que funcionan correctamente
# Asegúrate de tener algunos datos de prueba para pasar a las funciones
test_instance = "aaa"
gene = "TOX3"
taxon = "9606"
protein="TOX3_HUMAN"

print(type_data(test_instance))
print(getGene_info(gene, taxon))
print(getProtein_info(protein))
