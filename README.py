# My-first-repository
# How to open a tsv file in jupyter notebook.
import pandas as pd
df= pd.csv_read("file directory/file_name.tsv", delimiter='\t' ) #delimiter concatanates the columns and represent it like a csv file
# the df is storing the tsv file in a dataframe
# for example df = pd.read_csv("D:/DataAnalysis/top_500_albums.tsv", delimiter='\t')
df # it prints the dataFrame
