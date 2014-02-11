#!/usr/bin/env python

"""
factorize input number using p-1 method

For an input composite number n=p*q, this program may output p and q.
Assuming k mod (p-1) = 0, a^k mod p = 1.  If a^k mod n != 1, we can
get p from GCD(a^k-1, n).

The most important part of p-1 method is how to make up k.
"""


import fractions
import sys


def check(x, k, n):
  p = fractions.gcd(x + n - 1, n)
  q = n / p
  if p > q:
    (p, q) = (q, p)
  return (p, q)


def factor(n):
  factors = []
  a = pow(2, 2 ** 10, n)
  for hundred in xrange(0, 600, 100):
    k = 1
    for mod100 in xrange(1, 100, 2):
      k *= hundred + mod100
    a = pow(a, k, n)
    (p, n) = check(a, k, n)
    if p > 1:
      factors.append(p)
  factors.append(n)
  return factors


if __name__ == "__main__":
  n = int(raw_input())
  factors = factor(n)
  print factors
