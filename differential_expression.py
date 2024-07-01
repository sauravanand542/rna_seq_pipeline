import pandas as pd
import statsmodels.api as sm
import os

QUANTIFY_EXPRESSION_FOLDER = 'quantify_expression'
DIFFERENTIAL_EXPRESSION_FOLDER = 'differential_expression'
os.makedirs(DIFFERENTIAL_EXPRESSION_FOLDER, exist_ok=True)

# List input files in QUANTIFY_EXPRESSION_FOLDER
input_files = [f for f in os.listdir(QUANTIFY_EXPRESSION_FOLDER) if f.endswith('_counts.txt')]

# Load the counts and conditions data
all_counts = []
for input_file in input_files:
    counts = pd.read_csv(os.path.join(QUANTIFY_EXPRESSION_FOLDER, input_file), sep='\t', comment='#', header=0)
    counts.set_index('Geneid', inplace=True)
    counts = counts.iloc[:, 5:]  # Assuming the first 5 columns are metadata
    all_counts.append(counts)

# Concatenate counts data
all_counts = pd.concat(all_counts, axis=1)
all_counts = all_counts.T  # Transpose so genes are columns

# Load the conditions file
conditions = pd.read_csv('conditions.csv')

# Ensure the 'intercept' column is present
if 'intercept' not in conditions.columns:
    conditions['intercept'] = 1

# Align the indices of conditions and counts based on the sample names
conditions.set_index('sample', inplace=True)
all_counts.index = conditions.index  # Assuming that all_counts index should be aligned with sample names in conditions

# Check for missing values
if conditions.isnull().values.any():
    raise ValueError("There are missing values in the conditions DataFrame after reindexing.")

# Perform differential expression analysis for each gene
results_list = []
for gene in all_counts.columns:
    endog = all_counts[gene]
    exog = conditions[['intercept', 'condition']]
    model = sm.OLS(endog, exog).fit()
    
    results_list.append({
        'gene': gene,
        'coef': model.params['condition'],
        'p-value': model.pvalues['condition'],
        'r-squared': model.rsquared
    })

# Convert results to DataFrame
results_df = pd.DataFrame(results_list)

# Save results
results_df.to_csv(os.path.join(DIFFERENTIAL_EXPRESSION_FOLDER, 'differential_expression_results.csv'), index=False)

with open(os.path.join(DIFFERENTIAL_EXPRESSION_FOLDER, 'regression_summary.txt'), 'w') as f:
    f.write(results_df.describe().to_string())
