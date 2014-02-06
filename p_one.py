#!/usr/bin/env python

import fractions
import sys


def modpow(x, k, n):
  """modpow(x, k, n) returns x^k mod n"""
  a = 1
  m = x
  while k > 0:
    if k % 2 == 1:
      a = (a * m) % n
    m = (m * m) % n
    k /= 2
  return a


def core(a, k, n):
  p = fractions.gcd(n, modpow(a, k, n) - 1)
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
