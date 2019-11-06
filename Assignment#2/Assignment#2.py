import re


# result = re.findall(r"\\begin{tabular\}(?:{.*\})?\s*(?:\s*(.*?)\\\\\s*)*\\end{tabular}", latex_input)

def change_color(latex_input, pairs, colors):
    (formatting,table) = extract_table(latex_input)

    for idx, pair in enumerate(pairs):
        content = table[pair[0]][pair[1]]
        color = colors[idx]

        colored_content = r"\cellcolor{}{}{}{}".format('{', color, '}', content)

        table[pair[0]][pair[1]] = colored_content

    constructed_table = construct_latex(formatting,table)
    return constructed_table



def construct_latex(formatting,table):
    table = [" & ".join(row) for row in table]

    table = ' \\\\\n'.join(table)

    table = '{}{}\n{} \\\\\n{}'.format('\\begin{tabular}',formatting, table, '\\end{tabular}')

    return table

# Expected Output:

# \begin{tabular}
#  0.02 & \cellcolor{#549085}0.88 & 0.11 \\
#  0.65 & 0.02 & \cellcolor{#123456}0.94 \\
#  0.31 & 0.52 & 0.50 \\
# \end{tabular}

def extract_table(latex_input):
    # findall gives all the matches as a list. by using [0] we take only the first tuple.
    (formatting,rowsStr) = re.findall(r"\\begin{tabular\}({.*\})?(.*)\\\\\s*\\end{tabular}", latex_input, flags=re.S)[0]
    rows = re.split(r'\\\\', rowsStr)

    table = [re.split(r'&', row) for row in rows]

    for i, x in enumerate(table):
        for j, a in enumerate(x):
            table[i][j] = a.strip()

    return (formatting, table)


latex_table = r"""
\begin{tabular}{rrr}

 0.02 & 0.88 & 0.11 \\
 0.65 & 0.02 & 0.94 \\
 0.31 & 0.52 & 0.50 \\

\end{tabular}"""
final_table = change_color(latex_table, [[1, 2], [0, 1]], ['#123456', '#549085'])
print(final_table)

