#!/usr/bin/env python

def IsPrime(n):
  if n < 2:
    return False
  if n == 2:
    return True  # 2 is prime
  if n % 2 == 0:
    return False

  # Millar-Rabin test
  d = n - 1
  while d % 2 == 0:
    d /= 2
  for a in [2, 3, 5, 7]:
    r = pow(a, d * 2, n)
    if r != 1:
      return False

  return True  # probable prime

if __name__ == "__main__":
  n = int(raw_input())
  if IsPrime(n):
    print "%d is probable prime." % n
  else:
    print "%d is compostite." % n
  

  
