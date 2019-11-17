from Assignment2 import *


def test_table_coloring():
    input_table = r"""
\begin{tabular}
 Col1 & Col2 & Col3 \\
 0.02 & 0.88 & 0.11 \\
 0.65 & 0.02 & 0.94 \\
 0.31 & 0.52 & 0.50 \\

\end{tabular}"""

    expected = r"""\begin{tabular}
Col1 & \cellcolor{red}Col2 & Col3 \\
0.02 & \cellcolor{blue}0.88 & 0.11 \\
\cellcolor{green}0.65 & 0.02 & 0.94 \\
0.31 & 0.52 & 0.50 \\
\end{tabular}"""

    assert change_color(input_table, [[1, 2], [2, 2], [3, 1]], ['red', 'blue', 'green']) == expected


def test_table_stay_same_when_pairs_empty():
    input_table = r"\begin{tabular} Col1 & Col2 & Col3 \\ \end{tabular}"

    expected = r"""\begin{tabular}
Col1 & Col2 & Col3 \\
\end{tabular}"""

    assert change_color(input_table, [], []) == expected


def test_support_extra_table_property():
    input_table = r"\begin{tabular}{rrr} Col1 & Col2 & Col3 \\ \end{tabular}"

    assert "{rrr}" in change_color(input_table, [], [])
