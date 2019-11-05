import re


# result = re.findall(r"\\begin{tabular\}(?:{.*\})?\s*(?:\s*(.*?)\\\\\s*)*\\end{tabular}", latex_input)

def assignment(latex_input, pairs, colors):
    rowsStr = re.findall(r"\\begin\{tabular\}(?:\{.*\})?(.*)\\\\\s*\\end{tabular}", latex_input, flags=re.S)[0]
    print(rowsStr)

    rows = re.split(r'\\\\', rowsStr)

    rows = [row.strip() for row in rows]
    print(rows)


latex_table = r"""
\begin{tabular}{rrr}

 0.02 & 0.88 & 0.11 \\
 0.65 & 0.02 & 0.94 \\
 0.31 & 0.52 & 0.50 \\

\end{tabular}"""
assignment(latex_table, [[1, 2], [5, 4]], ['#123456', '#549085'])
