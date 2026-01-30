from matplotlib import pyplot as plt

from config.cmdargs import parse_cmd_args
from config.readconfig import display_config, read_config
from models.model import InputData
from solver.solver import findEtaD, prepareData
from utils.display import plot_table_heatmap
from utils.readwrite import read_matrix_file
from utils.scale import scale_data


def main():
    cmdArgs = parse_cmd_args()
    config = read_config(cmdArgs.cfg_file)
    display_config(config=config)

    dep = scale_data(read_matrix_file(cmdArgs.dep_file), 1.0 / 100)
    fl = read_matrix_file(cmdArgs.fl_file)

    inputData = InputData(delta=dep, gf=fl)

    inpData = prepareData(inputData, config)
    etaData = findEtaD(inputData, config)

    plot_table_heatmap(
        inpData.delta,
        cmap="jet",
        title=r"$\delta_{nd}$ - остаточная деполяризация",
    )

    plot_table_heatmap(
        etaData.delta_nd,
        cmap="jet",
        title=r"$\eta_{d}$ - доля пылевого аэрозоля ($0 \leq \eta_{d} \leq 1$)",
    )
    plt.show()


if __name__ == "__main__":
    main()
