### USING JUPYTER NOTEBOOK AS SLIDES ###

"""
To create a slideshow using a jupyter notebook is easy.

First, prepare notebook as slides via View -> Cell Toolbar -> Slideshow.

Then, mark each cell as a 'slide', 'sub-slide', 'note', or to be skipped (i.e. not shown).

Save notebook.

"""

# To initiate slideshow (presentation) in the browser, run the following command in Terminal:
jupyter nbconvert documents\jupyter-notebook-file.ipynb --to slides --post serve 

# Where 'documents\jupyter-notebook-file.ipynb' is just the notebook dir address/name!
