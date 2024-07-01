from flask import Flask, request, jsonify
import subprocess
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return 'Hello, this is the RNA-seq pipeline web app!'

@app.route('/run_pipeline', methods=['POST'])
def run_pipeline():
    local_dirs = [UPLOAD_FOLDER, 'preprocess', 'align_reads', 'quantify_expression', 'differential_expression']
    for dir in local_dirs:
        os.makedirs(dir, exist_ok=True)

    # Run preprocess.py
    #subprocess.run(['python3', 'preprocess.py'], check=True)
    
    # Run align_reads.py
    #subprocess.run(['python3', 'align_reads.py'], check=True)
    
    # Run quantify_expression.py
    #subprocess.run(['python3', 'quantify_expression.py'], check=True)
    
    # Run differential_expression.py
    subprocess.run(['python3', 'differential_expression.py'], check=True)

    return 'Pipeline run successfully', 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
