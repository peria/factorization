#!/usr/bin/env python

import fractions
import math

def msb(n):
  return 1 << (n.bit_length() - 1)


def solve(data):
  ndata = len(data)
  nbase = len(data[0][1])

  mat = []
  i = 0
  for _, d in data:
    l = 0
    for j in xrange(nbase):
      l = l * 2 + (d[j] % 2)
    l = (l << ndata) + (1 << i)
    i = i + 1
    mat.append(l)

  useful = ndata
  for i in xrange(ndata):
    mat.sort(reverse=True)

    bit = msb(mat[i])
    if bit < (2 << ndata):
      useful = i
      break
    for j in xrange(i + 1, ndata):
      if mat[j] & bit != 0:
        mat[j] = mat[j] ^ mat[i]

  ret = []
  mask = (1 << ndata) - 1
  for i in xrange(useful, ndata):
    ret.append(mat[i] & mask)

  return ret


def getExp(m, s, fb):
  es = [s % 2]
  for p in fb:
    e = 0
    while m % p == 0:
      e = e + 1
      m = m / p
    es.append(e)
  return (m == 1), es


def isqrt(n):
  x = n
  y = (x + 1) // 2
  while y < x:
    x = y
    y = (x + n // x) // 2
  return x


def sieve(n, fb):
  data = []
  sq = isqrt(n)
  q = sq
  x0, x1 = 1, sq
  y0, y1 = 0, 1
  b0, b1 = 0, sq
  m0, m1 = 1, n - sq**2
  s = 0
  while len(data) < len(fb) + 10 and x1 < n * n:
    q = (sq + b1) / m1
    x0, x1 = x1, x0 + q * x1
    y0, y1 = y1, y0 + q * y1
    b0, b1 = b1, m1 * q - b1
    m0, m1 = m1, m0 + q * (b0 - b1)
    smooth, e = getExp(m1, s, fb)
    s = s + 1
    if smooth:
      data.append((x1 % n, e))
  return data


def factor(n):
  base_fb = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271]
  fb = []
  for p in base_fb:
    if pow(n, (p - 1) / 2, p) == 1:
      fb.append(p)
  # print "Factor Base: ", fb
  data = sieve(n, fb)

  # In case we cannot find enough data, the factorization fails.
  if len(data) <= len(fb):
    return [n]

  # print "Data size %d x %d" % (len(data), len(fb) + 1)
  relations = solve(data)
  # print "Got %d relations" % len(relations)
  for r in relations:
    x = 1
    e = [0 for _ in xrange(len(fb))]
    # multipy data in r
    for i in xrange(len(data)):
      if (1 << i) & r == 0:
        continue
      xi, ei = data[i]
      ei = ei[1:]
      x = x * xi
      e = [e0 + e1 for (e0, e1) in zip(e, ei)]
    # gcd
    y = 1
    for p, i in zip(fb, e):
      y = y * pow(p, i / 2, n) % n
    g = fractions.gcd(n, x + y)
    if 1 < g and g < n:
      return sorted([g, n / g])
    g = fractions.gcd(n, x - y + n)
    if 1 < g and g < n:
      return sorted([g, n / g])
  return [n]

if __name__ == "__main__":
  n = int(raw_input())
  factors = factor(n)
  print factors
