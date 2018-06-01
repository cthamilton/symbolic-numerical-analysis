This repository is dedicated to showing application of symbolic math to numerical analysis.

Currently there are two REPL languages that I think could be used for numerical analysis and have native symbolic math packages. These are MATLAB and Python. 

Numerical analysis could obviously be done in other languages, like Julia, and there are a number of languages that focus on symbolic math, like Maple. While one might be able to implement code to do similar things in these languages, I don't currently see great motivation for implementing these codes in other languages. This may also reflect my biases at the time.

Why don't more people use symbolic math for numerical analysis? Namely speed, these codes give you flexibility; however, this flexibility comes at the cost of speed. On top of that, "hard core" numerical analysis is generally implemented in a lower level language, like C++ or Fortran.

I don't intend to deliberately develop a large code base for this repository myself (pull requests welcome), but I will include examples as they become available.

Why? My hope is that a greater use of symbolic math (especially for numerical analysis) could lead to better processor optimization for these operations.