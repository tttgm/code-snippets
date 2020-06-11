"""
Add data labels to bar and column charts in seaborn/matplotlib.
Can modify the string formatting to suit your data type and desired level of precision.
"""
### note: requires import of matplotlib like so:
import matplotlib as mpl

# vertical bar (column) chart
def datalabel_bar(ax, fontsize=12):
    rects = [rect for rect in ax.get_children() if isinstance(rect, mpl.patches.Rectangle)]
    for rect in rects:
        height = rect.get_height()
        if height > 0:
            ax.annotate(f"{height:.0f}",
                       xy=(rect.get_x() + rect.get_width() / 2, height),
                       xytext=(0, 3), # 3 points offset
                       textcoords="offset points",
                       ha="center", va="bottom", fontsize=fontsize)

# horizontal bar chart
def datalabel_hbar(ax, fontsize=12):
    rects = [rect for rect in ax.get_children() if isinstance(rect, mpl.patches.Rectangle)]
    for rect in rects:
        width = rect.get_width()
        if width > 1:
            ax.annotate(f"{width:.0f}",
                       xy=(width, rect.get_y() + rect.get_height() / 2),
                       xytext=(5,-1), # 5 points offset
                       textcoords="offset points",
                       ha="left", va="center", fontsize=fontsize)

