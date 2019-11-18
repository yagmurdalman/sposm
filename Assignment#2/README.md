# Assignment II

I develop a function that will take

- a latex table (in plain text),
- a list of number pairs containing row and column indices to identify cells, and
- a list of colors
and returns a plain text latex table with the content of the indicated cells colored with the desired colors.


## How to run the assignment:

After successfully building and running docker:

Copy my assignment
```
docker cp /path/to/YDalman_Assignment2.py sposm:/YDalman_Assignment2.py
```

Run with sample input
```
docker exec sposm python3 /YDalman_Assignment2.py
```

Run the tests

```
docker cp /path/to/test.py sposm:/test.py
docker exec sposm pytest /test.py
```

### Example usage

```
latex_table = r"""
\begin{tabular}
 Col1 & Col2 & Col3 \\
 0.02 & 0.88 & 0.11 \\
 0.65 & 0.02 & 0.94 \\
 0.31 & 0.52 & 0.50 \\

\end{tabular}"""
final_table = change_color(latex_table, [[1, 2], [2, 2], [3, 1]], ['red', 'blue', 'green'])
print(final_table)
```

