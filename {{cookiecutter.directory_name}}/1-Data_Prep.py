#!/usr/bin/env python
# coding: utf-8

# ## {{cookiecutter.project_name}}
# 
# {{cookiecutter.description}}
# 
# ### Data Sources
# - file1 : Description of where this file came from
# 
# ### Changes
# - {% now 'utc', '%m-%d-%Y' %} : Started project

# %%
import pandas as pd
from pathlib import Path
from datetime import datetime


# ### File Locations
# %%
today = datetime.today()
in_file = Path.cwd() / "data" / "raw" / "FILE1"
summary_file = Path.cwd() / "data" / "processed" / f"summary_{today:%b-%d-%Y}.pkl"


# %%
df = pd.read_csv(in_file)


# ### Column Cleanup
# 
# - Remove all leading and trailing spaces
# - Rename the columns for consistency.
# %%
# https://stackoverflow.com/questions/30763351/removing-space-in-dataframe-python
df.columns = [x.strip() for x in df.columns]


# %%
cols_to_rename = {'col1': 'New_Name'}
df.rename(columns=cols_to_rename, inplace=True)


# ### Clean Up Data Types
# %%
df.dtypes


# ### Data Manipulation
# %%



# ### Save output file into processed directory
# 
# Save a file in the processed directory that is cleaned properly. It will be read in and used later for further analysis.
# 
# Other options besides pickle include:
# - feather
# - msgpack
# - parquet
# %%
df.to_pickle(summary_file)

