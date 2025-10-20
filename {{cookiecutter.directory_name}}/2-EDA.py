#!/usr/bin/env python
# coding: utf-8

# ## {{cookiecutter.project_name}}
# 
# {{cookiecutter.description}}
# 
# This notebook contains basic statistical analysis and visualization of the data.
# 
# ### Data Sources
# - summary : Processed file from notebook 1-Data_Prep
# 
# ### Changes
# - {% now 'utc', '%m-%d-%Y' %} : Started project

# %%
import pandas as pd
from pathlib import Path
from datetime import datetime
import seaborn as sns


# %%
# get_ipython().run_line_magic('matplotlib', 'inline')


# ### File Locations
# %%
today = datetime.today()
in_file = Path.cwd() / "data" / "processed" / f"summary_{today:%b-%d-%Y}.pkl"
report_dir = Path.cwd() / "reports"
report_file = report_dir / "Excel_Analysis_{today:%b-%d-%Y}.xlsx"


# %%
df = pd.read_pickle(in_file)


# ### Perform Data Analysis
# %%



# ### Save Excel file into reports directory
# 
# Save an Excel file with intermediate results into the report directory
# %%
writer = pd.ExcelWriter(report_file, engine='xlsxwriter')


# %%
df.to_excel(writer, sheet_name='Report')


# %%
writer.save()

