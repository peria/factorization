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
  for i in xrange(1000):
    p = fractions.gcd(n, abs(x - y))
    if p > 1 and p < n:
      q = n / p
      if p > q:
        (p, q) = (q, p)
      return ([p], q)
    x = succ(x, n)
    y = succ(succ(y, n), n)

  # failed
  return ([], n)
    
  
if __name__ == "__main__":
  n = int(raw_input())
  (q, p) = factor(n)
  print [q], p
