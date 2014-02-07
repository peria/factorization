#!/usr/bin/env python

import rho
import p_one
import sys
import trial

if __name__ == "__main__":
  n0 = n1 = n2 = nn = 0
  for line in sys.stdin:
    line = line.strip()

    n = int(line)
    (p0, n) = trial.factor(n)
    (p1, n) = p_one.factor(n)
    (p2, n) = rho.factor(n)

    if len(p0) > 0:
      n0 += 1
    elif len(p1) > 0:
      n1 += 1
    elif len(p2) > 0:
      n2 += 1
    else:
      nn += 1
  print n0, n1, n2, nn
