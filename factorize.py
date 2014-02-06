#!/usr/bin/env python

import rho
import p_one
import sys
import trial

if __name__ == "__main__":
  for line in sys.stdin:
    line = line.strip()

    n = int(line)
    (p0, n) = trial.factor(n)
    (p1, n) = p_one.factor(n)
    (p2, n) = rho.factor(n)

    if len(p0) == 0 and len(p1) == 0 and len(p2) == 0:
      print "%s: %s * %s * %s * %d" % (line, p0, p1, p2, n)
