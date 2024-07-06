from SPARQLWrapper import SPARQLWrapper, JSON


def data_processing(consulta): #Función para procesar datos
    # Endpoint SPARQL
    endpoint_sparql = "http://ssb4.nt.ntnu.no:23122/sparql"
# Inicializar SPARQLWrapper para la primera consulta
    sparql = SPARQLWrapper(endpoint_sparql)
    sparql.setQuery(consulta)
    sparql.setReturnFormat(JSON)
    
    # Realizar la primera consulta SPARQL para obtener información de las proteínas
    resultados = sparql.query().convert()
    
    # Procesar resultados de la primera consulta
    resultados_procesados = []
    for resultado in resultados['results']['bindings']:
        resultado_procesado = {}
        for variable in resultado.keys():
            valor = resultado[variable]['value']
            resultado_procesado[variable] = valor
        resultados_procesados.append(resultado_procesado)
    return resultados_procesados 

def translate_chr(chromosome):
    ncbi_chromosome_ids = {
    "chr-1": "NC_000001.11",
    "chr-2": "NC_000002.12",
    "chr-3": "NC_000003.12",
    "chr-4": "NC_000004.12",
    "chr-5": "NC_000005.10",
    "chr-6": "NC_000006.12",
    "chr-7": "NC_000007.14",
    "chr-8": "NC_000008.11",
    "chr-9": "NC_000009.12",
    "chr-10": "NC_000010.11",
    "chr-11": "NC_000011.10",
    "chr-12": "NC_000012.12",
    "chr-13": "NC_000013.11",
    "chr-14": "NC_000014.9",
    "chr-15": "NC_000015.10",
    "chr-16": "NC_000016.10",
    "chr-17": "NC_000017.11",
    "chr-18": "NC_000018.10",
    "chr-19": "NC_000019.10",
    "chr-20": "NC_000020.11",
    "chr-21": "NC_000021.9",
    "chr-22": "NC_000022.11",
    "chr-X": "NC_000023.11",
    "chr-Y": "NC_000024.10",
    "mitochondrial" : "NC_012920.1"
    }
    # Verificar si el cromosoma existe en el diccionario
    if chromosome in ncbi_chromosome_ids:
        return ncbi_chromosome_ids[chromosome]
    else:
        return "Identificador de cromosoma no válido."