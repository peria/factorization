#!/usr/bin/env python

import optparse
import random

def ParseOption():
  parser = optparse.OptionParser()
  parser.add_option("-b", "--bits", dest="bits", default=100,
                    help="bit lengths of generated numbers.")
  parser.add_option("-n", "--number", dest="number", default=0,
                    help="number of generated random numbers.")
  parser.add_option("-s", "--seed", dest="seed", default=0,
                    help="seed nubmer for random generator.")
  return parser.parse_args()


def main():
  (options, args) = ParseOption()

  random.seed(int(options.seed))
  if options.number > 0:
    for i in xrange(int(options.number)):
      print random.getrandbits(int(options.bits))
  elif len(args) > 0:
    for n in map(int, args):
      print random.getrandbits(n)

      
if __name__ == "__main__":
  main()
  
