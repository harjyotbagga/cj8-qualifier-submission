from typing import Any, List, Optional


def make_table(rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False) -> str:
    """
    :param rows: 2D list containing objects that have a single-line representation (via `str`).
    All rows must be of the same length.
    :param labels: List containing the column labels. If present, the length must equal to that of each row.
    :param centered: If the items should be aligned to the center, else they are left aligned.
    :return: A table representing the rows passed in.
    """
    
    # Initiating final_table string
    final_table = ""
    n_rows = len(rows)
    n_cols = len(rows[0])
    max_length = [0 for i in range(n_cols)]

    # Checking the dimensions of the input, to make sure entries are correct.
    try:
        if labels:
            if (len(labels) != n_cols):
                raise Exception("The dimensions of rows are unequal. Please recheck the input.")
        for row in rows:
            if (len(row) != n_cols):
                raise Exception("The dimensions of rows are unequal. Please recheck the input.")
    except Exception as e:
        print(e)
        exit(0)
    
    # Taking the max_length of each column
    if labels:
        for i in range(n_cols):
            max_length[i] = max(max_length[i], len(str(labels[i])))
    for row in rows:
        for i in range(n_cols):
            max_length[i] = max(max_length[i], len(str(row[i])))

    # Adding the top row
    final_table += "┌"
    for i in range(n_cols):
        final_table += "─"*(max_length[i]+2)
        if (i != n_cols-1):
            final_table += "┬"
    final_table += "┐"
    final_table += "\n"
    
    # Adding label row
    if labels:
        for i in range(n_cols):
            final_table += "│ "
            if not centered:
                final_table += str(labels[i])
                final_table += " "*(max_length[i]-len(str(labels[i])))
            else:
                diff = max_length[i]-len(str(labels[i]))
                final_table += " "*(diff//2)
                final_table += str(labels[i])
                final_table += " "*(diff - diff//2)
            final_table += " "
        final_table += "│"
        final_table += "\n"
        final_table += "├"
        for i in range(n_cols):
            final_table += "─"*(max_length[i]+2)
            if (i != n_cols-1):
                final_table += "┼"
        final_table += "┤"
        final_table += "\n"
    
    # Adding rows
    for row in rows:
        for i in range(n_cols):
            final_table += "│ "
            if not centered:
                final_table += str(row[i])
                final_table += " "*(max_length[i]-len(str(row[i])))
            else:
                diff = max_length[i]-len(str(row[i]))
                final_table += " "*(diff//2)
                final_table += str(row[i])
                final_table += " "*(diff - diff//2)
            final_table += " "
        final_table += "│"
        final_table += "\n"
    
    # Adding bottom row
    final_table += "└"
    for i in range(n_cols):
        final_table += "─"*(max_length[i]+2)
        if (i != n_cols-1):
            final_table += "┴"
    final_table += "┘"
    final_table += "\n"    
    return final_table