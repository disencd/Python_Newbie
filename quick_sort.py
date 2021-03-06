__author__ = 'c_disenc'

import random

def quick_sort(items):
    """ Implementation of quick sort """
    if len(items) > 1:
        pivot_index = int(len(items) / 2)
        smaller_items = []
        larger_items = []

        for i, val in enumerate(items):
            if i != pivot_index:
                if val < items[pivot_index]:
                    smaller_items.append(val)
                else:
                    larger_items.append(val)

        quick_sort(smaller_items)
        quick_sort(larger_items)
        items[:] = smaller_items + [items[pivot_index]] + larger_items

if __name__ == '__main__':
    random_items = [random.randint(-50, 100) for c in range(10)]

    print ('Before: ', random_items)
    quick_sort(random_items)        # Replace the funtion name here to
                                        # try any of the other algorithms
    print ('After : ', random_items)
