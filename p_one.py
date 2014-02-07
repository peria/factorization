#!/usr/bin/env python

# Implementation of p-1 method.

import fractions
import sys


def core(x, k, n):
  p = fractions.gcd(n, pow(x, k, n) + n - 1)
  q = n / p
  if p > q:
    (p, q) = (q, p)
  return (p, q)


def factor(n):
  factors = []
  a = 2
  k = 2 ** 10
  for hundred in xrange(0, 500, 100):
    for mod100 in xrange(1, 100, 2):
      k *= hundred + mod100
    (p, n) = core(a, k, n)
    if p > 1:
      factors.append(p)
      if p * p > n:
        break

  return (factors, n)


if __name__ == "__main__":
  n = int(raw_input())
  (factors, p) = factor(n)
  print factors, p
