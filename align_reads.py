import subprocess
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

PREPROCESS_FOLDER = 'preprocess'
ALIGN_READS_FOLDER = 'align_reads'
os.makedirs(ALIGN_READS_FOLDER, exist_ok=True)

# List input files in PREPROCESS_FOLDER
input_files = [f for f in os.listdir(PREPROCESS_FOLDER) if f.endswith('_trimmed.fastq')]

try:
    # Run HISAT2 for each input file (assuming single-ended)
    for input_file in input_files:
        local_input_file = os.path.join(PREPROCESS_FOLDER, input_file)
        output_file = os.path.join(ALIGN_READS_FOLDER, input_file.replace('_trimmed.fastq', '_aligned.sam'))
        logger.info(f"Running HISAT2 for {local_input_file}")
        subprocess.run(['hisat2', '-x', 'genome_index/Homo_sapiens.GRCh38.dna.primary_assembly', '-U', local_input_file, '-S', output_file], check=True)
except subprocess.CalledProcessError as e:
    logger.error(f"An error occurred during alignment: {e}")
    raise
