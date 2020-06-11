### Save single seaborn/matplotlib chart
fn = 'example_barchart.svg'
figure = ax.get_figure()
figure.savefig(fn, bbox_inches="tight")

### Save seaborn "small multiples" chart (`FacetGrid`)
### note: seaborn func call is saved to variable 'g'
fn = 'example_FacetGrid_chart.svg'
figure = g.fig
figure.savefig(fn, bbox_inches = "tight")
