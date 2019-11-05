import re


# result = re.findall(r"\\begin{tabular\}(?:{.*\})?\s*(?:\s*(.*?)\\\\\s*)*\\end{tabular}", latex_input)

def change_color(latex_input, pairs, colors):
    table = extract_table(latex_input)

    for pair in pairs:
       print(table[pair[0]][pair[1]])



def extract_table(latex_input):
    rowsStr = re.findall(r"\\begin\{tabular\}(?:\{.*\})?(.*)\\\\\s*\\end{tabular}", latex_input, flags=re.S)[0]
    print(rowsStr)

    rows = re.split(r'\\\\', rowsStr)

    # rows = [row.strip() for row in rows]

    # print(rows)

    table = [re.split(r'&', row) for row in rows]
    print(table)
    return table


latex_table = r"""
\begin{tabular}{rrr}

 0.02 & 0.88 & 0.11 \\
 0.65 & 0.02 & 0.94 \\
 0.31 & 0.52 & 0.50 \\

\end{tabular}"""
change_color(latex_table, [[1, 2], [0, 1]], ['#123456', '#549085'])
