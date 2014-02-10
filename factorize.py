#!/usr/bin/env python

"""
factorize input numbers using many algorithms.

try to factorize input numbers using following algorithms in this order.
 * Trial division
 * p-1 method
 * Pollard's rho method
If output of each algorithm is not surely prime, it will be checed if it
is composite with Miller-Rabin's test.
If any of output factor is judged composite, it will be reported.
"""


import p_one
import prime
import rho
import sys
import trial


def main(ns):
  n0 = n1 = n2 = 0
  for n in ns:
    m = n
    # Trial division.  All elements in [p] are prime.
    (p, n) = trial.factor(n)

    # If n is composite, it will be factored with p-1 method.
    if n == 1 or prime.IsPrime(n):
      n0 += 1
    else:
      (q, n) = p_one.factor(n)
      p.extend(q)

    # If n is still composite, it will be factored with rho method.
    if n == 1 or prime.IsPrime(n):
      n1 += 1
    else:
      (q, n) = rho.factor(n)
      p.extend(q)

    # If n is still composite, it will be reported.
    if n == 1 or prime.IsPrime(n):
      n2 += 1
    else:
      if len(p) == 0:
        print "%s: (composite)" % m

  print n0, n1 - n0, n2 - n1, len(ns) - n2


if __name__ == "__main__":
  if len(sys.argv) > 1:
    argvs = sys.argv
    del argvs[0]
    main(map(int, sys.argv))
  else:
    ns = []
    for line in sys.stdin:
      ns.append(int(line.strip()))
    main(ns)
