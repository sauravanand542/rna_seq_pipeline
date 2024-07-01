import subprocess
import os

UPLOAD_FOLDER = 'uploads'
PREPROCESS_FOLDER = 'preprocess'
os.makedirs(PREPROCESS_FOLDER, exist_ok=True)

# List input files in UPLOAD_FOLDER
input_files = [f for f in os.listdir(UPLOAD_FOLDER) if f.endswith('.fastq')]

# Process each file with fastp (assuming single-ended)
for input_file in input_files:
    local_input_file = os.path.join(UPLOAD_FOLDER, input_file)
    local_output_file = os.path.join(PREPROCESS_FOLDER, input_file.replace('.fastq', '_trimmed.fastq'))
    subprocess.run(['fastp', '-i', local_input_file, '-o', local_output_file], check=True)
