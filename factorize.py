#!/usr/bin/env python

import prime
import rho
import p_one
import sys
import trial

if __name__ == "__main__":
  n0 = n1 = n2 = np = 0
  for line in sys.stdin:
    line = line.strip()

    n = int(line)
    (p, n) = trial.factor(n)
    if len(p) > 0:
      n0 += 1
    if not prime.IsPrime(n):
      (q, n) = p_one.factor(n)
      if len(q) > 0:
        n1 += 1
      p.extend(q)
    if not prime.IsPrime(n):
      (q, n) = rho.factor(n)
      if len(q) > 0:
        n2 += 1
      p.extend(q)
    if prime.IsPrime(n):
      print "%s: %s * %d" % (line, p, n)
      np += 1

  print n0, n1, n2, np
