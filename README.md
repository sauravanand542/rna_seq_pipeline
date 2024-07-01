# RNA-seq Pipeline

This repository contains an RNA-seq pipeline for processing RNA sequencing data, from raw reads to differential expression analysis. The pipeline is designed to be flexible and scalable, suitable for handling large datasets and integrating seamlessly into various analysis workflows.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
  - [Preprocessing](#preprocessing)
  - [Read Alignment](#read-alignment)
  - [Quantify Expression](#quantify-expression)
  - [Differential Expression Analysis](#differential-expression-analysis)
- [Credits](#credits)

## Overview

This RNA-seq pipeline processes raw RNA sequencing data to identify differentially expressed genes between conditions. The pipeline includes the following steps:
1. **Preprocessing**: Quality control and trimming of raw sequencing reads.
2. **Read Alignment**: Aligning trimmed reads to a reference genome.
3. **Quantify Expression**: Counting the number of reads aligned to each gene.
4. **Differential Expression Analysis**: Identifying genes that are differentially expressed between conditions.
5. **Significant Genes**: Extracting genes that meet the significance threshold.
6. **Functional Analysis**: Performing gene set enrichment analysis on the significant genes.

## Installation

### Requirements

- Python 3.9
- Required Python packages (specified in `requirements.txt`)
- External tools: `fastp`, `hisat2`, `featureCounts`

### Install Python Packages

```bash
pip install -r requirements.txt
```

### Install External Tools

```bash
# Install fastp
sudo apt-get update
sudo apt-get install -y fastp

# Install HISAT2
sudo apt-get install -y hisat2

# Install Subread (which includes featureCounts)
sudo apt-get install -y subread
```

## Usage
### Create the uploads Directory

-Upload the the fasta files in the uploads folder
```bash
mkdir uploads
```

### Run the pipeline
```bash
python3 app.py
curl -X POST http://localhost:5000/run_pipeline
```
## Preprocessing
- Preprocess raw FASTQ files using fastp for quality control and trimming.

## Read Alignment
- Align trimmed reads to the reference genome using hisat2.

## Quantify Expression
- Count the number of reads aligned to each gene using featureCounts.

## Differential Expression Analysis
- Perform differential expression analysis to identify genes that are differentially expressed between conditions.

## Credits
This pipeline was developed by Saurav Anand. Contributions and feedback are welcome.

For more information, refer to the individual script comments and documentation within this repository.
