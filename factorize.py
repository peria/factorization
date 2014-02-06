#!/usr/bin/env python

import p_one
import sys
import trial

if __name__ == "__main__":
  for line in sys.stdin:
    line = line.strip()

    n = int(line)
    (p0, n) = trial.factor(n)
    (p1, n) = p_one.factor(n)

    if n < 2 ** 70:
      print "%s: %s * %s * %d" % (line, p0, p1, n)
