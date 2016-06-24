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

import cfrac
import cProfile
import p_one
import prime
import rho
import sys
import trial


def factorize(n):
  # Trial division.  All elements in [p] are prime.
  (ps, n) = trial.factor(n)

  pps = []  # probable primes
  cs = []   # composites
  # check if n is possibly prime
  if n > 1:
    if prime.IsPrime(n):
      pps.append(n)
    else:
      cs.append(n)

  ccs = []  # composites which could not be factored.
  while len(cs) > 0:
    composites = cs
    cs = []
    for n in composites:
      # try to factor with p-1 method
      factors = p_one.factor(n)
      # try to factor with rho method
      if len(factors) == 1:
        factors = rho.factor_fast(n)
      # try to factor with cfrac method
      if len(factors) == 1:
        factors = cfrac.factor(n)

      # This composite number could not be factored.
      if len(factors) == 1:
        ccs.append(n)
        continue

      # split factors into composites and primes.
      for f in factors:
        if prime.IsPrime(f):
          pps.append(f)
        else:
          cs.append(f)

  ps.sort()
  pps.sort()
  ccs.sort()
  return (ps, pps, ccs)


def main(ns):
  succeed = 0
  for n in ns:
    (p, pp, c) = factorize(n)
    if len(c) == 0:
      succeed += 1
  print "%d / %d succeeded." % (succeed, len(ns))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    argvs = sys.argv
    del argvs[0]
    cProfile.run("main(map(int, sys.argv))")
  else:
    ns = []
    for line in sys.stdin:
      ns.append(int(line.strip()))
    cProfile.run("main(ns)")
