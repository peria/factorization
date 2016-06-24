#!/usr/bin/env python

import sys

def factor(n):
  p = 2
  factors = []
  while p * p <= n and p < 1000:
    while (n % p == 0):
      factors.append(p)
      n /= p
    p += 1
  if n < 1000 ** 2:
    factors.append(n)
    n = 1
  return (factors, n)


if __name__ == "__main__":
  n = int(raw_input())
  (factors, p) = factor(n)
  print factors, p
