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
  k = 1
  for i in xrange(100):
    k *= i + 1

  factors = []
  for a in xrange(2, 13):
    (p, n) = core(a, k, n)
    if p > 1:
      factors.append(p)

  return (factors, n)

  
if __name__ == "__main__":
  n = int(raw_input())
  (factors, p) = factor(n)
  print factors, p
