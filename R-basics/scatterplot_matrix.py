## SCATTERPLOT MATRIX ##
'''
There is a tool called the 'scatterplot matrix', which generates a scatter plot between every variable in the 
dataset and plots them all in a grid.
This can be useful to quickly identify patterns or relationships of interest between variables that we may 
have not been expecting!
'''
#NOTE: for CATEGORICAL variables boxplots/histograms might be more appropriate that scatter plots. Can still make matrixes of these as well.

#Using the 'GGally' package with its 'ggpairs()' function, the code looks like this:

set.seed(number)    # set seed 'for reproducible results'
ggpairs(df)         # generate scatterplot matrix for entire df

'''
IMPORTANT!!!
Depending on the size of the dataset, this can take up to AN HOUR to run! Make sure that if you do run it, 
you save the plot as an image so you can quickly look at it later!
'''
#You can speed it up by taking a 'sample()' of the data to operate on (insert into the 'df' parameter position).

#Might want to use the minimal theme styling:
theme_set(theme_minimal(20))
