#!/usr/bin/env python

from pylab import *



Ho = 1
B = 100.0
f_0 = 200.0
a = 0.8
H_gen = lambda f: sqrt(a / (1 + ((f - f_0) ** 2) / (B / 2) ** 2))
f = arange(1, 10000)

H_200_100 = H_gen(f)
h_200_100 = irfft(H_200_100)

f_0 = 1000
H_1000_100 = H_gen(f)
h_1000_100 = irfft(H_1000_100)

B=10
f_0 = 200
H_200_10 = H_gen(f)
h_200_10 = irfft(H_200_10)

plot(h_200_100, label="f_0 = 200 Hz, B = 100 Hz")
plot(h_1000_100, label="f_0 = 1000 Hz, B = 100 Hz")
plot(h_200_10, label="f_0 = 1000 Hz, B = 10 Hz")
legend()
show()
