## FIR Low Pass Filter

Analyze and implement a simple low pass filter given by the 9 × 9 point spread function

$$
h(m, n) = \begin{cases}
    1/81 &\text{for } |m| \leq 4 &\text{and } |n| \leq 4 \\
    0 &\text{otherwise}
\end{cases}
$$

The analytical expression for ...

$$
F(u, v) = \sum_{n=-4}^{4} \sum_{m=-4}^{4} f(n, m) e^{-j2\pi(\frac{un}{N} + \frac{vm}{M})}
$$