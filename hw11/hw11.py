from pulp import *
import pandas as pds

file_data = pds.ExcelFile(r"C:\Users\ShYam\ISYE6501\hw12 (11)-SP22\data 15.2\diet.xls")
file_data.sheet_names