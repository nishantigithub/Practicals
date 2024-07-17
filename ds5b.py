import pandas as pd
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Assuming you have a DataFrame with a 'group' column and a 'value' column
# Replace this with your actual data
data = {'group': ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D'],
        'value': [5, 7, 8, 6, 10, 12, 15, 13]}

df = pd.DataFrame(data)

# One-way ANOVA
f_statistic, p_value = f_oneway(df['value'][df['group'] == 'A'],
                                  df['value'][df['group'] == 'B'],
                                  df['value'][df['group'] == 'C'],
                                  df['value'][df['group'] == 'D'])

# Check if the overall ANOVA is significant
if p_value < 0.05:
    print("ANOVA is significant (p < 0.05)")
    print(f"F-statistic: {f_statistic}")
    print(f"P-value: {p_value}")

    # Perform Tukey's HSD post-hoc test
    tukey_results = pairwise_tukeyhsd(df['value'], df['group'])

    # Display the results
    print(tukey_results)

else:
    print("ANOVA is not significant (p >= 0.05)")
