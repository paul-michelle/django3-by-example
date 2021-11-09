# from collections import namedtuple
# from random import choice
#
# Card = namedtuple('Card',['rank', 'suit'])
#
# class FrenchDeck:
#
#     ranks = [str(i) for i in range(2, 11)] + list('JQKA')
#     suits = 'spades diamonds clubs hearts'.split()
#
#     def __init__(self):
#         self._deck = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
#
#     def __getitem__(self, index):
#         return self._deck[index]
#
#     def __len__(self):
#         return len(self._deck)
#
#
# deck = FrenchDeck()

# suit_values = dict(spades=3, hearts =2, diamonds=1, clubs=0)
#
# def spades_high(card):
#     rank_value = FrenchDeck.ranks.index(card.rank)
#     return rank_value*len(suit_values) + suit_values[card.suit]

# for card in sorted(deck, key=spades_high):
#     print(card)
#
# #_________________________page 71-72________________________________
# import bisect
# import sys
#
# HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
# NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]
#
# ROW_FMT = '{0:5d} @ {1:2d} {2} {0:<2d}'
#
# def demo(bisect_fn):
#     for needle in reversed(NEEDLES):
#         position = bisect_fn(HAYSTACK, needle)
#         offset = position * '  |'
#         print(ROW_FMT.format(needle, position, offset))
#
# if __name__ == '__main__':
#
#     if sys.argv[-1] == 'left':
#         bisect_fn = bisect.bisect_left
#     else:
#         bisect_fn = bisect.bisect
#
# print('DEMO:', bisect_fn.__name__)
# print("haystack ->", ' '.join('%2d' % n for n in HAYSTACK))
# demo(bisect_fn)
# #______________________________________________________________
# import bisect
#
#
# def get_score_in_alpha(score, borders=[60, 70, 80, 90], score_in_alpha = 'EDCBA'):
#     index = bisect.bisect(borders, score)
#     return score_in_alpha[index]
#
# scores = [45, 99, 76 , 67, 80, 95, 82, 55, 100]
# for score in scores:
#     print(get_score_in_alpha(score))
# #__________________________________________________________________
# import bisect
# import random
#
# SIZE = 7
#
# random.seed(1729) # pseudo-random!!!
#
# my_list = []
# for i in range(SIZE):
#     new_item = random.randrange(SIZE*2)
#     bisect.insort(my_list, new_item)
#     print(f'{new_item} ---> {my_list}')
# #______________________________________________________________________

# from array import array
# from random import random
#
# floats = array('d', (random() for i in range(10**7)))
# with open('floats.bin', 'wb') as file:
#     floats.tofile(file)
# floats2 = array('d')
# with open('floats.bin', 'rb') as file:
#     floats2.fromfile(file, 10**7)
#
# print(floats == floats2)
#____________________________________________________________________________

