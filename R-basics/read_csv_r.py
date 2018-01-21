## LOADING AND ANALAYZING A SAMPLE DATASET ##

#Can load in a csv file and assign it to a variable 'var' using:

df_name <- read.csv('file_name.tsv', sep='\t')   # .tsv is 'tab-separated values'

#This is saved as a 'Data Frame' object. To view the object, just doubleclick on it in the 
#'Environment' window.

#To see all of the 'variables' (i.e. the column headers), use names():

names(df_name)   # returns a list of the variable names

#Some useful functions for initial investigations of a new DF:

str(df_name)    # shows how the df is STRUCTURED
summary(df_name)    # shows some SUMMARY STATS of the df
colnames(df_name)   # shows the COLUMN NAMES
rownames(df_name)   # show the ROW NAMES
