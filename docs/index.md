# BioGatewayQuery

A Python package to perform SPARQL queries and exploit the data available on BioGateway.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Code_of_conduct](#code_of_conduct)
- [License](#license)
- [Contact Information](#contact-information)
- [Example usage detailed](#example)

## Installation

To install the package, use pip:

```bash
pip install BioGatewayQuery
```

## Contributing

Thank you for your interest in contributing to BioGatewayQuery! Here are a few guidelines to get started:

### Getting Started

1. Fork the repository.
2. Clone your fork: `git clone https://github.com/AlbertoHernandezHidalgo/BioGatewayQuery_python.git`
3. Create a new branch: `git checkout -b my-feature-branch`
4. Make your changes.
5. Commit your changes: `git commit -m 'Add some feature'`
6. Push to the branch: `git push origin my-feature-branch`
7. Submit a pull request.

### Code Standards

- Follow PEP 8 style guidelines.
- Write tests for any new functionality.
- Ensure existing tests pass.

### Pull Request Process

1. Ensure all tests are passing.
2. Submit your pull request.
3. The project maintainers will review your changes and provide feedback.

Thank you for your contribution!

## Code_of_conduct
### Our Pledge

We as members, contributors, and leaders pledge to make participation in our
community a harassment-free experience for everyone, regardless of age, body
size, visible or invisible disability, ethnicity, sex characteristics, gender
identity and expression, level of experience, education, socio-economic status,
nationality, personal appearance, race, religion, or sexual identity
and orientation.

We pledge to act and interact in ways that contribute to an open, welcoming,
diverse, inclusive, and healthy community.

### Our Standards

Examples of behavior that contributes to a positive environment for our
community include:

* Demonstrating empathy and kindness toward other people
* Being respectful of differing opinions, viewpoints, and experiences
* Giving and gracefully accepting constructive feedback
* Accepting responsibility and apologizing to those affected by our mistakes,
  and learning from the experience
* Focusing on what is best not just for us as individuals, but for the
  overall community

Examples of unacceptable behavior include:

* The use of sexualized language or imagery, and sexual attention or
  advances of any kind
* Trolling, insulting or derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or email
  address, without their explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

### Enforcement Responsibilities

Community leaders are responsible for clarifying and enforcing our standards of
acceptable behavior and will take appropriate and fair corrective action in
response to any behavior that they deem inappropriate, threatening, offensive,
or harmful.

Community leaders have the right and responsibility to remove, edit, or reject
comments, commits, code, wiki edits, issues, and other contributions that are
not aligned to this Code of Conduct, and will communicate reasons for moderation
decisions when appropriate.

### Scope

This Code of Conduct applies within all community spaces, and also applies when
an individual is officially representing the community in public spaces.
Examples of representing our community include using an official e-mail address,
posting via an official social media account, or acting as an appointed
representative at an online or offline event.

### Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported to the community leaders responsible for enforcement at
.
All complaints will be reviewed and investigated promptly and fairly.

All community leaders are obligated to respect the privacy and security of the
reporter of any incident.

### Enforcement Guidelines

Community leaders will follow these Community Impact Guidelines in determining
the consequences for any action they deem in violation of this Code of Conduct:

#### 1. Correction

**Community Impact**: Use of inappropriate language or other behavior deemed
unprofessional or unwelcome in the community.

**Consequence**: A private, written warning from community leaders, providing
clarity around the nature of the violation and an explanation of why the
behavior was inappropriate. A public apology may be requested.

#### 2. Warning

**Community Impact**: A violation through a single incident or series
of actions.

**Consequence**: A warning with consequences for continued behavior. No
interaction with the people involved, including unsolicited interaction with
those enforcing the Code of Conduct, for a specified period of time. This
includes avoiding interactions in community spaces as well as external channels
like social media. Violating these terms may lead to a temporary or
permanent ban.

#### 3. Temporary Ban

**Community Impact**: A serious violation of community standards, including
sustained inappropriate behavior.

**Consequence**: A temporary ban from any sort of interaction or public
communication with the community for a specified period of time. No public or
private interaction with the people involved, including unsolicited interaction
with those enforcing the Code of Conduct, is allowed during this period.
Violating these terms may lead to a permanent ban.

#### 4. Permanent Ban

**Community Impact**: Demonstrating a pattern of violation of community
standards, including sustained inappropriate behavior,  harassment of an
individual, or aggression toward or disparagement of classes of individuals.

**Consequence**: A permanent ban from any sort of public interaction within
the community.

### Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage],
version 2.0, available at
https://www.contributor-covenant.org/version/2/0/code_of_conduct.html.


## License

`BioGatewayQuery` was created by Alberto Hernández Hidalgo. It is licensed under the terms
of the MIT license.

Copyright (c) 2018 The Python Packaging Authority

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Contact Information

For any inquiries or issues, please contact:

Alberto Hernández Hidalgo

Email: albertoherhid@gmail.com
GitHub: https://github.com/AlbertoHernandezHidalgo

## Example usage detailed

We have one mutation of interest (rs4784227-> chr16:52565276) and we want to study its possible implications in the regulation of gene expression. 

First we will find the enhancers that are located on these coords with the function getCRMs_by_coord

```python
from BioGatewayQuery import getCRMs_by_coord, crm2phen, getPhenotype, crm2gene, gene2protein, prot2bp

mutation_position = 52565276

# We define a range around the mutation position (e.g., +/- 1000 bases)
range_start = mutation_position - 12500
range_end = mutation_position + 12500

#Now we use the function to get CRMs in the defined range
crms = getCRMs_by_coord("chr-16", range_start, range_end)

# We will count the number of entries in the list
num_entries = len(crms) if isinstance(crms, list) else 0
print(f"Number of CRMs in the specified range: {num_entries}")
```
Number of CRMs in the specified range: 485

We will select some crm for continue the study, and we will see if the crm is related with any disease using crm2phen function:
```python
for crm in crms:
    crm_name = crm['crm_name']
    phen_results = crm2phen(crm_name)
    if phen_results != ("No data available for the introduced crm or you may have introduced an instance that is not a crm. Check your data type with type_data function."):    
        print(f"CRM: {crm_name}")
        print(f"Phenotypes: {phen_results}\n")

print(getPhenotype("114480"))
```
CRM: crm/CRMHS00000005858
Phenotypes: [{'phen_id': 'OMIM/114480', 'database': 'http://biocc.hrbmu.edu.cn/DiseaseEnhancer/; http://health.tsinghua.edu.cn/jianglab/endisease/', 'articles': 'pubmed/23001124'}, {'phen_id': 'MESH/D001943', 'database': 'http://biocc.hrbmu.edu.cn/DiseaseEnhancer/; http://health.tsinghua.edu.cn/jianglab/endisease/', 'articles': 'pubmed/23001124'}, {'phen_id': 'DOID/DOID_1612', 'database': 'http://biocc.hrbmu.edu.cn/DiseaseEnhancer/; http://health.tsinghua.edu.cn/jianglab/endisease/', 'articles': 'pubmed/23001124'}]
[{'phen_label': 'BREAST CANCER'}]

We get the crm that are related to a phenotype, in this case only crm/CRMHS00000005858 is related to a disease, which is Breast cancer.

We are going now to search if our enhancer have any target gene using crm2gene function:
```python
genes=crm2gene("crm/CRMHS00000005858")
print(genes)
```
[{'gene_name': 'TOX3', 'database': 'http://biocc.hrbmu.edu.cn/DiseaseEnhancer/; http://health.tsinghua.edu.cn/jianglab/endisease/', 'articles': 'pubmed/23001124'}]

The gene TOX3 is related to our crm, now we can find which proteins are encoded by this gene in Homo sapiens with gene2protein function:
```python
protein=gene2protein("TOX3","Homo sapiens")
print(protein)
```
[{'prot_name': 'H3BTZ9_HUMAN'}, {'prot_name': 'J3QQQ6_HUMAN'}, {'prot_name': 'TOX3_HUMAN'}]

Finally we want to know in which biological process are involved these proteins, we will use prot2bp function:

```python
for prot in protein:
    prot_name=prot['prot_name']
    bp_results=prot2bp(prot_name)
    print(f"Protein {prot_name}")
    print(f"Biological process: {bp_results}\n")
```
Protein H3BTZ9_HUMAN
Biological process: No data available for the introduced protein or you may have introduced an instance that is not a protein. Check your data type with type_data function.

Protein J3QQQ6_HUMAN
Biological process: No data available for the introduced protein or you may have introduced an instance that is not a protein. Check your data type with type_data function.

Protein TOX3_HUMAN
Biological process: [{'bp_id': 'GO:0006357', 'bp_label': 'regulation of transcription by RNA polymerase II', 'relation_label': 'O15405--GO:0006357', 'database': 'goa/', 'articles': 'pubmed/21873635'}, {'bp_id': 'GO:0042981', 'bp_label': 'regulation of apoptotic process', 'relation_label': 'O15405--GO:0042981', 'database': 'goa/', 'articles': 'pubmed/21172805'}, {'bp_id': 'GO:0043524', 'bp_label': 'negative regulation of neuron apoptotic process', 'relation_label': 'O15405--GO:0043524', 'database': 'goa/', 'articles': 'pubmed/21172805'}, {'bp_id': 'GO:0045944', 'bp_label': 'positive regulation of transcription by RNA polymerase II', 'relation_label': 'O15405--GO:0045944', 'database': 'goa/', 'articles': 'pubmed/21172805'}]


As we can see, TOX3_HUMAN protein is related with regulation of apoptotic process, regulation of transcription by RNA polymerase II, negative regulation of neuron apoptotic process and positive regulation of transcription by RNA polymerase II. 


