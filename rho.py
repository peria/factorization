#!/usr/bin/env python

# Implementation of Pollard's rho method.

import fractions
import sys


def succ(x, n):
  """A successor of a series.  It can depend on the previous item."""
  return (x * x * x + 1) % n


def factor(n):
  x = 2
  y = succ(x, n)
  for i in xrange(100):
    pp = 1
    for j in xrange(10):
      pp = pp * abs(x - y) % n
      x = succ(x, n)
      y = succ(succ(y, n), n)
    p = fractions.gcd(n, pp)
    if p == 1 or p == n:
      continue

    q = n / p
    if p > q:
      (p, q) = (q, p)
    return [p, q]
  return [n]
    
  
if __name__ == "__main__":
  n = int(raw_input())
  factors = factor(n)
  print factors
