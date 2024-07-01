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
  - [Application file](#app)
- [Interpreting Differential Expression Results](#results)
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
This script uses fastp to perform quality control and trimming on raw FASTQ files. The script scans the uploads folder for input files, processes them, and saves the output to the preprocess folder.

## Read Alignment
This script uses hisat2 to align the trimmed reads to the reference genome. It reads the trimmed files from the preprocess folder, aligns them to a reference genome (which should be indexed beforehand), and saves the output to the align_reads folder.

## Quantify Expression
This script uses featureCounts to count the number of reads aligned to each gene. It processes the aligned read files from the align_reads folder and generates a count matrix, which is saved to the quantify_expression folder.

## Differential Expression Analysis
This script performs differential expression analysis using OLS regression. It reads the count matrix and the conditions.csv file to identify differentially expressed genes between conditions. The results, including regression summaries, are saved in the differential_expression folder.

## Application file
This script creates a Flask web application to run the pipeline through a web interface. Users can upload their raw FASTQ files to the uploads folder and trigger the pipeline by sending a POST request to the server.

## Interpreting Differential Expression Results
Let's say the differential_expression_results.csv file contains the following data:

gene	coef	p-value	r-squared
gene1	2.0	0.01	0.85
gene2	-1.5	0.03	0.90

## Credits
This pipeline was developed by Saurav Anand. Contributions and feedback are welcome.

For more information, refer to the individual script comments and documentation within this repository.
