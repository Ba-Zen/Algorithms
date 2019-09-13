#!/usr/bin/python

import argparse

def find_max_profit(prices):
  curr_min = prices[0]
  max_prof = prices[1] - curr_min
  for p in range(len(prices)):
    for x in range(p + 1, len(prices)):
      if prices[x] - prices[p] > max_prof:
        max_prof = prices[x] - prices[p]

  return max_prof

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))