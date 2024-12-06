# Python: Robust Average Calculation
This repository demonstrates a common error in Python when calculating averages and provides a robust solution.  The `bug.py` file shows the initial flawed code, susceptible to errors when processing empty lists or lists containing non-numeric data. The `bugSolution.py` offers an improved version that handles these exceptions gracefully, making the function more reliable.  The core issue is that the original code does not perform checks on the input list before performing the calculations, potentially resulting in runtime errors.