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

### Install external tools

```bash
# Install fastp
sudo apt-get update
sudo apt-get install -y fastp

# Install HISAT2
sudo apt-get install -y hisat2

# Install Subread (which includes featureCounts)
sudo apt-get install -y subread

