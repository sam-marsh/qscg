# qscg
Decomposes sparse Hamiltonians into a sum of *O(d^2)* 1-sparse Hamiltonians, where *d* is the bound on the number of non-zero elements per row, for use in simulation.

A trivial example:

![](https://tex.s2cms.ru/svg/%20%5Cbegin%7Bbmatrix%7D%200%20%26%200%20%26%201%20%26%200%20%5C%5C%200%20%26%200%20%26%201%20%26%201%20%5C%5C%201%20%26%201%20%26%200%20%26%200%20%5C%5C%200%20%26%201%20%26%200%20%26%200%20%5Cend%7Bbmatrix%7D%20%3D%20%5Cbegin%7Bbmatrix%7D%200%20%26%200%20%26%201%20%26%200%20%5C%5C%200%20%26%200%20%26%200%20%26%200%20%5C%5C%201%20%26%200%20%26%200%20%26%200%20%5C%5C%200%20%26%200%20%26%200%20%26%200%20%5Cend%7Bbmatrix%7D%20%2B%20%5Cbegin%7Bbmatrix%7D%200%20%26%200%20%26%200%20%26%200%20%5C%5C%200%20%26%200%20%26%201%20%26%200%20%5C%5C%200%20%26%201%20%26%200%20%26%200%20%5C%5C%200%20%26%200%20%26%200%20%26%200%20%5Cend%7Bbmatrix%7D%20%2B%20%5Cbegin%7Bbmatrix%7D%200%20%26%200%20%26%200%20%26%200%20%5C%5C%200%20%26%200%20%26%200%20%26%201%20%5C%5C%200%20%26%200%20%26%200%20%26%200%20%5C%5C%200%20%26%201%20%26%200%20%26%200%20%5Cend%7Bbmatrix%7D)

At the moment, the code is entirely undocumented and extremely hard to read! I plan to rewrite and also add the second step, which is to decompose these 1-sparse Hamiltonans into a series of fundamental quantum gates. The long-term goal of this library is to provide an easy way to input a sparse Hamiltonian and obtain the quantum circuit to simulate it.

[1] D. W. Berry, G. Ahokas, R. Cleve, and B. C. Sanders, “Efficient Quantum Algorithms for Simulating Sparse Hamiltonians,” Communications in Mathematical Physics, vol. 270, no. 2, pp. 359–371, Dec. 2006.
