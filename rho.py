#!/usr/bin/env python

# Implementation of Pollard's rho method.

import fractions
import sys


def succ(x, n):
  """A successor of a series.  It can depend on the previous item."""
  return (x * x + 1) % n


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
    if p == 1:
      continue
    if p == n:
      break

    q = n / p
    if p > q:
      (p, q) = (q, p)
    return [p, q]

  return [n]


def factor_fast(n):
  x = 1
  y = 1
  k = 1
  pp = 1
  for i in xrange(10):
    y = x
    for i in xrange(k):
      x = succ(x, n)
    for i in xrange(k):
      x = succ(x, n)
      pp = pp * abs(x - y) % n

    p = fractions.gcd(n, pp)
    if p == n:
      break
    if p == 1:
      x = succ(x, n)
      k *= 2
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
