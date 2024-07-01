import subprocess
import os

ALIGN_READS_FOLDER = 'align_reads'
QUANTIFY_EXPRESSION_FOLDER = 'quantify_expression'
os.makedirs(QUANTIFY_EXPRESSION_FOLDER, exist_ok=True)

# List input files in ALIGN_READS_FOLDER
input_files = [f for f in os.listdir(ALIGN_READS_FOLDER) if f.endswith('_aligned.sam')]

# Run featureCounts for each input file
for input_file in input_files:
    local_input_file = os.path.join(ALIGN_READS_FOLDER, input_file)
    output_file = os.path.join(QUANTIFY_EXPRESSION_FOLDER, input_file.replace('_aligned.sam', '_counts.txt'))
    subprocess.run(['featureCounts', '-a', 'Homo_sapiens.GRCh38.104.gtf', '-o', output_file, '-T', '4', local_input_file], check=True)
