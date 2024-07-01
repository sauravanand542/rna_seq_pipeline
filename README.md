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
  - [Significant Genes](#significant-genes)
  - [Functional Analysis](#functional-analysis)
- [File Descriptions](#file-descriptions)
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
Install External Tools
You will need to install the following external tools. Below are the installation commands for Ubuntu:

bash
Copy code
# Install fastp
sudo apt-get update
sudo apt-get install -y fastp

# Install HISAT2
sudo apt-get install -y hisat2

# Install Subread (which includes featureCounts)
sudo apt-get install -y subread
Usage
Create the uploads Directory

Before starting the pipeline, create an uploads directory in the project root to store your raw FASTQ files.

bash
Copy code
mkdir uploads
Run the Pipeline

The pipeline can be run in a step-by-step manner, executing each script in the correct order.

Preprocessing
Preprocess raw FASTQ files using fastp for quality control and trimming.

bash
Copy code
python preprocess.py
Read Alignment
Align trimmed reads to the reference genome using hisat2.

bash
Copy code
python align_reads.py
Quantify Expression
Count the number of reads aligned to each gene using featureCounts.

bash
Copy code
python quantify_expression.py
Differential Expression Analysis
Perform differential expression analysis to identify genes that are differentially expressed between conditions.

bash
Copy code
python differential_expression.py
Significant Genes
Extract significant genes based on p-value threshold.

bash
Copy code
python significant_genes.py
Functional Analysis
Perform gene set enrichment analysis on significant genes.

bash
Copy code
python functional_analysis.py
File Descriptions
preprocess.py: Preprocesses raw FASTQ files using fastp for quality control and trimming.
align_reads.py: Aligns trimmed reads to a reference genome using hisat2.
quantify_expression.py: Counts the number of reads aligned to each gene using featureCounts.
differential_expression.py: Performs differential expression analysis using OLS regression.
significant_genes.py: Extracts genes that meet the significance threshold.
functional_analysis.py: Performs gene set enrichment analysis on the significant genes.
app.py: A Flask web application for running the pipeline through a web interface.
conditions.csv: A CSV file containing sample conditions for the differential expression analysis.
Credits
This pipeline was developed by Saurav Anand. Contributions and feedback are welcome.

For more information, refer to the individual script comments and documentation within this repository.

vbnet
Copy code

### Instructions for Using Each Python File

1. **preprocess.py**
   - This script uses `fastp` to perform quality control and trimming on raw FASTQ files.
   - Make sure to place your raw FASTQ files in the `uploads` directory.
   - Run the script: `python preprocess.py`

2. **align_reads.py**
   - This script uses `hisat2` to align the trimmed reads to the reference genome.
   - Ensure that the reference genome is indexed and available in the `genome_index` directory.
   - Run the script: `python align_reads.py`

3. **quantify_expression.py**
   - This script uses `featureCounts` to count the number of reads aligned to each gene.
   - Run the script: `python quantify_expression.py`

4. **differential_expression.py**
   - This script performs differential expression analysis using OLS regression.
   - Make sure the `conditions.csv` file is correctly formatted and placed in the project root.
   - Run the script: `python differential_expression.py`

5. **significant_genes.py**
   - This script extracts genes that meet a specified p-value threshold for significance.
   - Run the script: `python significant_genes.py`

6. **functional_analysis.py**
   - This script performs gene set enrichment analysis on the significant genes.
   - Run the script: `python functional_analysis.py`

By following these instructions, users should be able to run the entire RNA-seq pipeline, starting from raw FASTQ files and ending with a list of differentially expressed genes and their functional analysis. If you have any questions or issues, please refer to the comments and documentation within each script or reach out to the repository maintainer.





