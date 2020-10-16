import numpy as np
import pandas as pd


size_selection = 'small'

if size_selection == 'large':
    n_rows = 200000000  # 200 million
elif size_selection == 'medium':
    n_rows = 20000000  # 20 million
elif size_selection == 'small':
    n_rows = 20000     # 20 thousand
else:
    raise ValueError(f"variable: size_selection was set to an unrecognized value: {size_selection}")

# generate random data: X entries, 2 columns (dimensions)
array = np.random.randint(0, 100,
                          size=(n_rows, 2),
                          dtype=np.int32)

# convert to a pandas array for easy CSV export functionality
df = pd.DataFrame(array,
                  columns=['val1', 'val2'])

# write the file to "disk"
df.to_csv(f"data/{size_selection}.csv",
          sep=',',
          index=False)
