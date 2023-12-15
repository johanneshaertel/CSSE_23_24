import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Set display options to show all rows and columns
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.max_colwidth", None)

# Reading line delimited json.
df = pd.read_json("temp/output.json", lines=True)

# Plot scatter
plt.scatter(np.log(df['public_count']), np.log(df['size_comments_w']))
plt.ylabel('Size of Comments')
plt.xlabel('Public Count')
plt.title('Scatter Plot: Size of Comments vs. Public Count')
plt.show()


