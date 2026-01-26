from matplotlib import pyplot as plt

from config.readconfig import get_default_config
from models.model import InputData
from solver.solver import findEtaD
from utils.display import plot_table_heatmap
from utils.readwrite import Table, read_matrix_file


def main():
    config = get_default_config()
    dep = read_matrix_file("dep.txt")
    dep.data /= 100

    res = findEtaD(InputData(delta=dep.data, beta=dep.data, gf=dep.data), config)
    plot_table_heatmap(
        Table(dep.row_labels, dep.col_labels, res.delta_nd),
        cmap="jet",
        title=r"$\delta_{nd}$",
    )
    plt.show()


if __name__ == "__main__":
    main()
