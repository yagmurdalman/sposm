import re

# Given a latex input in plain text, pairs as list of index pairs and colors as list,
# it returns a plain text latex table with the content of the indicated cells colored with the desired colors.
def change_color(latex_input, pairs, colors):

    # First check the parameters' correctness
    assert len(pairs) == len(colors), "The number of pairs and colors must be the same!"

    assert type(pairs) == list, "The type of pairs must be list!"

    assert type(colors) == list, "The type of colors must be list!"

    assert r"\hline" not in latex_input, r"Currently latex tables with '\hline' are not supported!"

    (formatting, table) = extract_table(latex_input)

    for idx, pair in enumerate(pairs):

        check_valid_pair(table, pair)

        # Start index at 1 (The default one is starting from 0)
        row_idx, col_idx = pair[0] - 1, pair[1] - 1
        content = table[row_idx][col_idx]
        color = colors[idx]

        colored_content = r"\cellcolor{}{}{}{}".format('{', color, '}', content)

        table[row_idx][col_idx] = colored_content

    constructed_table = construct_latex(formatting, table)
    return constructed_table

# Given latex input string, this function applies regex to extract latex formatting and the rows.
def extract_table(latex_input):

    try:
        # findall gives all the matches as a list. by using [0] we take only the first tuple.
        # First match is latex formatting e.g. {ccc}
        # Second match contains all content between \begin{tabular} and \end{tabular}
        (formatting, rowsStr) = \
            re.findall(r"\\begin{tabular\}({.*\})?(.*)\\\\\s*\\end{tabular}", latex_input, flags=re.S)[0]
        rows = re.split(r'\\\\', rowsStr)

        table = [re.split(r'&', row) for row in rows]

        for i, x in enumerate(table):
            for j, a in enumerate(x):
                table[i][j] = a.strip()

        return formatting, table

    # If any error happens when applying regex, raise an error message with a better explanation
    except:
        raise ValueError("Complex latex tables are not supported. Please check your latex table!")

# Given formatting and table, this function constructs latex table.
def construct_latex(formatting, table):
    table = [" & ".join(row) for row in table]

    table = ' \\\\\n'.join(table)

    table = '{}{}\n{} \\\\\n{}'.format('\\begin{tabular}', formatting, table, '\\end{tabular}')

    return table

# Given extracted table and each pair, this function checks if row and column indexes are within range.
def check_valid_pair(table, pair):
    if pair[0] < 1 or pair[1] < 1:
        raise ValueError("Pairs must contain only positive integers. Found: {}".format(pair))
    if pair[0] > len(table):
        raise ValueError("Pairs must be in the range. Found: {}".format(pair))
    if pair[1] > len(table[pair[0] - 1]):
        raise ValueError("Pairs must be in the range. Found: {}".format(pair))

# Example usage
latex_table = r"""
\begin{tabular}
 Col1 & Col2 & Col3 \\
 0.02 & 0.88 & 0.11 \\
 0.65 & 0.02 & 0.94 \\
 0.31 & 0.52 & 0.50 \\

\end{tabular}"""
final_table = change_color(latex_table, [[1, 2], [2, 2], [3, 1]], ['red', 'blue', 'green'])
print(final_table)
