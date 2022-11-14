import pandas as pd
import os
import sys

# convert csv to dataframe,
# and add a filename as the new column
def getDf(filepath):
    df = pd.read_csv(filepath)
    filename = os.path.basename(filepath)
    df.insert(loc=len(df.columns), column='filename', value=filename)
    return df

combined = pd.DataFrame()
# iterate all files we want to combine
for filepath in sys.argv[1:]:
    df = getDf(filepath)
    combined = pd.concat([combined, df])

# print the result
print(combined.to_csv(index=False, quoting=1))

