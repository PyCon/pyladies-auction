#!/usr/bin/env python3
"""PyLadies raffle draw

The raffle is run across the duration fo the auction, picking winners durring breaks.

All items in the raffle are in a single pool of items.
There are multiple raffle winners.
When a raffle ticket is pulled the winner comes up and takes an item of their choice from those remaining.
Each person can only win once, no matter how many tickets they purchase.
Each ticket is a single entry in the raffle, so purchasing more tickets increases their odds.
The goal is to have the maximum amount of winners and increase participation.

This used to be done with paper numbered raffle tickets which we ripped appart, mixed in a box and pulled one at a time.
However this was very time consuming, and randomly mixing up ~1K paper tickets is impossible.
This resulted in a number of 'feelbad' moments where numbers close together would be picked in a row.
While this was random, it had the appearence of otherwise. Additionally as each person could only
win once, we would havre to pull more and more tickets to find someone who had not already won.
More 'feelbad' as a person hears/sees a ticket number htey have but already won.

Instead we will have numbered slips on carbonless copy booklets. Tickets can be purchased 
on the slips. This is just a dumber of tickets written on the slip. Adding tickets is adding
a new number of the additional tickets purchased (NO DOING MATH!) When adding tickets,
write down both on the slip and in the record book.

These are entered into a spread sheet. The first column is the slip number, and 
each additional column is a number of tickets. A row can have no number of tickets purchased.

This is saved as a CSV. This script reads that CSV and picks raffle winners.
We could be cleaver and use some of the builtin tools to do a weighted randomization, but 
in the spirit of the raffle we brute force extra work to match the actions of performing
the raffle in real life, with some bennifits.

1. Have a dict of the slips to the total number of tickets on the slip.
2. Each slip number is added to a list for each ticket on the slip.
3. Randomize the list.
4. Pull a winning slip number at random from the random list.
5. Remove the winning slip from the dict.
6. Print out the slip record with the individual numbers in the spreadsheet for validatioan.
6. GOTO 2.



"""
import csv
import random
import itertools
import argparse
import json
import os.path

# We are using a brute force method here.
# we could use random.choices() 
# providing the cummulative weights as the ticket counts, 
# and a k of 1 then prune and re-run, but there are issues 
# with how the calculation is done which while 'fair' are 
# different from a pure random ticket draw.

# So we will over do it. We will ramdomize the sequence
# then pull a random index.
# No this does not make a difference statistically,
# but it does better aproximate the real world actions
# of mixxing up raffle tickets and then randomly drawing one.
# Computers are fast enough

def _load_csv(filename):
    with open(filename, newline="") as csvf:
        for row in csv.reader(csvf):
            row = [x for x in row if x]
            if len(row) <= 1:
                continue
            yield row[0], (sum(int(x, 10) for x in row[1:]), row)

def load_csv(filename):
    """return a dict of:
        {'slip #': (#tickets, ['slip#', 'count', 'count',...]), ...}
    """
    return dict(_load_csv(filename))

def flatten(data, winners):
    """flatten to a list of ['slip #', 'slip #', ...]
    Where the same slip number is repeated for each ticket.
    """
    def iterate_by_count(data):
        for slip, (count, row) in data.items():
            if slip not in winners['ids']:
                yield(itertools.repeat(slip, count))
    return list(itertools.chain.from_iterable(iterate_by_count(data)))

def picks(filename, num, winners):
    """
    """
    # load the csv file into the main data dict.
    data = load_csv(filename)
    num_slips = len(data)
    num_tickets = sum(x[0] for x in data.values())
    print(f'loaded {num_slips} slips with {num_tickets} total tickets.')
    for i in range(num):
        # flatten to a list of slip numbenrs where each slip number is repeated
        # for each ticket in the slip.
        tickets = flatten(data, winners)
        # randomize the list (simulate mixing tickets)
        random.shuffle(tickets)
        # pick one at random
        slip = random.choice(tickets)
        # return the origional raw data from the CSV for the slip.
        yield data[slip][1]
        # delete the winning slip entry from the data.
        del data[slip]
        # add them to the winners
        winners['ids'].append(slip)

DEFAULT_WINNER_COUNT=40

parser = argparse.ArgumentParser()
parser.add_argument('csv',
    help="CSV file containing the slips and counts.")
parser.add_argument('-c', '--count', type=int,
    default=DEFAULT_WINNER_COUNT,
    help="Number of winning slips to pull. "
         f"(default: {DEFAULT_WINNER_COUNT})")
parser.add_argument('-w', '--winners',
    default='winners.json',
    help="Winners tracking file")

if __name__ == "__main__":
    args = parser.parse_args()
    if os.path.exists(args.winners):
        winners = json.load(open(args.winners))
    else:
        winners = {'ids': []}
    for result in picks(args.csv, args.count, winners):
        print(' '.join(result))
    json.dump(winners, open(args.winners, 'w'))

