import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm

mpl.rcParams['xtick.labelsize'] = 10
mpl.rcParams['ytick.labelsize'] = 12
mpl.rcParams['axes.edgecolor'] = 'gray'


axalpha = 0.05
figcolor = 'white'
dpi = 80
fig = plt.figure(figsize=(6, 1.1), dpi=dpi)
fig.patch.set_edgecolor(figcolor)
fig.patch.set_facecolor(figcolor)


def add_math_background():
    ax = fig.add_axes([0., 0., 1., 1.])

    text = []
    text.append(
        (r"E=mc2=$\sqrt{2},\ \ldots$"
         r"E=mc2=$\sqrt{2},\ \ldots$"
         r"E=mc2=$\sqrt{2},\ \ldots$"
        , (0.7, 0.2), 20))
    text.append(( r"E=mc2=$\sqrt{2},\ \ldots$" 
                  r"E=mc2=$\sqrt{2},\ \ldots$",
                 (0.35, 0.9), 20))
    text.append(( r"E=mc2=$\sqrt{2},\ \ldots$",
                 (0.15, 0.3), 25))
    text.append(( r"E=mc2=$\sqrt{2},\ \ldots$",
                 (0.85, 0.7), 30))
    for eq, (x, y), size in text:
        ax.text(x, y, eq, ha='center', va='center', color="#11557c",
                alpha=0.25, transform=ax.transAxes, fontsize=size)
    ax.set_axis_off()
    return ax


def add_matplotlib_text(ax):
    ax.text(0.95, 0.5, r"E=mc2=$\sqrt{2},\ \ldots$", color='#11557c', fontsize=65,
            ha='right', va='center', alpha=1.0, transform=ax.transAxes)

if __name__ == '__main__':
    main_axes = add_math_background()
    add_matplotlib_text(main_axes)
    plt.show()