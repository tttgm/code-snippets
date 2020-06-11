### Save single seaborn/matplotlib chart
fn = 'example_barchart.svg'
figure = ax.get_figure()
figure.savefig(fn, bbox_inches="tight")

### Save seaborn "small multiples" chart (`FacetGrid`)
### note: seaborn func call is saved to variable 'g' which is
### a 'FacetGrid' object
fn = 'example_FacetGrid_chart.svg'
g.savefig(fn, bbox_inches = "tight")

### Alternatively, for consistency with above, first get
### the figure element, then save:
figure = g.fig
figure.savefig(fn, bbox_inches = "tight")
