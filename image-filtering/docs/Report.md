## FIR Low Pass Filter

Analyze and implement a simple low pass filter given by the 9 × 9 point spread function:

$$
h(m, n) = \begin{cases}
    1/81 &\text{for } |m| \leq 4 &\text{and } |n| \leq 4 \\
    0 &\text{otherwise}
\end{cases}
$$

We can plot the magnitude of the impulse response by finding the analytical expression for $H(e^{ju}, e^{jv})$ across all values, which is the DSFT:

$$
H(u, v) = \sum_{n=-\infin}^{\infin} \sum_{m=-\infin}^{\infin} f(n, m) e^{-j2\pi(\frac{un}{N} + \frac{vm}{M})}
$$

We can substitute $\frac{1}{81}$ within the range $-4\leq{n,m}\leq4$ since that is the only non-zero piece of the function and get the following:

$$
H(u, v) = \sum_{n=-4}^{4} \sum_{m=-4}^{4} \frac{1}{81} e^{-j2\pi(\frac{un}{9} + \frac{vm}{9})}
$$

