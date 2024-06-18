# BioGatewayQuery

A Python package to perform SPARQL queries and exploit the data available on BioGateway.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact Information](#contact-information)

## Installation

To install the package, use pip:

```bash
pip install BioGatewayQuery
```

## Usage
Here's a brief example of how to use the package:
```python
from BioSPARQL import getGene_info, getGenes_by_coord
# Get Gene info
result = getGene_info('BRCA1', '9606')
print(result)
# Get Genes by Coordinates
chr = "NC_000001.11"
start = 1000000
end = 2000000
strand = None  # or '+' or '-'
genes = getGenes_by_coord(chr, start, end, strand)
print("Genes in the specified coordinates:", genes)
```
## Contributing

Interested in contributing? Check out the contributing guidelines. 
Please note that this project is released with a Code of Conduct. 
By contributing to this project, you agree to abide by its terms.

## License

`BioGatewayQuery` was created by Alberto Hernández Hidalgo. It is licensed under the terms
of the MIT license.

## Contact Information
For any inquiries or issues, please contact:

Alberto Hernández Hidalgo

Email: albertoherhid@gmail.com
GitHub: https://github.com/AlbertoHernandezHidalgo