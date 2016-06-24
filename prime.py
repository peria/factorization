#!/usr/bin/env python

def MillerRabin(a, d, s, n):
  r = pow(a, d, n)
  if r == 1:
    return True
  for i in range(s):
    if r == n - 1:
      return True
    if r == 1:
      return False
    r = r * r % n
  return False


def IsPrime(n):
  if n < 2:
    return False
  if n == 2:
    return True  # 2 is prime
  if n % 2 == 0:
    return False

  # Miller-Rabin test
  d = n - 1
  s = 0
  while d % 2 == 0:
    d /= 2
    s += 1
  for a in [2, 3, 5, 7]:
    if not MillerRabin(a, d, s, n):
      return False
  return True  # probable prime


if __name__ == "__main__":
  n = int(raw_input())
  if IsPrime(n):
    print "%d is probable prime." % n
  else:
    print "%d is compostite." % n
