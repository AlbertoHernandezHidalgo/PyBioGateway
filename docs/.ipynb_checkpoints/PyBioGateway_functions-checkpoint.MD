<a name="_px1h05vtlcww"></a>Funciones de PyBioGateway
#

|<a name="_m9hpiarbn6up"></a>**Ontología**|**Uri**|**Prefijo**|
| :- | :- | :- |
|**Simple Knowledge Organization System (SKOS)**|**http://www.w3.org/2004/02/skos/core#**|**skos**|
|**Resource Description Framework (RDF)**|**http://www.w3.org/1999/02/22-rdf-syntax-ns#**|**rdf**|
|**RDF Schema (RDFS)**|**http://www.w3.org/2000/01/rdf-schema#**|**rdfs**|
|**Semanticscience Integrated Ontology (SIO)**|**http://semanticscience.org/resource/**|**sio**|
|**Open Biomedical Ontologies (OBO)**|**http://purl.obolibrary.org/obo/**|**obo**|
|**Dublin core (DC)**|**http://purl.org/dc/terms/**|**dc**|
|**Schema (SCH)**|**http://schema.org/**|**sch**|
|**Open Biomedical Ontologies (OBO)**|**http://www.geneontology.org/formats/oboInOwl#**|**oboowl**|
# <a name="_48m7ysot854z"></a>**Tabla 1. Tabla con la información sobre la ontología y los prefijos usados en las consultas.**
# <a name="_9v9oum6b7e0l"></a>**Función type\_data(name):**
**Descripción**: Esta función sirve para consultar el tipo de entidad biológica a la que pertenece una entidad específica introducida por el usuario.

Esta función tiene como parámetro el nombre (prefLabel o altLabel) de la entidad biológica específica que queremos consultar en el grafo de conocimiento, y devuelve el tipo de entidad biológica a la que pertenece, es decir si es un gen, proteína, dominio asociado topológicamente (TAD), módulo cis regulador (CRM), proceso biológico, componente celular o función molecular.

**Parámetros:** 

**-“name”**: Nombre de la entidad biológica que el usuario quiere consultar. Siete tipos de entidades pueden consultarse: proteínas, genes, TADs, CRMs, procesos biológicos, funciones moleculares o componentes celulares. Los vocabularios empleados son los siguientes:

- Proteínas: Son válidos tanto el “entry name” de Uniprot como otros identificadores alternativos. Ejemplo: “INSR\_HUMAN”.
- Genes: gene symbol HGNC. Ejemplo: “INSR”
- TADs y CRMs: identificadores propios de BioGateway. Ejemplo: “crm/CRMHS00000003515”, “tad/TADHS00000020654”.
- Procesos biológicos, funciones moleculares o componentes celulares: Identificadores propios de Gene Ontology (GO). Ejemplo: “GO:0000206”

**Salida:** 

**-“bioentity\_type”**: Tipo de entidad biológica a la que pertenece el valor de entrada. Valores posibles:

- Proteína: Ejemplo salida, “protein” (prefLabel).
- Gen: Ejemplo salida, “gene” (prefLabel).
- TAD: Ejemplo salida, “topologically\_associated\_domain (tad)” (prefLabel).
- CRM: Ejemplo salida, “cis\_regulatory\_module (crm)” (prefLabel).
- Proceso biológico: Ejemplo salida, “biological\_process” (hasOBONamespace).
- Componente celular: Ejemplo salida, “cellular\_component” (hasOBONamespace).
- Función molecular: Ejemplo salida, “molecular\_function” (hasOBONamespace).

**Ejemplo de ejecución:**

Entrada:

type\_data(“INSR\_HUMAN”)

Salida: 

“protein”

Entrada con nombre alternativo de la misma proteína:

type\_data("P06213")

Salida:

“protein”

**Tabla resumen:**

|Variable|Rol|Tipo|Descripción|Propiedad de la Ontología|
| :- | :- | :- | :- | :- |
|**“name”**|**entrada**|**string** |**Nombre de la entidad biológica**|<p>**skos:prefLabel o** </p><p>**skos:altLabel**</p>|
|**“bioentity\_type”**|**salida**|**string**|**Tipo de entidad biológica**|**rdfs:subClassof obo:hasOBONamespace**|


# <a name="_aejpdc2ab8ha"></a>**Función: getGene\_info(gene, taxon)**

**Descripción:** Función que proporciona la información asociada al gen que se desea consultar, disponible en el grafo de conocimiento:  **http://rdf.biogateway.eu/graph/gene.**

Esta función tiene dos parámetros: el nombre del gen que queremos consultar y el taxón.

**Parámetros:** 

**-“gene”.** Insertamos el gen en formato gene symbol (propiedad: prefLabel). Ejemplo: “BRCA1”

**-”taxon”.** Insertamos o bien el número del taxon o bien el nombre del organismo (propiedad: label). Ejemplo: “Homo sapiens”, “9606”.

**Salida:**

Devuelve un diccionario con los siguientes campos:

-**”chromosome”:** Indica el cromosoma al que pertenece el gen (propiedad: BFO\_0000050 (part of)).

-**”start”**: Indica la posición de inicio del gen en la secuencia genómica (propiedad: GENO\_0000894 (start\_position)).

-**”end”**: Indica la posición de finalización del gen en la secuencia genómica (propiedad: GENO\_0000895 (end\_position)).

-**”strand”:** Indica la orientación del gen en la secuencia genómica (propiedad: GENO\_0000906 (on strand)).

-**”assembly”:** Indica el ensamblaje del genoma humano correspondiente a nuestro gen (propiedad: hasVersion).

-**”alt\_gene\_sources”:** Corresponde a otras fuentes o bases de datos que contienen información relacionada con el gen de interés (propiedad: closeMatch).

-**”definition”:** Proporciona una definición del gen (propiedad: definition).


**Ejemplo de ejecución:**

Entrada: **getGene\_info**("Brca1", "Mus musculus")

Salida: 

{'start': '101379587',

` `'end': '101442808',

` `'strand': 'ReverseStrandPosition',

` `'chr': 'NC\_000077.7',

` `'assembly': 'GCF\_000001635.27',

'alt\_gene\_sources':'ensembl/ENSMUSG00000017146; ensembl/ENSMUSG00000017146.13; ncbigene/12189',

` `'definition': 'gene 10090/Brca1 encoding [A0A087WP26\_MOUSE A0A087WPE1\_MOUSE A0A087WPK5\_MOUSE BRCA1\_MOUSE]'}





**Tabla resumen:**


|Variable|Rol|Tipo|Descripción|Propiedad de la Ontología|Grafo|
| :- | :- | :- | :- | :- | :- |
|**“gene”**|**entrada**|**string**|**Nombre del gen en formato symbol**|**skos:prefLabel**|**gene**|
|**“taxon”**|**entrada**|**string**|**Número de taxón o nombre del organismo**|**rdfs:label**|**taxon**|
|**“chromosome”**|**salida**|**string**|**Cromosoma al que pertenece el gen**|<p>**obo:BFO\_0000050**</p><p>**(part of )**</p>|**gene**|
|**“start”**|**salida**|**integer**|**Posición de inicion del gen**|<p>**obo:GENO\_0000894**</p><p>**(start position)** </p>|**gene**|
|**“end”**|**salida**|**integer**|**Posición de fin del gen**|<p>**obo:GENO\_0000895**</p><p>**(end position)** </p>|**gene**|
|**“strand”**|**salida**|**string**|**Orientación del gen**|**obo:GENO\_0000906 (on strand)** |**gene**|
|**“assembly”**|**salida**|**string**|**Ensamblaje del genoma humano al que corresponde el gen**|**dc:hasVersion**|**gene**|
|**“alt\_gene\_sources”**|**salida**|**string**|**Fuentes alternativas con información sobre el gen**|**skos:closeMatch**|**gene**|
|**“definition”**|**salida**|**string**|**Descripción del gen** |**skos:definition**|**gene**|

#
# <a name="_c4lumi1vi55h"></a><a name="_xbzdxllvku01"></a>**Función getGenes\_by\_coord(chr, start, end , strand):**
**Descripción:** Función que devuelve los genes en formato gene symbol(prefLabel), que se encuentran dentro de las coordenadas genómicas especificadas. Usamos la información disponible en el grafo  **http://rdf.biogateway.eu/graph/gene.**

**Parámetros:** 

-**”chr”**: Indica el cromosoma al que pertenece el segmento (identificador del cromosoma en el NCBI). Ejemplo: “NC\_000074.7”. 

-**”start”**: Indica la posición de inicio del segmento en la secuencia genómica. Ejemplo: “90973665”

-**”end”:** Indica la posición de finalización del segmento en la secuencia genómica. Ejemplo: “91075654”

-**”strand”**: Indica la cadena de ADN en la que se quiere realizar la búsqueda. Si se declara como none, buscará en ambas cadenas. Valores permitidos: “ReverseStrandPosition” y “ForwardStrandPosition”.


**Salida:**

Lista de genes que se encuentran dentro de las coordenadas genómicas especificadas. A su vez, para cada gen se indica:

**-”gene\_name”:** Nombre del gen en formato gene symbol (propiedad: prefLabel). 

-**”start”**: Indica la posición de inicio del gen en la secuencia genómica (propiedad: GENO\_0000894).

-**”end”**: Indica la posición de finalización del gen en la secuencia genómica (propiedad: GENO\_0000895).

-**”strand”:** Indica la orientación del gen en la secuencia genómica (propiedad: GENO\_0000906). Este campo sólo se proporciona si no se ha especificado cadena de ADN en la función.


**Ejemplo ejecución:**

Entrada: getGenes\_by\_coord("NC\_051352.1", 52565276, 58596412 ,"ForwardStrandPosition")

Salida: 

[{'gene\_name': 'Fzd8', 'start': '57312924', 'end': '57320551'},

` `{'gene\_name': 'Hist2h3c2', 'start': '183797721', 'end': '41378877'},

` `{'gene\_name': 'Hist2h3c2', 'start': '183837311', 'end': '41532577'},

` `{'gene\_name': 'Hist2h3c2', 'start': '183797721', 'end': '41532577'},

` `{'gene\_name': 'Hist2h3c2', 'start': '183837311', 'end': '41426735'},

` `{'gene\_name': 'Hist2h3c2', 'start': '183837311', 'end': '41378877'},

` `{'gene\_name': 'Hist2h3c2', 'start': '183797721', 'end': '41426735'},

` `{'gene\_name': 'Hnrnpk', 'start': '91756628', 'end': '6275001'},

` `{'gene\_name': 'Lgals8', 'start': '58024652', 'end': '58052764'},

` `{'gene\_name': 'Map3k8', 'start': '53382908', 'end': '53403216'},

` `{'gene\_name': 'Mtr', 'start': '58219998', 'end': '58308560'},

` `{'gene\_name': 'Actn2', 'start': '58143334', 'end': '58210622'},

` `{'gene\_name': 'Crem', 'start': '54238889', 'end': '54305989'}]



**Tabla resumen:**


|Variable|Rol|Tipo|Descripción|Propiedad de la Ontología|Grafo|
| :- | :- | :- | :- | :- | :- |
|**“chr”**|**entrada**|**string**|**Cromosoma al que pertenece el segmento genómico**|**obo:BFO\_0000050 (part of )**|**gene**|
|**“start”**|**entrada**|**integer**|**Posición de inicion del segmento genómico**|<p>**obo:GENO\_0000894**</p><p>**(start position)** </p>|**gene**|
|**“end”**|**entrada**|**integer**|**Posición de fin del segmento genómico**|<p>**obo:GENO\_0000895**</p><p>**(end position)** </p>|**gene**|
|**“strand”**|**entrada (opcional)**|**string**|**Cadena de DNA donde se quiere realizar la búsqueda**|**obo:GENO\_0000906 (on strand)** |**gene**|
|**“gene\_name”**|**salida**|**string**|**Nombre del gen en formato symbol**|**skos:prefLabel**|**gene**|
|**“start”**|**salida**|**integer**|**Posición de inicion del gen**|<p>**obo:GENO\_0000894**</p><p>**(start position)** </p>|**gene**|
|**“end”**|**salida**|**integer**|**Posición de fin del gen**|<p>**obo:GENO\_0000895**</p><p>**(end position)** </p>|**gene**|
|**“strand”**|**salida (opcional)**|**string**|**Orientación del gen**|**obo:GENO\_0000906 (on strand)** |**gene**|



# <a name="_9mr7ueqc7lrj"></a>**Función getProtein\_info(protein)**

**Descripción:** Función que facilita la información asociada a la proteína de interés, disponible en el grafo de conocimiento:  **http://rdf.biogateway.eu/graph/protein.**

Esta función tiene un parámetro, el nombre de la proteína que queremos consultar en formato entry name de Uniprot.

**Parámetros:** 

**-“protein”:** Insertamos el nombre de la proteína en formato entry name de Uniprot (propiedad: prefLabel). Ejemplo: “BRCA1\_HUMAN”.

**Salida:**

Devuelve un diccionario con los siguientes campos:

**-”protein\_alt\_names”:** Devuelve los nombres alternativos de la proteína (propiedad: altLabel), en concreto el nombre de la proteína en formato entry de Uniprot, así como el nombre del gen que la codifica y sinónimos de este gen.

-**”definition”:** Proporciona una definición de la proteína (propiedad: definition).

**-”evidence\_level”:** Este término se refiere al nivel de evidencia que respalda la información asociada con la proteína (propiedad: evidenceLevel).

**-”alt\_sources”:** Hace referencia a otras fuentes o bases de datos que contienen información relacionada con la proteína (propiedad: closeMatch).

**-”articles”:** Corresponde a artículos científicos o publicaciones que están asociadas con la proteína de interés que se encuentran en la base de datos Pubmed (propiedad: SIO\_000772 (has evidence)).



**Ejemplo ejecución:**

Entrada: getProtein\_info(“TOX3\_HUMAN”)



Salida:

{'protein\_alt\_ids': 'O15405; TOX3; TNRC9; CAGF9', 'definition': 'TOX high mobility group box family member 3 (CAG trinucleotide repeat-containing gene F9 protein) (Trinucleotide repeat-containing gene 9 protein)', 'evidence\_level': '5.0', 'alt\_sources': 'ensembl/ENSP00000219746.9; ensembl/ENSP00000385705.3; refseq/NP\_001073899.2; refseq/NP\_001139660.1', 'articles': 'pubmed/15616553; pubmed/9225980; pubmed/21172805; pubmed/14702039'}

**Tabla resumen:**


|Variable|Rol|Tipo|Descripción|Propiedad de la Ontología|Grafo|
| :- | :- | :- | :- | :- | :- |
|**“protein”**|**entrada**|**string**|**Nombre de la proteína en formato entry name de Uniprot**|**skos:prefLabel**|**protein**|
|**”protein\_alt\_names”**|**salida**|**string**|**Nombres alternativos de la proteína**|**skos:altLabel**|**protein**|
|**”definition”**|**salida**|**string**|**Definición de la proteína**|**skos:definition**|**protein**|
|**”evidence\_level”**|**salida**|**string**|**Nivel de evidencia asociado a la proteína**|**sch:evidenceLevel**|**protein**|
|**“alt\_sources”**|**salida**|**string**|**Fuentes alternativas con información sobre la proteína**|**skos:closeMatchl**|**protein**|
|**“articles”**|**salida**|**string**|**Artículos relacionados con la proteína**|<p>**sio:SIO\_000772**</p><p>**(has evidence)**</p>|**protein**|



# <a name="_j0sbhu4m7dpk"></a>**Función getPhenotype(phenotype):**

**Descripción:** Esta función permitirá obtener el fenotipo a partir de un identificador OMIM o del nombre de una enfermedad, usa el grafo **http://rdf.biogateway.eu/graph/omim**:

-Por un lado si el valor introducido es un identificador OMIM de un fenotipo, nos devolverá su etiqueta preferente.

-Por otro lado si el valor introducido es el nombre de una enfermedad (por ejemplo “breast cancer”), nos devolverá la etiqueta preferente y el identificador omim de aquellos fenotipos cuya etiqueta, tanto preferente como alternativa, contenga la enfermedad introducida. Es decir, los fenotipos que contengan el nombre introducido.

**Parámetros:** 

-**“phenotype”**: Los valores permitidos de este parámetro serán:

-Identificador OMIM de un fenotipo. Ejemplo “MTHU036782”.

-Nombre de una enfermedad. Ejemplo “lung cancer”.


**Salida:**



La salida dependerá del tipo de parámetro introducido:

-Si ha sido introducido un identificador OMIM de un fenotipo, la salida será simplemente la etiqueta preferente de este identificador (prefLabel).

-Si se ha introducido el nombre de una enfermedad, la salida estará compuesta por aquellos fenotipos que contienen en su etiqueta preferente esta enfermedad (prefLabel o altLabel), así como su identificador OMIM.

**Ejemplo ejecución:**

Entrada: getPhenotype("breast cancer")

Salida: [{'omim\_id': '604704', 'label': 'BREAST CANCER ANTIESTROGEN RESISTANCE 3'},

` `{'omim\_id': 'MTHU036782', 'label': 'Breast cancer, lobular'},

` `{'omim\_id': 'MTHU068657', 'label': 'Breast cancer, early-onset'},

` `{'omim\_id': '137215',

`  `'label': 'DIFFUSE GASTRIC AND LOBULAR BREAST CANCER SYNDROME'},

` `{'omim\_id': 'MTHU015471',

`  `'label': 'Paraneoplastic SPS is associated with breast cancer and other malignancies'},

Entrada: getPhenotype("604704")

Salida: [{'phen\_label': 'BREAST CANCER ANTIESTROGEN RESISTANCE 3'}]

**Tabla resumen:**

|Variable|Rol|Tipo|Descripción|Propiedad de la Ontología|Grafo|
| :- | :- | :- | :- | :- | :- |
|**“phenotype”**|**entrada**|**string**|**Nombre de una enfermedad o identificador OMIM de un fenotipo** |**skos:prefLabel**|**omim**|
|**“omim\_id”**|**salida**|**string**|**Identificador OMIM del fenotipo (opcional)**|**skos:prefLabel**|**omim**|
|**“phen\_label”**|**salida**|**string**|**Nombre común del fenotipo**|**skos:prefLabel**|**omim**|

# <a name="_dhv1rzxb29dg"></a>**Función getCRM\_info(crm):**

**Descripción:** Función que devuelve la información asociada al módulo cis-regulador (crm) que queremos consultar, disponible en el grafo de conocimiento:  **http://rdf.biogateway.eu/graph/crm.**

Esta función tiene un parámetro el cual es el nombre del crm que queremos consultar (propiedad: prefLabel).


**Parámetros:** 

-**”crm”**: El parámetro introducido en la función será el nombre preferente del módulo cis-regulador (propiedad: prefLabel). Ejemplo "crm/CRMHS00003225754".

**Salida:**

Devuelve un diccionario con los siguientes campos:

-**”start”**: Indica la posición de inicio del crm en la secuencia genómica (propiedad: GENO\_0000894 (start\_position)).

-**”end”**: Indica la posición de finalización del crm en la secuencia genómica (propiedad: GENO\_0000895 (end\_position)).

-**”chromosome”**: Indica el cromosoma al que pertenece el crm, (identificador del cromosoma en el NCBI) (propiedad: BFO\_0000050 (part\_of)). 

-**”assembly”:** Indica el ensamblaje del genoma humano correspondiente a nuestro crm (propiedad: hasVersion).

-**”taxon”**: Devuelve el taxón al que pertenece este crm (identificador taxonómico del NCBI) (propiedad: RO\_0002162).

-**”definition”**: Definición del crm disponible en la propiedad definition del grafo de conocimiento.


**Ejemplo ejecución:**

Entrada: getCRM\_info("crm/CRMHS00000005387")

Salida: 

[{'start': '355447',

`  `'end': '358949',

`  `'chromosome': 'NC\_000011.10',

`  `'assembly': 'GCF\_000001405.26',

`  `'taxon': 'NCBITaxon\_9606',

`  `'definition': 'Cis-regulatory module located in Homo sapiens chr11 between 355447 and 358949'}]


**Tabla resumen:**

|Variable|Rol|Tipo|Descripción|Propiedad de la Ontología|Grafo|
| :- | :- | :- | :- | :- | :- |
|**“crm”**|**entrada**|**string**|<p>**Nombre del módulo cis-regulador** </p><p>**(crm)**</p>|**skos:prefLabel**|**crm**|
|**“taxon”**|**salida**|**string**|**Número de taxón al que pertenece el crm**|<p>**obo:RO\_0002162**</p><p>**(in taxon)**</p>|**crm**|
|**“chromosome”**|**salida**|**string**|**Cromosoma al que pertenece el crm**|<p>**obo:BFO\_0000050**</p><p>**(part of )**</p>|**crm**|
|**“start”**|**salida**|**integer**|**Posición de inicion del crm**|<p>**obo:GENO\_0000894**</p><p>**(start position)**</p>|**crm**|
|**“end”**|**salida**|**integer**|**Posición de fin del crm**|<p>**obo:GENO\_0000895**</p><p>**(end position)**</p>|**crm**|
|**“strand”**|**salida**|**string**|**Orientación del crm**|<p>**obo:GENO\_0000906**</p><p>**(on strand)**</p>|**crm**|
|**“assembly”**|**salida**|**string**|**Ensamblaje del genoma humano al que corresponde el crm**|**dc:has Version**|**crm**|
|**“definition”**|**salida**|**string**|**Descripción del crm** |**skos:definition**|**crm**|

# <a name="_dlbdtuhkif8p"></a>**Función getCRM\_additional\_info(crm):**
**Descripción:** Esta función proporcionará información adicional sobre el crm de interés, disponible en el grafo **http://rdf.biogateway.eu/graph/crm** que no se obtiene de la función getCRM\_info.

**Parámetros:** 

-**”crm”**: El parámetro introducido en la función será el nombre preferente del módulo cis-regulador (propiedad: prefLabel). Ejemplo "crm/CRMHS00000005387”.

**Salida:**

Devuelve un diccionario con los siguientes campos:

**-“evidence”:** Corresponde a la evidencia que respalda la información disponible sobre el módulo-cis regulador (propiedad: evidenceOrigin).

**-”database”:** Indica la base de datos donde se encuentra registrada la información sobre el crm de interés (propiedad: SIO\_000253 (has source)).

**-”biological\_samples”:** Se refiere a los diferentes tipos de muestras biológicas que están asociados con el estudio del módulo cis-regulador (propiedad: TXPO\_0003500 (observed in)). En concreto, devolverá los identificadores en formato de términos ontológicos. Ejemplo: “CLO\_0001601”, “UBERON\_0002113”, “BTO\_0000018”.

-**”articles”:** Hace referencia a los artículos científicos que han sido publicados en Pubmed relacionados con el módulo cis-regulador introducido (propiedad: SIO\_000772 (has evidence)).

**Ejemplo ejecución:**

Entrada: getCRM\_add\_info("crm/CRMHS00000005387")

Salida: 

{'evidence': '<http://www.licpathway.net/ENdb/search/Detail.php?Species=Human&Enhancer_id=E_01_273>',

` `'database': '<http://www.licpathway.net/ENdb/>',

` `'biological\_samples': 'BTO\_0000007; BTO\_0000018; CLO\_0001230; CLO\_0001601; CL\_0002518; CL\_0000082; UBERON\_0002048; UBERON\_0002113',

` `'articles': 'pubmed/28511927'}

**Tabla resumen:**


|Variable|Rol|Tipo|Descripción|Propiedad de la Ontología|Grafo|
| :- | :- | :- | :- | :- | :- |
|**“crm”**|**entrada**|**string**|**Nombre del módulo cis-regulador (crm)**|**skos:prefLabel**|**crm**|
|**”evidence”**|**salida**|**string**|**Nivel de evidencia asociado al crm**|**sch:evidenceOrigin**|**crm**|
|**“database”**|**salida**|**string**|**Base de datos donde encontramos la información del crm**|<p>**sio:SIO\_000253**</p><p>**(has source )**</p>|**crm**|
|**“biological\_samples”**|**salida**|**string**|**Muestras biológicas asociadas al crm de interés**|<p>**obo:TXPO\_0003500**</p><p>**(observed in )**</p>|**crm**|
|**“articles”**|**salida**|**string**|**Artículos relacionados con el crm**|<p>**sio:SIO\_000772**</p><p>**(has evidence)**</p>|**crm**|


# <a name="_ned0hcwk5q78"></a>**Función getCRMs\_by\_coord(chromosome, start, end):**
**Descripción:** Función que devuelve el identificador de los crms (prefLabel) que se encuentran dentro de las coordenadas genómicas especificadas. 

**Parámetros:** 

-**”chromosome”**: Indica el cromosoma en el que queremos realizar la búsqueda, los valores permitidos **son chr-número de cromosoma**. Ejemplo: “chr-1”. “chr-18”, “mitochondrial” (para buscar en el ADN mitocondrial).

-**”start”**: Indica la posición de inicio del segmento en la secuencia genómica. Ejemplo: “90973665”

-**”end”:** Indica la posición de finalización del segmento en la secuencia genómica. Ejemplo: “91075654”




**Salida:**

Lista de módulos-cis reguladores que se encuentran dentro de las coordenadas genómicas especificadas. A su vez, para cada crm se indica:

**-”crm\_name”:** Nombre del módulo cis regulador que se encuentra dentro de las coordenadas genómicas especificadas (propiedad: prefLabel). 

-**”start”**: Indica la posición de inicio del crm en la secuencia genómica (propiedad: GENO\_0000894).

-**”end”**: Indica la posición de finalización del crm en la secuencia genómica (propiedad: GENO\_0000895).

**Ejemplo ejecución:**

Entrada: getCRMs\_by\_coord("mitochondrial","1", "500")

Salida: 

[{'crm\_name': 'crm/CRMHS00032244267', 'start': '175', 'end': '426'},

` `{'crm\_name': 'crm/CRMHS00032244371', 'start': '230', 'end': '389'},

` `{'crm\_name': 'crm/CRMHS00032244378', 'start': '32', 'end': '334'}]


**Tabla resumen:**



|Variable|Rol|Tipo|Descripción|Propiedad de la Ontología|Grafo|
| :- | :- | :- | :- | :- | :- |
|**“chromosome”**|**entrada**|**string**|**Cromosoma al que pertenece el segmento genómico**|<p>**obo:BFO\_0000050**</p><p>**(part of )**</p>|**crm**|
|**“start”**|**entrada**|**integer**|**Posición de inicio del segmento genómico**|<p>**obo:GENO\_0000894**</p><p>**(start position)**</p>|**crm**|
|**“end”**|**entrada**|**integer**|**Posición de fin del segmento genómico**|<p>**obo:GENO\_0000895**</p><p>**(end position)**</p>|**crm**|
|**“crm\_name”**|**salida**|**string**|**Nombre del crm que se encuentra dentro de las coordenadas genómicas** |**skos:prefLabel**|**crm**|
|**“start”**|**salida**|**integer**|**Posición de inicio del crm**|<p>**obo:GENO\_0000894**</p><p>**(start position)**</p>|**crm**|
|**“end”**|**salida**|**integer**|**Posición de fin del crm**|<p>**obo:GENO\_0000895**</p><p>**(end position)**</p>|**crm**|


# <a name="_7y26w9cqizwf"></a>**Función getTAD\_info(tad):**

**Descripción:** Función que proporciona la información asociada al dominio topológicamente asociado (tad) que queremos consultar, disponible en el grafo de conocimiento:  **http://rdf.biogateway.eu/graph/tad.**

Esta función tiene un parámetro el cual es el identificador del tad que queremos consultar (propiedad: prefLabel).

**Parámetros:** 

-**”tad”**: El parámetro introducido en la función será el nombre preferente del dominio topológicamente asociado (propiedad: prefLabel). Ejemplo "tad/TADHS00000038004”


**Salida:**

Devuelve un diccionario con los siguientes campos:

-**”chromosome”**: Indica el cromosoma al que pertenece el tad, (identificador del cromosoma en el NCBI) (propiedad: BFO\_0000050). 

-**”start”**: Indica la posición de inicio del tad en la secuencia genómica (propiedad: GENO\_0000894).

-**”end”**: Indica la posición de finalización del tad en la secuencia genómica (propiedad: GENO\_0000895).

-**”assembly”:** Indica el ensamblaje del genoma humano correspondiente a nuestro crm (propiedad: hasVersion).

-**”taxon”**: Devuelve el taxón al que pertenece este tad (identificador taxonómico del NCBI) (propiedad: RO\_0002162 ).

-**”definition”**: Definición del tad disponible en la propiedad definition del grafo de conocimiento.


**Ejemplo ejecución:**

Entrada: getTAD\_info("tad/TADHS00000038004")

Salida:

[{'start': '34120000',

`  `'end': '35840000',

`  `'chromosome': 'NC\_000013.11',

`  `'assembly': 'GCF\_000001405.26',

`  `'taxon': 'NCBITaxon\_9606',

`  `'definition': 'Topologically associated domain located in Homo sapiens chr13 between 34120000 and 35840000'}]

**Tabla resumen:**

|Variable|Rol|Tipo|Descripción|Propiedad de la Ontología|Grafo|
| :- | :- | :- | :- | :- | :- |
|**“tad”**|**entrada**|**string**|**Nombre del dominio topológicamente asociado**|**objeto de la relación prefLabel**|**tad**|
|**“chromosome”**|**salida**|**string**|**Cromosoma al que pertenece el tad**|<p>**obo:BFO\_0000050**</p><p>**(part of )**</p>|**tad**|
|**“start”**|**salida**|**integer**|**Posición de inicion del tad**|<p>**obo:GENO\_0000894**</p><p>**(start position)**</p>|**tad**|
|**“end”**|**salida**|**integer**|**Posición de fin del tad**|<p>**obo:GENO\_0000895**</p><p>**(end position)**</p>|**tad**|
|**“assembly”**|**salida**|**string**|**Ensamblaje del genoma humano al que corresponde el tad**|**dc:hasVersion**|**tad**|
|**“taxon”**|**salida**|**string**|**Taxón al que pertenece este tad (identificador del NCBI)**|<p>**obo:RO\_0002162**</p><p>**(in taxon )**</p>|<p></p><p>**tad**</p>|
|**“definition”**|**salida**|**string**|**Descripción del tad** |**skos:definition**|**tad**|

# <a name="_6gqkc0vfngur"></a>**Función getTAD\_additional\_info(tad):**
**Descripción:** Esta función proporcionará información adicional sobre el tad de interés, disponible en el grafo **http://rdf.biogateway.eu/graph/tad** que no se obtiene de la función getTAD\_info.



**Parámetros:** 

-**”tad”**: El parámetro introducido en la función será el nombre preferente del dominio topológicamente asociado (propiedad: prefLabel). Ejemplo "tad/TADHS00000038004”.

**Salida:**

Devuelve un diccionario con los siguientes campos:

**-“evidence”:** Corresponde a la evidencia que respalda la información disponible sobre el tad (propiedad: evidenceOrigin).

**-”database”:** Indica la base de datos donde se encuentra registrada la información sobre el tad de interés (propiedad: SIO\_000253 (has source)).

**-”biological\_samples”:** Se refiere a los diferentes tipos de muestras biológicas que están asociados con el estudio del dominio topológicamente asociado (propiedad: TXPO\_0003500 (observed in)). En concreto, devolverá los identificadores en formato de términos ontológicos. Ejemplo: “CLO\_0001601”, “UBERON\_0002113”, “BTO\_0000018”.

-**”articles”:** Hace referencia a los artículos científicos que han sido publicados en Pubmed relacionados con el dominio topológicamente asociado introducido (propiedad: SIO\_000772 (has evidence)).

**Ejemplo ejecución:**

Entrada: getTAD\_add\_info("tad/TADHS00000038004")

Salida:

{'evidence': '<http://dna.cs.miami.edu/TADKB/domain.php?sp=hum&cl=HMEC&rg=hg19&chr=14&se=96700000_96850000&id=83&res=50kb&caller=IS>',

` `'database': '<http://dna.cs.miami.edu/TADKB/>',

` `'biological\_samples': 'BTO\_0001229; CLO\_0006951; CL\_0002327; UBERON\_0000310; UBERON\_0002048; BTO\_0004300; CL\_0002553',

` `'articles': 'pubmed/30871473'}

**Tabla resumen:** 

|Variable|Rol|Tipo|Descripción|Propiedad de la Ontología|Grafo|
| :- | :- | :- | :- | :- | :- |
|**“tad”**|**entrada**|**string**|**Nombre del dominio topológicamente asociado (tad)**|**skos:prefLabel**|**tad**|
|**”evidence”**|**salida**|**string**|**Nivel de evidencia asociado al tad**|**sch:evidenceOrigin**|**tad**|
|**“database”**|**salida**|**string**|**Base de datos donde encontramos la información del tad**|<p>**sio:SIO\_000253**</p><p>**(has source )**</p>|**tad**|
|**“biological\_samples”**|**salida**|**string**|**Muestras biológicas asociadas al tad de interés**|<p>**obo:TXPO\_0003500**</p><p>**(observed in )**</p>|**tad**|
|**“articles”**|**salida**|**string**|**Artículos relacionados con el tad**|<p>**sio:SIO\_000772**</p><p>**(has evidence)**</p>|**tad**|

# <a name="_1x5z6oer29w9"></a>**Función getTAD\_by\_coord(chromosome,start, end):**

**Descripción:** Función que devuelve el identificador de los tads (prefLabel) que se encuentran dentro de las coordenadas genómicas especificadas. 

**Parámetros:** 

-**”chromosome”**: Indica el cromosoma al que pertenece el segmento (identificador del cromosoma en el NCBI). Ejemplo: “chr-13”. 

-**”start”**: Indica la posición de inicio del segmento en la secuencia genómica. Ejemplo: “90973665”

-**”end”:** Indica la posición de finalización del segmento en la secuencia genómica. Ejemplo: “91075654”



**Salida:**

**-”tad\_name”:** Devuelve una lista de los ids de los dominios topológicamente asociados que se encuentran dentro de las coordenadas genómicas especificadas (propiedad: prefLabel). 

-**”start”**: Indica la posición de inicio del tad en la secuencia genómica (propiedad: GENO\_0000894).

-**”end”**: Indica la posición de finalización del tad en la secuencia genómica (propiedad: GENO\_0000895).

**Ejemplo ejecución:**

Entrada: getTADs\_by\_coord("chr-13","34120000", "35840000")

Salida: 

[{'tad\_id': 'tad/TADHS00000038004', 'start': '34120000', 'end': '35840000'},

` `{'tad\_id': 'tad/TADHS00000029314', 'start': '35200000', 'end': '35840000'},

` `{'tad\_id': 'tad/TADHS00000071459', 'start': '34125863', 'end': '35175863'},

` `{'tad\_id': 'tad/TADHS00000071460', 'start': '34165863', 'end': '35825863'},

` `{'tad\_id': 'tad/TADHS00000071461', 'start': '34185863', 'end': '35155863'},

` `{'tad\_id': 'tad/TADHS00000071462', 'start': '34305863', 'end': '35455863'},

` `{'tad\_id': 'tad/TADHS00000071463', 'start': '34325863', 'end': '35025863'},

` `{'tad\_id': 'tad/TADHS00000071465', 'start': '35150863', 'end': '35800863'},

` `{'tad\_id': 'tad/TADHS00000071468', 'start': '35170863', 'end': '35810863'},

` `{'tad\_id': 'tad/TADHS00000071479', 'start': '35195863', 'end': '35815863'},

` `{'tad\_id': 'tad/TADHS00000071484', 'start': '35215863', 'end': '35825863'},

` `{'tad\_id': 'tad/TADHS00000071485', 'start': '35225863', 'end': '35825863'},

` `{'tad\_id': 'tad/TADHS00000071489', 'start': '35375863', 'end': '35725863'},

` `{'tad\_id': 'tad/TADHS00000071490', 'start': '35375863', 'end': '35775863'},

` `{'tad\_id': 'tad/TADHS00000071491', 'start': '35375863', 'end': '35825863'},

` `{'tad\_id': 'tad/TADHS00000071492', 'start': '35425863', 'end': '35725863'}]

**Tabla resumen:**

|Variable|Rol|Tipo|Descripción|Propiedad de la Ontología|Grafo|
| :- | :- | :- | :- | :- | :- |
|**“chromosome”**|**entrada**|**string**|**Cromosoma al que pertenece el segmento genómico**|<p>**obo:BFO\_0000050**</p><p>**(part of )**</p>|**tad**|
|**“start”**|**entrada**|**integer**|**Posición de inicio del segmento genómico**|<p>**obo:GENO\_0000894**</p><p>**(start position)**</p>|**tad**|
|**“end”**|**entrada**|**integer**|**Posición de fin del segmento genómico**|<p>**obo:GENO\_0000895**</p><p>**(end position)**</p>|**tad**|
|**“tad\_name”**|**salida**|**string**|**Nombre del tad que se encuentra dentro de las coordenadas genómicas** |**skos:prefLabel**|**tad**|
|**“start”**|**salida**|**integer**|**Posición de inicio del tad**|<p>**obo:GENO\_0000894**</p><p>**(start position)**</p>|**tad**|
|**“end”**|**salida**|**integer**|**Posición de fin del tad**|<p>**obo:GENO\_0000895**</p><p>**(end position)**</p>|**tad**|


# <a name="_xc1bar37pz53"></a>**Función gene2protein(gene,taxon)**

**Descripción:** Esta función permite obtener las proteínas codificadas por el gen introducido en la consulta, y en el taxón seleccionado. Si el valor de taxón es **None**, devolverá las proteínas codificadas por el gen en los distintos taxones. Esta información se obtendrá del grafo **http://rdf.biogateway.eu/graph/gene**

**Parámetros:** 

**-”gene”:** Este parámetro corresponde al nombre del gen en formato symbol (propiedad: prefLabel). Ejemplo: “BRCA1”

-**”taxon”:** Permite seleccionar el taxón en el que se quiere realizar la consulta. El valor puede ser el** identificador taxonómico del NCBI o el nombre del organismo (propiedad: label). Ejemplo: “Homo sapiens”, “9606”.


**Salida:**

Devuelve una lista con las proteínas codificadas por el gen de interés:

-”**protein\_name**”: La función devuelve los nombres en formato entry name de Uniprot (prefLabel) de las proteínas codificadas por el gen introducido (propiedad: SIO\_010078(encodes)).

**Ejemplo de ejecución:**

Entrada: gene2protein(“TOX3”,”9606”)

Salida:

[{‘protein\_name’: 'H3BTZ9\_HUMAN'},

` `{protein\_name: 'J3QQQ6\_HUMAN'},

` `{protein\_name: 'TOX3\_HUMAN'}]

**Tabla resumen:**

|Variable|Rol|Tipo|Descripción|Propiedad de la Ontología|Grafo|
| :- | :- | :- | :- | :- | :- |
|**“gene”**|**entrada**|**string**|**Nombre del gen en formato symbol**|**skos:prefLabel**|**gene**|
|**“taxon”**|**entrada**|**string**|**Número de taxón o nombre del organismo**|**skos:label**|**taxon**|
|**“protein\_name”**|**salida**|**string**|**Nombre de la proteína en formato entry name de Uniprot codificada por el gen introducido**|<p>**sio:SIO\_010078**</p><p>**(encodes)**</p>|**gene**|

# <a name="_7aboxbs7fesu"></a>**Función protein2gene(protein)**


**Descripción:** Esta función permite obtener el gen que codifica la proteína introducida en la consulta. Esta información se obtendrá del grafo **http://rdf.biogateway.eu/graph/gene**

**Parámetros:** 

**-“protein”:** Insertamos el nombre de la proteína tanto en formato entry name de Uniprot (propiedad: prefLabel) como en formato entry de Uniprot (propiedad: altLabel). Ejemplo: “BRCA1\_HUMAN”, “P38398”.

**Salida:**

-”**gene\_name**”: La función devuelve el nombre en formato symbol (prefLabel) del gen que codifica la proteína introducida (propiedad: SIO\_010078).

**Ejemplo de ejecución:**

Entrada: protein2gene("BRCA1\_MOUSE")

Salida: [{'gene\_name': 'Brca1'}]

**Tabla resumen:**


|Variable|Rol|Tipo|Descripción|Propiedad de la Ontología|Grafo|
| :- | :- | :- | :- | :- | :- |
|**“protein”**|**entrada**|**string**|**Nombre de la proteína en formato entry name de Uniprot codificada por el gen introducido**|**skos:prefLabel**|**protein**|
|**“gene\_name”**|**salida**|**string**|**Nombre del gen en formato symbol**|<p>**sio:SIO\_010078**</p><p>**(encodes)**</p>|**gene**|

# <a name="_yfat25lecx5n"></a>**Función gene2phen(gene)**

**Descripción:** Esta función posibilita la obtención de los fenotipos asociados a un gen previamente introducido como parámetro de esta función. Para ello explotaremos el grafo **http://rdf.biogateway.eu/graph/gene2phen.**

**Parámetros:**

**-”gene”:** Este parámetro corresponde al nombre del gen en formato symbol (propiedad: prefLabel). Ejemplo: “BRCA1”.

**Salida:**

La función devuelve una lista de los fenotipos relacionados con el gen de interés. A subes de cada fenotipo obtenemos los siguientes datos:

**-”omim\_id”:** Corresponde al identificador Omim del fenotipo que está asociado al gen introducido (propiedad: RO\_0002331 (involved in)).

-**”phen\_label”:** Se refiere a la etiqueta preferente del fenotipo al que corresponde el identificador omim (pref\_label).

**Ejemplo de ejecución:**

Entrada: gene2phen(“BRCA1”)

Salida: 

[{'omim\_id': '114480', 'phen\_label': 'Breast cancer (BC)'},

` `{'omim\_id': '167000', 'phen\_label': 'Ovarian cancer (OC)'},

` `{'omim\_id': '604370',

`  `'phen\_label': 'Breast-ovarian cancer, familial, 1 (BROVCA1)'},

` `{'omim\_id': '617883',

`  `'phen\_label': 'Fanconi anemia, complementation group S (FANCS)'}]

**Tabla resumen:**

|Variable|Rol|Tipo|Descripción|Propiedad de la Ontología|Grafo|
| :- | :- | :- | :- | :- | :- |
|**“gene”**|**entrada**|**string**|**Nombre de una enfermedad o identificador OMIM de un fenotipo** |<p>**obo:RO\_0002331**</p><p>**(involved in )**</p>|**gene2phen**|
|**“omim\_id”**|**salida**|**string**|**Identificador OMIM del fenotipo (opcional)**|<p>**obo:RO\_0002331**</p><p>**(involved in)**</p>|**gene2phen**|
|**“phen\_label”**|**salida**|**string**|**Nombre común del fenotipo**|**skos:prefLabel**|**gene2phen**|


# <a name="_qyumd717q3p0"></a>**Función phen2gene(phenotype)**

**Descripción:** Esta función permite la obtención de los genes asociados a un fenotipo previamente introducido como parámetro de esta función. Para ello explotaremos el grafo **http://rdf.biogateway.eu/graph/gene2phen.**

**Parámetros:**

-**”phenotype”**: Este parámetro corresponde al fenotipo de interés. Permite tanto su identificador OMIM (“211980”), como el nombre de una enfermedad(“lung cancer”).


**Salida:**

-”**gene\_name**”: La función devuelve una lista con los nombres en formato symbol (porpiedad: prefLabel) de los genes relacionados con el fenotipo de interés (propiedad: RO\_0002331).

**Ejemplo de ejecución:**

Entrada: phen2gene("lung cancer")

Salida: 

[{'gene\_name': 'MXRA5'}, {'gene\_name': 'BRAF'}, {'gene\_name': 'ERBB2'}, {'gene\_name': 'SLC22A18'}]


**Tabla resumen:**

|Variable|Rol|Tipo|Descripción|Propiedad de la Ontología|Grafo|
| :- | :- | :- | :- | :- | :- |
|**“phenotype”**|**entrada**|**string**|**Nombre de una enfermedad o identificador OMIM de un fenotipo** |<p>**obo:RO\_0002331**</p><p>**(involved in )**</p>|**gene2phen**|
|**“gene\_name”**|**salida**|**string**|**Nombre del gen en formato symbol**|<p>**obo:RO\_0002331**</p><p>**(involved in)**</p>|**gene2phen**|

# <a name="_2agu27ozifcm"></a>**Función prot2bp(protein)**

**Descripción:** Esta función permite estudiar los procesos biológicos en los que participa la proteína de interés, explotando la información del grafo **http://rdf.biogateway.eu/graph/prot2bp.**

**Parámetros:**

**-“protein”:** Insertamos el nombre de la proteína tanto en formato entry name de Uniprot (propiedad: prefLabel) como en formato entry de Uniprot (propiedad: altLabel). Ejemplo: “BRCA1\_HUMAN”, “P38398”.

**Salida:**

La función devuelve una lista con los procesos biológicos relacionados con la proteína seleccionada. Presenta los siguientes campos:

**-”bp\_id”:** Corresponde al identificador del proceso biológico en Gene Ontology (propiedad: oboInOwl#id). Ejemplo: “GO:0035349”

**-”bp\_label”:** Se refiere a la etiqueta del proceso biológico en el grafo de conocimiento **http://rdf.biogateway.eu/graph/go** (propiedad: label). Ejemplo: "coenzyme A transmembrane transport"

**-”relation\_label”:** Hace referencia a la etiqueta que presenta la relación entre la proteína y el proceso biológico de interés (propiedad: prefLabel) disponible en el grafo **http://rdf.biogateway.eu/graph/prot2mf .**

**-”database”:** Indica la base de datos donde se encuentra registrada la información sobre la relación entre la proteína y el proceso biológico de interés (propiedad: SIO\_000253 (has source)).

**-”articles”:** Corresponde a artículos científicos o publicaciones que están asociadas con la relación entre la proteína y el proceso biológico de interés, que se encuentran en la base de datos Pubmed (propiedad: SIO\_000772 (has evidence)).


**Ejemplo de ejecución:**

Entrada: prot2bp("BRCA1\_HUMAN")

Salida: 

[{'bp\_id': 'GO:0035066',

`  `'bp\_label': 'positive regulation of histone acetylation',

`  `'relation\_label': 'P38398--GO:0035066',

`  `'database': 'goa/',

`  `'articles': 'pubmed/21873635'},

` `{'bp\_id': 'GO:0045786',

`  `'bp\_label': 'negative regulation of cell cycle',

`  `'relation\_label': 'P38398--GO:0045786',

`  `'database': 'goa/',

`  `'articles': 'pubmed/15159397'},

` `{'bp\_id': 'GO:0007095',

`  `'bp\_label': 'mitotic G2 DNA damage checkpoint signaling',

`  `'relation\_label': 'P38398--GO:0007095',

`  `'database': 'goa/',

`  `'articles': 'pubmed/19261748; pubmed/17643121; pubmed/17525340'}]


**Tabla resumen:**

|Variable|Rol|Tipo|Descripción|Propiedad de la Ontología|Grafo|
| :- | :- | :- | :- | :- | :- |
|**“protein”**|**entrada**|**string**|**Nombre de la proteína en formato entry name** |<p>**obo:RO\_0002331**</p><p>**(involved in )**</p>|**prot2bp**|
|**“bp\_id”**|**salida**|**string**|**Identificador en Gene Ontology del proceso biológico relacionado con la proteína de interés** |<p>**obo:RO\_0002331**</p><p>**(involved in)**</p>|**prot2bp**|
|**“bp\_label”**|**salida**|**string**|**Etiqueta del proceso biológico en el grafo** |**skos:label**|**go**|
|**“relation\_label”**|**salida**|**string**|**Etiqueta que presenta la relación entre la proteína y el proceso biológico de interés**|**skos:prefLabel**|**prot2bp**|
|**“database”**|**salida**|**string**|**Base de datos con la información sobre la relación**|<p>**sio:SIO\_0000253**</p><p>**(has source)**</p>|**prot2bp**|
|**“articles”**|**salida**|**string**|**Artículos asociados a la relación**|<p>**sio:SIO\_0000772**</p><p>**(has evidence)**</p>|**prot2bp**|

# <a name="_lydsknu6akc9"></a>**Función bp2prot(biological\_process,taxon)**

**Descripción:** Esta función devuelve las proteínas relacionadas con un proceso biológico específico explotando la información del grafo **http://rdf.biogateway.eu/graph/prot2bp.**


**Parámetros:**

**-”biological\_process”**: Este parámetro es el proceso biológico de interés, los valores permitidos son: su identificador en Gene Ontology (Ejemplo: “GO:0035349”) o el nombre de un proceso biológico (Ejemplo: “coenzyme A transmembrane transport”).

-**”taxon”:** Permite seleccionar el taxón en el que se quiere realizar la consulta. El valor puede ser el** identificador taxonómico del NCBI o el nombre del organismo (propiedad: label). Ejemplo: “Homo sapiens”, “9606”. Si el valor del taxon es **None**, aplicará la búsqueda con todos los taxones disponibles en el grafo de conocimiento.


**Salida:**

La función devuelve una lista con las proteínas relacionadas con el proceso biológico especificado. Presenta los siguientes campos:

-”**protein\_name**”: La función devuelve una lista con los nombres en formato entry name de Uniprot (prefLabel) de las proteínas relacionadas con el proceso biológico de interés (propiedad: RO\_0002331 (involved in)).

**-”relation\_label”:** Hace referencia a la etiqueta que presenta la relación entre la proteína y el proceso biológico de interés (propiedad: prefLabel) disponible en el grafo **http://rdf.biogateway.eu/graph/prot2mf .**

**-”database”:** Indica la base de datos donde se encuentra registrada la información sobre la relación entre la proteína y el proceso biológico de interés (propiedad: SIO\_000253 (has source)).

**-”articles”:** Corresponde a artículos científicos o publicaciones que están asociadas con la relación entre la proteína y el proceso biológico de interés, que se encuentran en la base de datos Pubmed (propiedad: SIO\_000772 (has evidence)).

**Ejemplo de ejecución:**

Entrada: bp2prot("GO:0043524","Homo sapiens")

Salida:

[{'protein\_name': 'FZD9\_HUMAN',

`  `'relation\_label': 'O00144--GO:0043524',

`  `'database': 'goa/',

`  `'articles': 'pubmed/27509850'},

` `{'protein\_name': 'HTRA2\_HUMAN',

`  `'relation\_label': 'O43464--GO:0043524',

`  `'database': 'goa/',

`  `'articles': 'pubmed/18221368'},

` `{'protein\_name': 'NGF\_HUMAN',

`  `'relation\_label': 'P01138--GO:0043524',

`  `'database': 'goa/',

`  `'articles': 'pubmed/21873635'},

` `{'protein\_name': 'GDNF\_HUMAN',

`  `'relation\_label': 'P39905--GO:0043524',

`  `'database': 'goa/',

`  `'articles': 'pubmed/8493557; pubmed/21873635'}]

**Tabla resumen:**

|Variable|Rol|Tipo|Descripción|Propiedad de la Ontología|Grafo|
| :- | :- | :- | :- | :- | :- |
|**“biological\_process”**|**entrada**|**string**|**Identificador en Gene Ontology o nombre del proceso biológico**|<p>**obo:RO\_0002331**</p><p>**(involved in )**</p>|**prot2bp**|
|**“taxon”**|**entrada (opcional)**|**string**|**Número de taxón o nombre del organismo**|<p>**obo:RO\_0002162**</p><p>**(in taxon)**</p>|**prot**|
|**“protein\_name”**|**salida**|**string**|**Nombre de la proteína relacionada con el proceso biológico en formato entry name de Uniprot** |<p>**obo:RO\_0002331**</p><p>**(involved in )**</p>|**prot2bp**|
|**“relation\_label”**|**salida**|**string**|**Etiqueta que presenta la relación entre la proteína y el proceso biológico de interés**|**skos:prefLabel**|**prot2bp**|
|**“database”**|**salida**|**string**|**Base de datos con la información sobre la relación**|<p>**sio:SIO\_0000253**</p><p>**(has source)**</p>|**prot2bp**|
|**“articles”**|**salida**|**string**|**Artículos asociados a la relación**|<p>**sio:SIO\_0000772**</p><p>**(has evidence)**</p>|**prot2bp**|

# <a name="_8bugs993y6kc"></a>**Función prot2cc(protein)**

**Descripción:** Esta función facilita el estudio de los componentes celulares en los que participa la proteína de interés, explotando la información del grafo 

**http://rdf.biogateway.eu/graph/prot2cc**

**Parámetros:**

**-“protein”:** Insertamos el nombre de la proteína tanto en formato entry name de Uniprot (propiedad: prefLabel) como en formato entry de Uniprot (propiedad: altLabel). Ejemplo: “BRCA1\_HUMAN”, “P38398”.


**Salida:**

La función devuelve una lista con los componentes celulares relacionados con la proteína seleccionada. Presenta los siguientes campos:


**-”cc\_id”:** Corresponde al identificador del componente celular en Gene Ontology (propiedad: oboInOwl#id) relacionado con nuestra proteína (propiedad: BFO\_0000050). Ejemplo: “GO:0005634”

**-”cc\_label”:** Se refiere a la etiqueta del componente celular en el grafo de conocimiento **http://rdf.biogateway.eu/graph/go** (propiedad: label). Ejemplo: "nucleus".

**-”relation\_label”:** Hace referencia a la etiqueta que presenta la relación entre la proteína y el componente celular de interés (propiedad: prefLabel) disponible en el grafo **http://rdf.biogateway.eu/graph/prot2mf .**

**-”database”:** Indica la base de datos donde se encuentra registrada la información sobre la relación entre la proteína y el componente celular de interés (propiedad: SIO\_000253 (has source)).

**-”articles”:** Corresponde a artículos científicos o publicaciones que están asociadas con la relación entre la proteína y el componente celular de interés, que se encuentran en la base de datos Pubmed (propiedad: SIO\_000772 (has evidence)).



**Ejemplo de ejecución:**

Entrada: prot2cc("BRCA1\_HUMAN")

Salida:

[{'cc\_id': 'GO:0000151',

`  `'cc\_label': 'ubiquitin ligase complex',

`  `'relation\_label': 'P38398--GO:0000151',

`  `'database': 'goa/',

`  `'articles': 'pubmed/14976165'},

` `{'cc\_id': 'GO:0000152',

`  `'cc\_label': 'nuclear ubiquitin ligase complex',

`  `'relation\_label': 'P38398--GO:0000152',

`  `'database': 'goa/',

`  `'articles': 'pubmed/14636569'},

` `{'cc\_id': 'GO:0000800',

`  `'cc\_label': 'lateral element',

`  `'relation\_label': 'P38398--GO:0000800',

`  `'database': 'goa/',

`  `'articles': 'pubmed/9774970'},

` `{'cc\_id': 'GO:0000931',

`  `'cc\_label': 'gamma-tubulin ring complex',

`  `'relation\_label': 'P38398--GO:0000931',

`  `'database': 'goa/',

`  `'articles': 'pubmed/12214252'},

` `{'cc\_id': 'GO:0005634',

`  `'cc\_label': 'nucleus',

`  `'relation\_label': 'P38398--GO:0005634',

`  `'database': 'goa/',

`  `'articles': 'pubmed/17643121; pubmed/20656689; pubmed/26833090; pubmed/17525340; pubmed/14636569; pubmed/9342365; pubmed/22369660; pubmed/19369211; pubmed/20160719; pubmed/23855721; pubmed/18171670'}]

**Tabla resumen:**

|Variable|Rol|Tipo|Descripción|Propiedad de la Ontología|Grafo|
| :- | :- | :- | :- | :- | :- |
|**“protein”**|**entrada**|**string**|**Nombre de la proteína en formato entry name de Uniprot** |<p>**obo:RO\_0002331**</p><p>**(involved in )**</p>|**prot2cc**|
|**“cc\_id”**|**salida**|**string**|**Identificador en Gene Ontology del componente celular relacionado con la proteína de interés** |<p>**obo:RO\_0002331**</p><p>**(involved in)**</p>|**prot2cc**|
|**“cc\_label”**|**salida**|**string**|**Etiqueta del proceso biológico componente celular en el grafo** |**skos:label**|**go**|
|**“relation\_label”**|**salida**|**string**|**Etiqueta que presenta la relación entre la proteína y el componente celular de interés**|**skos:prefLabel**|**prot2cc**|
|**“database”**|**salida**|**string**|**Base de datos con la información sobre la relación**|<p>**sio:SIO\_0000253**</p><p>**(has source)**</p>|**prot2cc**|
|**“articles”**|**salida**|**string**|**Artículos asociados a la relación**|<p>**sio:SIO\_0000772**</p><p>**(has evidence)**</p>|**prot2cc**|

# <a name="_txiqrufyzbl"></a>**Función cc2prot(cellular\_component,taxon)**

**Descripción:** Esta función devuelve las proteínas relacionadas con un componente celular específico explotando la información del grafo **http://rdf.biogateway.eu/graph/prot2cc.**


**Parámetros:**

**-”cellular\_component”**: Este parámetro es el componente celular de interés, los valores permitidos son: su identificador en Gene Ontology (Ejemplo: “GO:0034703”) o el nombre del componente celular (Ejemplo: “cation channel complex”).

-**”taxon”:** Permite seleccionar el taxón en el que se quiere realizar la consulta. El valor puede ser el** identificador taxonómico del NCBI o el nombre del organismo (propiedad: label). Ejemplo: “Homo sapiens”, “9606”. Si el valor del taxon es **None**, aplicará la búsqueda con todos los taxones disponibles en el grafo de conocimiento.


**Salida:**

La función devuelve una lista con las proteínas relacionadas con el componente celular especificado. Presenta los siguientes campos:

-”**protein\_name**”: La función devuelve una lista con los nombres en formato entry name de Uniprot (prefLabel) de las proteínas relacionadas con el componente celular de interés (propiedad: BFO\_0000050(part of)).

**-”relation\_label”:** Hace referencia a la etiqueta que presenta la relación entre la proteína y el componente celular de interés (propiedad: prefLabel) disponible en el grafo **http://rdf.biogateway.eu/graph/prot2mf .**

**-”database”:** Indica la base de datos donde se encuentra registrada la información sobre la relación entre la proteína y el componente celular de interés (propiedad: SIO\_000253 (has source)).

**-”articles”:** Corresponde a artículos científicos o publicaciones que están asociadas con la relación entre la proteína y el componente celular de interés, que se encuentran en la base de datos Pubmed (propiedad: SIO\_000772 (has evidence)).

**Ejemplo de ejecución:**

Entrada: cc2prot("GO:0034703","9606")

Salida:

[{'protein\_name': 'TRPC3\_HUMAN',

`  `'relation\_label': 'Q13507--GO:0034703',

`  `'database': 'goa/',

`  `'articles': 'pubmed/21873635'},

` `{'protein\_name': 'PKD2\_HUMAN',

`  `'relation\_label': 'Q13563--GO:0034703',

`  `'database': 'goa/',

`  `'articles': 'pubmed/30093605'},

` `{'protein\_name': 'UNC80\_HUMAN',

`  `'relation\_label': 'Q8N2C7--GO:0034703',

`  `'database': 'goa/',

`  `'articles': 'pubmed/21873635'},

` `{'protein\_name': 'TRPC6\_HUMAN',

`  `'relation\_label': 'Q9Y210--GO:0034703',

`  `'database': 'goa/',

`  `'articles': 'pubmed/21873635'},

` `{'protein\_name': 'PKD1\_HUMAN',

`  `'relation\_label': 'P98161--GO:0034703',

`  `'database': 'goa/',

`  `'articles': 'pubmed/30093605'}]


**Tabla resumen:**

|Variable|Rol|Tipo|Descripción|Propiedad de la Ontología|Grafo|
| :- | :- | :- | :- | :- | :- |
|**“cellular\_component”**|**entrada**|**string**|**Identificador en Gene Ontology o nombre del componente**|<p>**obo:RO\_0002331**</p><p>**(involved in )**</p>|**prot2cc**|
|**“taxon”**|**entrada (opcional)**|**string**|**Número de taxón o nombre del organismo**|<p>**obo:RO\_0002162**</p><p>**(in taxon)**</p>|**prot**|
|**“protein\_name”**|**salida**|**string**|**Nombre de la proteína relacionada con el componente celular en formato entry name de Uniprot** |<p>**obo:RO\_0002331**</p><p>**(involved in )**</p>|**prot2cc**|
|**“relation\_label”**|**salida**|**string**|**Etiqueta que presenta la relación entre la proteína y el componente celular de interés**|**skos:prefLabel**|**prot2cc**|
|**“database”**|**salida**|**string**|**Base de datos con la información sobre la relación**|<p>**sio:SIO\_0000253**</p><p>**(has source)**</p>|**prot2cc**|
|**“articles”**|**salida**|**string**|**Artículos asociados a la relación**|<p>**sio:SIO\_0000772**</p><p>**(has evidence)**</p>|**prot2cc**|

# <a name="_6azuc8d8l0s2"></a>**Función prot2mf(protein)**

**Descripción:** Esta función permite estudiar las funciones moleculares en las que participa la proteína de interés, explotando la información del grafo **http://rdf.biogateway.eu/graph/prot2mf**

**Parámetros:**

**-“protein”:** Insertamos el nombre de la proteína tanto en formato entry name de Uniprot (propiedad: prefLabel) como en formato entry de Uniprot (propiedad: altLabel). Ejemplo: “BRCA1\_HUMAN”, “P38398”.

**Salida:**

La función devuelve una lista con las funciones moleculares relacionadas con la proteína seleccionada. Presenta los siguientes campos:

**-”mf\_id”:** Corresponde al identificador de la función molecular en Gene Ontology (propiedad: oboInOwl#id) de las funciones moleculares relacionadas con la proteína de interés (propiedad:RO\_0002327 (enables)) . Ejemplo: “GO:0004672”

**-”mf\_label”:** Se refiere a la etiqueta de la función molecular en el grafo de conocimiento **http://rdf.biogateway.eu/graph/go** (propiedad: label). Ejemplo: "protein kinase activity"

**-”relation\_label”:** Hace referencia a la etiqueta que presenta la relación entre la función molecular y la proteína de interés (propiedad: prefLabel) disponible en el grafo **http://rdf.biogateway.eu/graph/prot2mf .**

**-”database”:** Indica la base de datos donde se encuentra registrada la información sobre la relación entre la función molecular y la proteína de interés (propiedad: SIO\_000253 (has source)).

**-”articles”:** Corresponde a artículos científicos o publicaciones que están asociadas con la relación entre la función molecular y la proteína de interés, que se encuentran en la base de datos Pubmed (propiedad: SIO\_000772 (has evidence)).

**Ejemplo de ejecución:**

Entrada: prot2mf("BRCA1\_HUMAN")

Salida:

{'mf\_id': 'GO:0002039',

`  `'mf\_label': 'p53 binding',

`  `'relation\_label': 'P38398--GO:0002039',

`  `'database': 'goa/',

`  `'articles': 'pubmed/15571721'},

` `{'mf\_id': 'GO:0003677',

`  `'mf\_label': 'DNA binding',

`  `'relation\_label': 'P38398--GO:0003677',

`  `'database': 'goa/',

`  `'articles': 'pubmed/9662397'},

` `{'mf\_id': 'GO:0003713',

`  `'mf\_label': 'transcription coactivator activity',

`  `'relation\_label': 'P38398--GO:0003713',

`  `'database': 'goa/',

`  `'articles': 'pubmed/9662397'},

` `{'mf\_id': 'GO:0003723',

`  `'mf\_label': 'RNA binding',

`  `'relation\_label': 'P38398--GO:0003723',

`  `'database': 'goa/',

`  `'articles': 'pubmed/12419249'},

` `{'mf\_id': 'GO:0004842',

`  `'mf\_label': 'ubiquitin-protein transferase activity',

`  `'relation\_label': 'P38398--GO:0004842',

`  `'database': 'goa/',

`  `'articles': 'pubmed/20351172; pubmed/21873635; pubmed/17349954; pubmed/19117993; pubmed/12890688'}]


**Tabla resumen:**

|Variable|Rol|Tipo|Descripción|Propiedad de la Ontología|Grafo|
| :- | :- | :- | :- | :- | :- |
|**“protein”**|**entrada**|**string**|**Nombre de la proteína en formato entry name** |<p>**obo:RO\_0002331**</p><p>**(involved in )**</p>|**prot2mf**|
|**“mf\_id”**|**salida**|**string**|**Identificador en Gene Ontology de la función molecular relacionada con la proteína de interés** |<p>**obo:RO\_0002331**</p><p>**(involved in)**</p>|**prot2mf**|
|**“mf\_label”**|**salida**|**string**|**Etiqueta la función molecular en el grafo** |**skos:label**|**go**|
|**“relation\_label”**|**salida**|**string**|**Etiqueta que presenta la relación entre la proteína y la función molecular de interés**|**skos:prefLabel**|**prot2mf**|
|**“database”**|**salida**|**string**|**Base de datos con la información sobre la relación**|<p>**sio:SIO\_0000253**</p><p>**(has source)**</p>|**prot2mf**|
|**“articles”**|**salida**|**string**|**Artículos asociados a la relación**|<p>**sio:SIO\_0000772**</p><p>**(has evidence)**</p>|**prot2mf**|



# <a name="_zdz4hzwnvr8n"></a>**Función mf2prot(molecular\_function,taxon)**

**Descripción:** Esta función devuelve las proteínas relacionadas con la función molecular especificada explotando la información del grafo **http://rdf.biogateway.eu/graph/prot2mf**




**Parámetros:**

**-”molecular\_function”**: Este parámetro es la función molecular de interés, los valores permitidos son: su identificador en Gene Ontology (Ejemplo: “GO:0004672”) o el nombre del componente celular (Ejemplo: “protein kinase activity”).

-**”taxon”:** Permite seleccionar el taxón en el que se quiere realizar la consulta. El valor puede ser el** identificador taxonómico del NCBI o el nombre del organismo (propiedad: label). Ejemplo: “Homo sapiens”, “9606”. Si el valor del taxon es **None**, aplicará la búsqueda con todos los taxones disponibles en el grafo de conocimiento.


**Salida:**

La función devuelve una lista con las proteínas relacionadas con la función molecular de interés. Presenta los siguientes campos:

-”**protein\_name**”: Son los nombres en formato entry name de Uniprot (prefLabel) de las proteínas relacionadas con el componente celular de interés (propiedad:RO\_0002327).

**-”relation\_label”:** Hace referencia a la etiqueta que presenta la relación entre la proteína y la función molecular de interés (propiedad: prefLabel) disponible en el grafo **http://rdf.biogateway.eu/graph/prot2mf .**

**-”database”:** Indica la base de datos donde se encuentra registrada la información sobre la relación entre la proteína y la función molecular de interés (propiedad: SIO\_000253 (has source)).

**-”articles”:** Corresponde a artículos científicos o publicaciones que están asociadas con la relación entre la proteína y la función molecular de interés, que se encuentran en la base de datos Pubmed (propiedad: SIO\_000772 (has evidence)).

**Ejemplo de ejecución:**

Entrada: mf2prot("protein binding","9606")

Salida: 

[{'protein\_name': 'ZN217\_HUMAN',

`  `'relation\_label': 'O75362--GO:0005515',

`  `'database': 'goa/',

`  `'articles': 'pubmed/16940172'},

` `{'protein\_name': 'SIR6\_HUMAN',

`  `'relation\_label': 'Q8N6T7--GO:0005515',

`  `'database': 'goa/',

`  `'articles': 'pubmed/19135889; pubmed/23217706; pubmed/23911928'},

` `{'protein\_name': 'NELFE\_HUMAN',

`  `'relation\_label': 'P18615--GO:0005515',

`  `'database': 'goa/',

`  `'articles': 'pubmed/32296183; pubmed/26496610; pubmed/14667819; pubmed/28514442; pubmed/25416956; pubmed/24981860; pubmed/12612062; pubmed/20211142'}]

**Tabla resumen:**



|Variable|Rol|Tipo|Descripción|Propiedad de la Ontología|Grafo|
| :- | :- | :- | :- | :- | :- |
|**“molecular\_function”**|**entrada**|**string**|**Identificador en Gene Ontology o nombre de la función molecular**|<p>**obo:RO\_0002331**</p><p>**(involved in )**</p>|**prot2mf**|
|**“taxon”**|**entrada (opcional)**|**string**|**Número de taxón o nombre del organismo**|<p>**obo:RO\_0002162**</p><p>**(in taxon)**</p>|**prot**|
|**“protein\_name”**|**salida**|**string**|**Nombre de la proteína relacionada con la función molecular en formato entry name de Uniprot** |<p>**obo:RO\_0002331**</p><p>**(involved in )**</p>|**prot2mf**|
|**“relation\_label”**|**salida**|**string**|**Etiqueta que presenta la relación entre la proteína y la función molecular de interés**|**skos:prefLabel**|**prot2mf**|
|**“database”**|**salida**|**string**|**Base de datos con la información sobre la relación**|<p>**sio:SIO\_0000253**</p><p>**(has source)**</p>|**prot2mf**|
|**“articles”**|**salida**|**string**|**Artículos asociados a la relación**|<p>**sio:SIO\_0000772**</p><p>**(has evidence)**</p>|**prot2mf**|

# <a name="_xg3bowwf2g4h"></a>**Función gene2crm(gene)**
**Descripción:** Esta función nos permite obtener los crms asociados al gen introducido como parámetro. Para ello usaremos la información del grafo **http://rdf.biogateway.eu/graph/crm2gene .**

**Parámetros:**

**-”gene”:** Este parámetro corresponde al nombre del gen en formato symbol (propiedad: prefLabel). Ejemplo: “TOX3”.

**Salida:**

La función devuelve un diccionario con los crms que están relacionados con el gen introducido. Presenta los siguientes campos:

**-”crm\_name”:** Nombre del módulo cis-regulador (propiedad: prefLabel) que está relacionado con el gen introducido (propiedad: RO\_0002429). 

**-”database”:** Indica la base de datos donde se encuentra registrada la información sobre la relación entre el crm y el gen de interés (propiedad: SIO\_000253 (has source)).

**-”articles”:** Corresponde a artículos científicos o publicaciones que están asociadas con la relación entre el crm y el gen de interés, que se encuentran en la base de datos Pubmed (propiedad: SIO\_000772 (has evidence)).

**Ejemplo de ejecución:**

Entrada: gene2crm("TOX3")

Salida:

[{'crm\_name': 'crm/CRMHS00000005857',

`  `'database': '<http://lcbb.swjtu.edu.cn/EnhFFL/>;[ ](http://218.8.241.248:8080/SEA3/)<http://218.8.241.248:8080/SEA3/>;[ ](http://bioinfo.vanderbilt.edu/AE/HACER)<http://bioinfo.vanderbilt.edu/AE/HACER>;[ ](https://genome.ucsc.edu/cgi-bin/hgTrackUi?db=hg38&g=geneHancer)<https://genome.ucsc.edu/cgi-bin/hgTrackUi?db=hg38&g=geneHancer>;[ ](http://enhanceratlas.net/scenhancer/)<http://enhanceratlas.net/scenhancer/>;[ ](https://webs.iiitd.edu.in/raghava/cancerend/)<https://webs.iiitd.edu.in/raghava/cancerend/>;[ ](https://enhancer.lbl.gov/)<https://enhancer.lbl.gov/>;[ ](http://www.licpathway.net/sedb/)<http://www.licpathway.net/sedb/>;[ ](http://health.tsinghua.edu.cn/jianglab/endisease/)<http://health.tsinghua.edu.cn/jianglab/endisease/>;[ ](http://biocc.hrbmu.edu.cn/DiseaseEnhancer/)<http://biocc.hrbmu.edu.cn/DiseaseEnhancer/>;[ ](https://fantom.gsc.riken.jp/5/)<https://fantom.gsc.riken.jp/5/>;[ ](http://acgt.cs.tau.ac.il/focs/)<http://acgt.cs.tau.ac.il/focs/>;[ ](https://asntech.org/dbsuper/)<https://asntech.org/dbsuper/>;[ ](http://yiplab.cse.cuhk.edu.hk/jeme/)<http://yiplab.cse.cuhk.edu.hk/jeme/>',

`  `'articles': 'pubmed/24119843; pubmed/28869592; pubmed/30247654; pubmed/23374354; pubmed/29716618; pubmed/23001124; pubmed/35694152; pubmed/24670763; pubmed/32360910; pubmed/17130149; pubmed/30371817; pubmed/28605766; pubmed/34761274; pubmed/31667506'}

**Tabla resumen:** 




|Variable|Rol|Tipo|Descripción|Propiedad de la Ontología|Grafo|
| :- | :- | :- | :- | :- | :- |
|**“gene”**|**entrada**|**string**|**Nombre del gen en formato symbol**|<p>**obo:RO\_0002429**</p><p>**(involved in positive regulation of )**</p>|**crm2gene**|
|**“crm\_name”**|**salida**|**string** |**Nombre del módulo cis-regulador relacionado con el gen introducido**|<p>**obo:RO\_0002429**</p><p>**(involved in positive regulation of )**</p>|**crm2gene**|
|**“database”**|**salida**|**string**|**Base de datos con la información sobre la relación entre el crm y el gen.**|<p>**sio:SIO\_0000253**</p><p>**(has source)**</p>|**crm2gene**|
|**“articles”**|**salida**|**string**|**Artículos asociados a la relación**|<p>**sio:SIO\_0000772**</p><p>**(has evidence)**</p>|**crm2gene**|

#
# <a name="_c2grywafq4pl"></a><a name="_ha8n7x4sywwa"></a>**Función crm2gene(crm)**

**Descripción:** Esta función facilita la obtención de los genes a los que un crm específico afecta. Para ello usaremos la información del grafo **http://rdf.biogateway.eu/graph/crm2gene .**

**Parámetros:**

-**”crm”**: El parámetro introducido en la función será el identificador preferente del módulo cis-regulador (propiedad: prefLabel). Ejemplo "crm/CRMHS00003225754".

**Salida:**

La función devuelve un diccionario con los genes que están relacionados con el crm de interés. Presenta los siguientes campos:

-”**gene\_name**”: La función devuelve una lista con los nombres en formato symbol (porpiedad: prefLabel) de los genes relacionados con el crm de interés (propiedad:RO\_0002429).

**-”database”:** Indica la base de datos donde se encuentra registrada la información sobre la relación entre el gen y el crm de interés (propiedad: SIO\_000253 (has source)).

**-”articles”:** Corresponde a artículos científicos o publicaciones que están asociadas con la relación entre el gen y el crm de interés, que se encuentran en la base de datos Pubmed (propiedad: SIO\_000772 (has evidence)).

**Ejemplo de ejecución:**

Entrada: crm2gene("crm/CRMHS00000137026")

Salida:

[{'gene\_name': 'CRAT',

`  `'database': '<http://bioinfo.vanderbilt.edu/AE/HACER>;[ ](https://fantom.gsc.riken.jp/5/)<https://fantom.gsc.riken.jp/5/>;[ ](https://webs.iiitd.edu.in/raghava/cancerend/)<https://webs.iiitd.edu.in/raghava/cancerend/>;[ ](http://yiplab.cse.cuhk.edu.hk/jeme/)<http://yiplab.cse.cuhk.edu.hk/jeme/>',

`  `'articles': 'pubmed/24670763; pubmed/32360910; pubmed/28869592; pubmed/30247654'},

` `{'gene\_name': 'NTMT1',

`  `'database': '<http://bioinfo.vanderbilt.edu/AE/HACER>;[ ](https://fantom.gsc.riken.jp/5/)<https://fantom.gsc.riken.jp/5/>;[ ](https://webs.iiitd.edu.in/raghava/cancerend/)<https://webs.iiitd.edu.in/raghava/cancerend/>;[ ](http://yiplab.cse.cuhk.edu.hk/jeme/)<http://yiplab.cse.cuhk.edu.hk/jeme/>',

`  `'articles': 'pubmed/24670763; pubmed/32360910; pubmed/28869592; pubmed/30247654'},

` `{'gene\_name': 'PTPA',

`  `'database': '<http://bioinfo.vanderbilt.edu/AE/HACER>;[ ](https://fantom.gsc.riken.jp/5/)<https://fantom.gsc.riken.jp/5/>;[ ](https://webs.iiitd.edu.in/raghava/cancerend/)<https://webs.iiitd.edu.in/raghava/cancerend/>;[ ](http://yiplab.cse.cuhk.edu.hk/jeme/)<http://yiplab.cse.cuhk.edu.hk/jeme/>',

`  `'articles': 'pubmed/24670763; pubmed/32360910; pubmed/28869592; pubmed/30247654'

**Tabla resumen:**




|Variable|Rol|Tipo|Descripción|Propiedad de la Ontología|Grafo|
| :- | :- | :- | :- | :- | :- |
|**“crm”**|**entrada**|**string**|<p>**Nombre del módulo cis-regulador**</p><p>**Nombre del gen en formato symbol**</p>|<p>**obo:RO\_0002429**</p><p>**(involved in positive regulation of )**</p>|**crm2gene**|
|**“gene\_name”**|**salida**|**string** |**Nombre del gen en formato symbol relacionado con el crm**|<p>**obo:RO\_0002429**</p><p>**(involved in positive regulation of )**</p>|**crm2gene**|
|**“database”**|**salida**|**string**|**Base de datos con la información sobre la relación entre el crm y el gen**|<p>**sio:SIO\_0000253**</p><p>**(has source)**</p>|**crm2gene**|
|**“articles”**|**salida**|**string**|**Artículos asociados a la relación**|<p>**sio:SIO\_0000772**</p><p>**(has evidence)**</p>|**crm2gene**|

# <a name="_fazt4ulbk0ur"></a>**Función tfac2crm(tfac)**
**Descripción:** La función posibilita la obtención de los crms asociados a un factor de transcripción específico, información que encontramos en el grafo **http://rdf.biogateway.eu/graph/crm2tfac**

**Parámetros:**

**-“tfac”:** Este parámetro corresponde al nombre en formato entry name de Uniprot del factor de transcripción del cual queremos conocer con qué crms interactúa.


**Salida:**

La función devuelve un diccionario con los crms que están relacionados con el factor de transcripción introducido. Presenta los siguientes campos:

**-”crm\_name”:** Nombre de los módulos cis-reguladores ((propiedad: prefLabel)) con los que interactúa el factor de transcripción especificado  (propiedad:RO\_0002436). 

**-”database”:** Indica la base de datos donde se encuentra registrada la información sobre la relación entre el crm y el factor de transcripción(propiedad: SIO\_000253 (has source)).

**-”articles”:** Corresponde a artículos científicos o publicaciones que están asociadas con la relación entre el crm y el factor de transcripción de interés, que se encuentran en la base de datos Pubmed (propiedad: SIO\_000772 (has evidence)).

**-“evidence”:** Corresponde a la evidencia que respalda la información disponible sobre la relación entre el factor de transcripción y el crm (propiedad: evidenceOrigin).

**-”biological\_samples”:** Se refiere a los diferentes tipos de muestras biológicas que están asociados con el estudio de la relación entre el módulo cis-regulador y el factor de transcripción (propiedad: TXPO\_0003500 (observed in)). En concreto, devolverá los identificadores en formato de términos ontológicos. Ejemplo: “CLO\_0001601”, “UBERON\_0002113”, “BTO\_0000018”.

**Ejemplo de ejecución:**

Entrada: tfac2crm("FOSL2\_HUMAN")

Salida: 

[{'crm\_name': 'crm/CRMHS00000005425',

`  `'database': '<http://www.licpathway.net/ENdb/>',

`  `'articles': 'pubmed/29149598',

'evidence': '<http://www.licpathway.net/ENdb/search/Detail.php?Species=Human&Enhancer_id=E_01_292>',

`  `'biological\_samples': 'UBERON\_0001003; CL\_0000148'},

` `{'crm\_name': 'crm/CRMHS00000006865',

`  `'database': '<http://lcbb.swjtu.edu.cn/EnhFFL/>',

`  `'articles': 'pubmed/35694152',

'evidence': '<http://lcbb.swjtu.edu.cn/EnhFFL/details/?term=enH639113&subtype=enhancer&species=human>',

`  `'biological\_samples': 'CL\_0002319; UBERON\_0002421; BTO\_0000601'},

` `{'crm\_name': 'crm/CRMHS00000006866',

`  `'database': '<http://lcbb.swjtu.edu.cn/EnhFFL/>',

`  `'articles': 'pubmed/35694152',

‘evidence': '<http://lcbb.swjtu.edu.cn/EnhFFL/details/?term=enH594653&subtype=enhancer&species=human>',

`  `'biological\_samples': 'CL\_0002319; UBERON\_0002421; BTO\_0000601'}]

**Tabla resumen:**

|Variable|Rol|Tipo|Descripción|Propiedad de la Ontología|Grafo|
| :- | :- | :- | :- | :- | :- |
|**“tfac”**|**entrada**|**string**|**Nombre del del factor de transcripción en formato entry name de Uniprot**|<p>**obo:RO\_0002436**</p><p>**(molecularly interacts with)**</p>|**crm2tfac**|
|**“crm\_name”**|**salida**|**string** |**Nombre del módulo cis-regulador relacionado con el factor de transcripción introducido**|<p>**obo:RO\_0002436**</p><p>**(molecularly interacts with)**</p>|**crm2tfac**|
|**“database”**|**salida**|**string**|**Base de datos con la información sobre la relación entre el crm y el tfac.**|<p>**sio:SIO\_0000253**</p><p>**(has source)**</p>|**crm2tfac**|
|**“articles”**|**salida**|**string**|**Artículos asociados a la relación**|<p>**sio:SIO\_0000772**</p><p>**(has evidence)**</p>|**crm2tfac**|
|**”evidence”**|**salida**|**string**|**Nivel de evidencia asociado la relación**|**sch:evidenceOrigin**|**crm2tfac**|
|**“biological\_samples”**|**salida**|**string**|**Muestras biológicas asociadas a la relación**|**obo:TXPO\_0003500 (observed in)**|**crm2tfac**|


# <a name="_ahdi8dw08hkc"></a>**Función crm2tfac(crm)**
**Descripción:** Esta función permite estudiar los factores de transcripción que interactúan con un crm determinado, usando la información del grafo **http://rdf.biogateway.eu/graph/crm2tfac.**

**Parámetros:**

-**”crm”**: El parámetro introducido en la función será el identificador preferente del módulo cis-regulador (propiedad: prefLabel). Ejemplo "crm/CRMHS00000007832".

**Salida:**

La función devuelve un diccionario con los factores de transcripción que están relacionados con el crm de interés. Presenta los siguientes campos:

**-“tfac\_name”:** Nombres en formato entry name de Uniprot de los factores de transcripción que interactúan con el crm de interés. Ejemplo: “TF7L2\_HUMAN”.

**-”database”:** Indica la base de datos donde se encuentra registrada la información sobre la relación entre el factor de transcripción y el crm de interés (propiedad: SIO\_000253 (has source)).

**-”articles”:** Corresponde a artículos científicos o publicaciones que están asociadas con la relación entre el factor de transcripción y el crm de interés, que se encuentran en la base de datos Pubmed (propiedad: SIO\_000772 (has evidence)).

**-“evidence”:** Corresponde a la evidencia que respalda la información disponible sobre la relación entre el factor de transcripción y el crm de interés(propiedad: evidenceOrigin).

**-”biological\_samples”:** Se refiere a los diferentes tipos de muestras biológicas que están asociados con el estudio de la relación entre el factor de transcripción y el crm introducido (propiedad: TXPO\_0003500 (observed in)). En concreto, devolverá los identificadores en formato de términos ontológicos. Ejemplo: “CLO\_0001601”, “UBERON\_0002113”, “BTO\_0000018”.

**Ejemplo de ejecución:**

Entrada: crm2tfac("crm/CRMHS00000007832")

Salida: 

[{'tfac\_name': 'RAD21\_HUMAN',

`  `'database': '<http://lcbb.swjtu.edu.cn/EnhFFL/>',

`  `'articles': 'pubmed/35694152',

'evidence': '<http://lcbb.swjtu.edu.cn/EnhFFL/details/?term=enH58066&subtype=enhancer&species=human>',

`  `'biological\_samples': 'UBERON\_0005090; CL\_0000187; BTO\_0000887'},

` `{'tfac\_name': 'SRF\_HUMAN',

`  `'database': '<http://lcbb.swjtu.edu.cn/EnhFFL/>',

`  `'articles': 'pubmed/35694152',

'evidence': '<http://lcbb.swjtu.edu.cn/EnhFFL/details/?term=enH58066&subtype=enhancer&species=human>',

`  `'biological\_samples': 'UBERON\_0005090; CL\_0000187; BTO\_0000887'},

` `{'tfac\_name': 'TAF1\_HUMAN',

`  `'database': '<http://lcbb.swjtu.edu.cn/EnhFFL/>',

`  `'articles': 'pubmed/35694152',

'evidence': '<http://lcbb.swjtu.edu.cn/EnhFFL/details/?term=enH58066&subtype=enhancer&species=human>',

`  `'biological\_samples': 'UBERON\_0005090; CL\_0000187; BTO\_0000887'},

` `{'tfac\_name': 'RPB1\_HUMAN',

`  `'database': '<http://lcbb.swjtu.edu.cn/EnhFFL/>',

`  `'articles': 'pubmed/35694152',

'evidence': '<http://lcbb.swjtu.edu.cn/EnhFFL/details/?term=enH58066&subtype=enhancer&species=human>',

`  `'biological\_samples': 'UBERON\_0005090; CL\_0000187; BTO\_0000887'}]

**Tabla resumen:**

|Variable|Rol|Tipo|Descripción|Propiedad de la Ontología|Grafo|
| :- | :- | :- | :- | :- | :- |
|**“crm”**|**entrada**|**string** |**Nombre del módulo cis-regulador** |<p>**obo:RO\_0002436**</p><p>**(molecularly interacts with)**</p>|**crm2tfac**|
|**“tfac\_name”**|**salida**|**string**|**Nombre del del factor de transcripción en formato entry name de Uniprot relacionado con el crm introducido**|<p>**obo:RO\_0002436**</p><p>**(molecularly interacts with)**</p>|**crm2tfac**|
|**“database”**|**salida**|**string**|**Base de datos con la información sobre la relación entre el crm y el tfac.**|<p>**sio:SIO\_0000253**</p><p>**(has source)**</p>|**crm2tfac**|
|**“articles”**|**salida**|**string**|**Artículos asociados a la relación**|<p>**sio:SIO\_0000772**</p><p>**(has evidence)**</p>|**crm2tfac**|
|**”evidence”**|**salida**|**string**|**Nivel de evidencia asociado la relación**|**sch:evidenceOrigin**|**crm2tfac**|
|**“biological\_samples”**|**salida**|**string**|**Muestras biológicas asociadas a la relación**|**obo:TXPO\_0003500 (observed in)**|**crm2tfac**|

# <a name="_tyfrxgueml04"></a>**Función crm2phen(crm)**
**Descripción:** Esta función posibilita la obtención de los fenotipos asociados a un crm previamente introducido como parámetro de esta función. Para ello explotaremos el grafo **http://rdf.biogateway.eu/graph/crm2phen.**

**Parámetros:**

-**”crm”**: El parámetro introducido en la función será el identificador preferente del módulo cis-regulador (propiedad: prefLabel). Ejemplo ""crm/CRMHS00000005764"".

**Salida:**

La función devuelve un diccionario con los fenotipos relacionados con el crm seleccionado. Asimismo, presenta los siguientes campos:

**-”phen\_id”:** Corresponde a los identificadores de los fenotipos asociados al crm de interés, en concreto puede devolver tanto el identificador OMIM, como el identificador DOID como el identificador MeSH.

**-”database”:** Indica la base de datos donde se encuentra registrada la información sobre la relación entre el fenotipo y el crm de interés (propiedad: SIO\_000253 (has source)).

**-”articles”:** Corresponde a artículos científicos o publicaciones que están asociadas con la relación entre el fenotipo y el crm de interés, que se encuentran en la base de datos Pubmed (propiedad: SIO\_000772 (has evidence)).


**Ejemplo de ejecución:**

Entrada: crm2phen("crm/CRMHS00000005764")

Salida:

[{'phen\_id': 'OMIM/181500',

'database':'<http://biocc.hrbmu.edu.cn/DiseaseEnhancer/>;[ ](http://health.tsinghua.edu.cn/jianglab/endisease/)<http://health.tsinghua.edu.cn/jianglab/endisease/>',

`  `'articles': 'pubmed/25453756'},

` `{'phen\_id': 'MESH/D012559',

'database':'<http://biocc.hrbmu.edu.cn/DiseaseEnhancer/>;[ ](http://health.tsinghua.edu.cn/jianglab/endisease/)<http://health.tsinghua.edu.cn/jianglab/endisease/>',

`  `'articles': 'pubmed/25453756'},

` `{'phen\_id': 'DOID/DOID\_5419',

'database':'<http://biocc.hrbmu.edu.cn/DiseaseEnhancer/>;[ ](http://health.tsinghua.edu.cn/jianglab/endisease/)<http://health.tsinghua.edu.cn/jianglab/endisease/>',

`  `'articles': 'pubmed/25453756'}]

**Tabla resumen:**

|Variable|Rol|Tipo|Descripción|Propiedad de la Ontología|Grafo|
| :- | :- | :- | :- | :- | :- |
|**“crm”**|**entrada**|**string**|<p>**Nombre del módulo cis-regulador**</p><p>**Nombre del gen en formato symbol**</p>|**obo:RO\_0002331 (involved in )**|**crm2phen**|
|**“phen\_id”**|**salida**|**string** |**Identificador de los fenotipos asociados al crm de interés**|**obo:RO\_0002331 (involved in )**|**crm2phen**|
|**“database”**|**salida**|**string**|**Base de datos con la información sobre la relación entre el crm y el fenotipo**|<p>**sio:SIO\_0000253**</p><p>**(has source)**</p>|**crm2phen**|
|**“articles”**|**salida**|**string**|**Artículos asociados a la relación**|<p>**sio:SIO\_0000772**</p><p>**(has evidence)**</p>|**crm2phen**|

# <a name="_uesege7br1rv"></a>**Función phen2crm(phenotype)**
**Descripción:** Esta función devuelve los crms que están asociados a un fenotipo determinado. Explota la información disponible en el grafo **http://rdf.biogateway.eu/graph/crm2phen.**

**Parámetros:**

-**”phenotype”**: Este parámetro corresponde al fenotipo de interés. Se permite tanto su identificador OMIM (“181500”), como el nombre de una enfermedad(“schizophrenia”).

**Salida:**

La función devuelve un diccionario con los crms que están relacionados con el fenotipo especificado. Presenta los siguientes campos:

**-”crm\_name”:** Nombre de los módulos cis-reguladores ((propiedad: prefLabel)) asociados al fenotipo introducido (propiedad: RO\_0002331 (involved in)).



-”**omim\_id**”: Corresponde al identificador OMIM del fenotipo que está asociado al crm (solo si se ha introducido el nombre de un fenotipo).

**-”database”:** Indica la base de datos donde se encuentra registrada la información sobre la relación entre el crm y el fenotipo especificado (propiedad: SIO\_000253 (has source)).

**-”articles”:** Corresponde a artículos científicos o publicaciones que están asociadas con la relación entre el crm y el fenotipo de interés, que se encuentran en la base de datos Pubmed (propiedad: SIO\_000772 (has evidence)).

**Ejemplo de ejecución:**

Entrada: phen2crm("schizophrenia")

Salida: 

[{'crm\_name': 'crm/CRMHS00000005764',

`  `'omim\_id': 'OMIM/181500',

'database':'<http://biocc.hrbmu.edu.cn/DiseaseEnhancer/>;[ ](http://health.tsinghua.edu.cn/jianglab/endisease/)<http://health.tsinghua.edu.cn/jianglab/endisease/>',

`  `'articles': 'pubmed/25453756'},

` `{'crm\_name': 'crm/CRMHS00000005770',

`  `'omim\_id': 'OMIM/181500',

'database':'<http://biocc.hrbmu.edu.cn/DiseaseEnhancer/>;[ ](http://health.tsinghua.edu.cn/jianglab/endisease/)<http://health.tsinghua.edu.cn/jianglab/endisease/>',

`  `'articles': 'pubmed/25453756'},

` `{'crm\_name': 'crm/CRMHS00000005771',

`  `'omim\_id': 'OMIM/181500',

'database':'<http://biocc.hrbmu.edu.cn/DiseaseEnhancer/>;[ ](http://health.tsinghua.edu.cn/jianglab/endisease/)<http://health.tsinghua.edu.cn/jianglab/endisease/>',

`  `'articles': 'pubmed/25434007'},

` `{'crm\_name': 'crm/CRMHS00000005773',

`  `'omim\_id': 'OMIM/181500',

'database':'<http://biocc.hrbmu.edu.cn/DiseaseEnhancer/>;[ ](http://health.tsinghua.edu.cn/jianglab/endisease/)<http://health.tsinghua.edu.cn/jianglab/endisease/>',

`  `'articles': 'pubmed/25453756'},

` `{'crm\_name': 'crm/CRMHS00000005816',

`  `'omim\_id': 'OMIM/181500',

'database':'<http://biocc.hrbmu.edu.cn/DiseaseEnhancer/>;[ ](http://health.tsinghua.edu.cn/jianglab/endisease/)<http://health.tsinghua.edu.cn/jianglab/endisease/>',

`  `'articles': 'pubmed/27276213; pubmed/25453756'}]



**Tabla resumen:**

|Variable|Rol|Tipo|Descripción|Propiedad de la Ontología|Grafo|
| :- | :- | :- | :- | :- | :- |
|**“phenotype”**|**entrada**|**string**|**Identificador OMIM o nombre del fenotipo de interés**|**obo:RO\_0002331 (involved in )**|**crm2phen**|
|**“crm\_name”**|**salida**|**string** |**Nombre del módulo cis-regulador relacionado con el fenotipo introducido**|**obo:RO\_0002331 (involved in )**|**crm2phen**|
|**“omim\_id”**|<p>**salida**</p><p>**(opcional)**</p>|**string**|**Identificador OMIM del fenotipo asociado al crm**|**obo:RO\_0002331 (involved in )**|**crm2phen**|
|**“database”**|**salida**|**string**|**Base de datos con la información sobre la relación entre el crm y el fenotipo**|<p>**sio:SIO\_0000253**</p><p>**(has source)**</p>|**crm2phen**|
|**“articles”**|**salida**|**string**|**Artículos asociados a la relación**|<p>**sio:SIO\_0000772**</p><p>**(has evidence)**</p>|**crm2phen**|

# <a name="_l3wapw3ov1de"></a>**Función tfac2gene(tfac)**
**Descripción:** Esta función  permite obtener los genes que son regulados por un factor de transcripción determinado, gracias a la información proporcionada por el grafo **http://rdf.biogateway.eu/graph/tfac2gene.**

**Parámetros:**

**-“tfac”:** Este parámetro corresponde al nombre en formato entry name de Uniprot del factor de transcripción del cual queremos conocer a qué genes regula. Ejemplo: "NKX31\_HUMAN". 

**Salida:**

La función devuelve dos diccionarios con los genes que son regulados positiva y negativamente por el factor de transcripción introducido. Presenta los siguientes campos:

**-”gene\_name”:** Nombre en formato symbol de los genes ((propiedad: prefLabel)) que son regulados por el factor de transcripción especificado  (propiedad: RO\_0002429 (involved in positive regulation of) y propiedad: RO\_0002430  (involved in negative regulation of)). 

**-”database”:** Indica la base de datos donde se encuentra registrada la información sobre la relación entre el geny el factor de transcripción(propiedad: SIO\_000253 (has source)).

**-”articles”:** Corresponde a artículos científicos o publicaciones que están asociadas con la relación entre el gen y el factor de transcripción de interés, que se encuentran en la base de datos Pubmed (propiedad: SIO\_000772 (has evidence)).

**-“evidence\_level”:** Corresponde a la evidencia que respalda la información disponible sobre la relación entre el factor de transcripción y el gen (propiedad: evidenceOrigin).

**-”definition”**: Proporciona la definición de la relación que se produce entre cada gen y el factor de transcripción especificado (propiedad: definition), disponible en el propio grafo (**http://rdf.biogateway.eu/graph/tfac2gene**).

**Ejemplo de ejecución:**

Entrada: tfac2gene("NKX31\_HUMAN")

Salida:

'Positive regulation results:',

` `[{'gene\_name': 'CLIC4',

`   `'database': '<https://github.com/saezlab/CollecTRI>',

`   `'articles': 'pubmed/16316993',

`   `'evidence\_level': '1',

`   `'definition': 'Q99801 involved in positive regulation of 9606/CLIC4'},

`  `{'gene\_name': 'DKK3',

`   `'database': '<https://github.com/saezlab/CollecTRI>',

`   `'articles': 'pubmed/23975733',

`   `'evidence\_level': '1',

`   `'definition': 'Q99801 involved in positive regulation of 9606/DKK3'},

`  `{'gene\_name': 'MAP3K5',

`   `'database': '<https://github.com/saezlab/CollecTRI>',

`   `'articles': 'pubmed/21594902',

`   `'evidence\_level': '1',

`   `'definition': 'Q99801 involved in positive regulation of 9606/MAP3K5'},

`  `{'gene\_name': 'NKX3-1',

`   `'database': '<https://github.com/saezlab/CollecTRI>',

`   `'articles': 'pubmed/15880262; pubmed/20855495; pubmed/19886863; pubmed/20195545; pubmed/23368843; pubmed/16270157; pubmed/19263243; pubmed/21730289; pubmed/16763719; pubmed/20716579; pubmed/16845664',

`   `'evidence\_level': '11',

`   `'definition': 'Q99801 involved in positive regulation of 9606/NKX3-1'}]

'Negative regulation results:',

` `[{'gene\_name': 'AR',

`   `'database': '<https://github.com/saezlab/CollecTRI>',

`   `'articles': 'pubmed/23492366; pubmed/17202838; pubmed/20363913; pubmed/18360715; pubmed/16697957',

`   `'evidence\_level': '5',

`   `'definition': 'Q99801 involved in regulation of 9606/AR'},

`  `{'gene\_name': 'BCL2',

`   `'database': '<https://github.com/saezlab/CollecTRI>',

`   `'articles': 'pubmed/24273454; pubmed/17191317; pubmed/22869582; pubmed/16316993; pubmed/22266868; pubmed/9581775; pubmed/15817464; pubmed/19137013; pubmed/22331597; pubmed/23313858; pubmed/12679484; pubmed/24098340; pubmed/17486276; pubmed/14684736; pubmed/8183578; pubmed/19266349; pubmed/21940310',

`   `'evidence\_level': '17',

`   `'definition': 'Q99801 involved in regulation of 9606/BCL2'},

`  `{'gene\_name': 'CCND1',

`   `'database': '<https://github.com/saezlab/CollecTRI>',

`   `'articles': 'pubmed/17639064; pubmed/22179513',

`   `'evidence\_level': '2',

`   `'definition': 'Q99801 involved in regulation of 9606/CCND1'}]

**Tabla resumen:**



|Variable|Rol|Tipo|Descripción|Propiedad de la Ontología|Grafo|
| :- | :- | :- | :- | :- | :- |
|**“tfac”**|**entrada**|**string**|**Nombre del del factor de transcripción en formato entry name de Uniprot**|**obo:RO\_0002429(involved in positive regulation of ) y obo:RO\_0002430(involved in negative regulation of )**|**tfac2gene**|
|**“gene\_name”**|**salida**|**string** |**Nombre del gen en formato symbol relacionado con el factor de transcripción**|**obo:RO\_0002429(involved in positive regulation of ) y obo:RO\_0002430(involved in negative regulation of )**|**tfac2gene**|
|**“database”**|**salida**|**string**|**Base de datos con la información sobre la relación entre el factor de transcripción y el gen**|<p>**sio:SIO\_0000253**</p><p>**(has source)**</p>|**tfac2gene**|
|**“articles”**|**salida**|**string**|**Artículos asociados a la relación**|<p>**sio:SIO\_0000772**</p><p>**(has evidence)**</p>|**tfac2gene**|
|**“evidence\_level”**|**salida**|**integer**|**Evidencia que respalda la información disponible sobre la relación entre el factor de transcripción y el gen**|**sch:evidenceLevel**|**tfac2gene**|
|**“definition”**|**salida**|**string**|**Definición de la relación**|**skos:definition**|**tfac2gene**|

# <a name="_cfxmgttjx51d"></a>**Función gene2tfac(gene)**
**Descripción:** Esta función devolverá los factores de transcripción que regulan el gen introducido, usando la información disponible en el grafo **http://rdf.biogateway.eu/graph/tfac2gene.**

**Parámetros:**

**-”gene”:** Este parámetro corresponde al nombre del gen en formato symbol (propiedad: prefLabel). Ejemplo: “TOX3”.

**Salida:**

La función tiene como salida dos diccionarios con los factores de transcripción que regulan de manera positiva al gen en uno de ellos, y en el otro aquellos que lo regulan de manera negativa. Presenta los siguientes campos:

**-“tfac\_name”:** Nombres en formato entry name de Uniprot de los factores de transcripción que interactúan con el gen introducido (propiedad: RO\_0002429 (involved in positive regulation of) y propiedad: RO\_0002430  (involved in negative regulation of)). 

**-”database”:** Indica la base de datos donde se encuentra registrada la información sobre la relación entre el gen y el factor de transcripción(propiedad: SIO\_000253 (has source)).

**-”articles”:** Corresponde a artículos científicos o publicaciones que están asociadas con la relación entre el factor de transcripción y el gen de interés, que se encuentran en la base de datos Pubmed (propiedad: SIO\_000772 (has evidence)).

**-“evidence\_level”:** Corresponde a la evidencia que respalda la información disponible sobre la relación entre el factor de transcripción y el gen (propiedad: evidenceOrigin).

**-”definition”**: Proporciona la definición de la relación que se produce entre cada factor de transcripción y el gen especificado (propiedad: definition), disponible en el grafo **http://rdf.biogateway.eu/graph/tfac2gene**.

**Ejemplo de ejecución:**

Entrada: gene2tfac("BRCA1")

Salida:

('Positive regulation results:',

` `[{'tfac\_name': 'BHE41\_HUMAN',

`   `'database': '<https://github.com/saezlab/CollecTRI>',

`   `'articles': 'pubmed/20006609',

`   `'evidence\_level': '1',

`   `'definition': 'Q9C0J9 involved in positive regulation of 9606/BRCA1'},

`  `{'tfac\_name': 'P63\_HUMAN',

`   `'database': '<https://github.com/saezlab/CollecTRI>',

`   `'articles': 'pubmed/24556685',

`   `'evidence\_level': '1',

`   `'definition': 'Q9H3D4 involved in positive regulation of 9606/BRCA1'},

`  `{'tfac\_name': 'MBD2\_HUMAN',

`   `'database': '<https://github.com/saezlab/CollecTRI>',

`   `'articles': 'pubmed/16052033; pubmed/23011797',

`   `'evidence\_level': '2',

`   `'definition': 'Q9UBB5 involved in positive regulation of 9606/BRCA1'}

'Negative regulation results:',

` `[{'tfac\_name': 'HMGA1\_HUMAN',

`   `'database': '<https://github.com/saezlab/CollecTRI>',

`   `'articles': 'pubmed/16007157; pubmed/12640109',

`   `'evidence\_level': '2',

`   `'definition': 'P17096 involved in regulation of 9606/BRCA1'},

`  `{'tfac\_name': 'HMGA1\_HUMAN',

`   `'database': '<https://github.com/saezlab/CollecTRI>',

`   `'articles': 'pubmed/16007157; pubmed/12640109',

`   `'evidence\_level': '2',

`   `'definition': 'P17096 involved in negative regulation of 9606/BRCA1'},

`  `{'tfac\_name': 'ID4\_HUMAN',

`   `'database': '<https://github.com/saezlab/CollecTRI>',

`   `'articles': 'pubmed/24475217; pubmed/12032322; pubmed/17016441; pubmed/11136250; pubmed/21194482; pubmed/16582598',

`   `'evidence\_level': '6',

`   `'definition': 'P47928 involved in negative regulation of 9606/BRCA1'},

`  `{'tfac\_name': 'LMO4\_HUMAN',

`   `'database': '<https://github.com/saezlab/CollecTRI>',

`   `'articles': 'pubmed/12925972; pubmed/11751867',

`   `'evidence\_level': '2',

`   `'definition': 'P61968 involved in negative regulation of 9606/BRCA1'},


**Tabla resumen:**

|Variable|Rol|Tipo|Descripción|Propiedad de la Ontología|Grafo|
| :- | :- | :- | :- | :- | :- |
|**“gene”**|**entrada**|**string**|**Nombre del gen en formato symbol relacionado con el factor de transcripción**|**obo:RO\_0002429(involved in positive regulation of ) y obo:RO\_0002430(involved in negative regulation of )**|**tfac2gene**|
|**“tfac\_name”**|**salida**|**string** |**Nombre del del factor de transcripción en formato entry name de Uniprot**|**obo:RO\_0002429(involved in positive regulation of ) y obo:RO\_0002430(involved in negative regulation of )**|**tfac2gene**|
|**“database”**|**salida**|**string**|**Base de datos con la información sobre la relación entre el factor de transcripción y el gen**|<p>**sio:SIO\_0000253**</p><p>**(has source)**</p>|**tfac2gene**|
|**“articles”**|**salida**|**string**|**Artículos asociados a la relación**|<p>**sio:SIO\_0000772**</p><p>**(has evidence)**</p>|**tfac2gene**|
|**“evidence\_level”**|**salida**|**integer**|**Evidencia que respalda la información disponible sobre la relación entre el factor de transcripción y el gen**|**sch:evidenceLevel**|**tfac2gene**|
|**“definition”**|**salida**|**string**|**Definición de la relación**|**skos:definition**|**tfac2gene**|

# <a name="_eju3h69stbja"></a>**Funciones auxiliares**
-**data\_processing:** Facilita el procesamiento de los datos obtenidos en las consultas SPARQL, de manera que el usuario obtenga resultados fácilmente legibles y entendibles.

-**translate\_chr**: Permite traducir un cromosoma humano en su identificador en el NCBI. Por ejemplo, chr-1 lo traduce a NC\_000001.11.
