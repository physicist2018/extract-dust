from utils.readwrite import Table


def scale_data(data: Table, scale_factor: float):
    """Scale the data in a Table by a given factor.

    Args:
        data (Table): The input data to be scaled.
        scale_factor (float): The factor by which to scale the data.

    Returns:
        Table: A new Table with the scaled data.
    """
    return Table(data.row_labels, data.col_labels, data.data * scale_factor)
