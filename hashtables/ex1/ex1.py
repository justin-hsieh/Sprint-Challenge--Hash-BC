#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    # O(n)
    for index in range(length):

        # find the difference between the limit and each weight
        difference = limit - weights[index]

        # check hash table to see if difference value exists as a hash index value
        target = hash_table_retrieve(ht, difference)

        # if value is found in hashtable
        if target is not None:
            # sum of current index weight and target weight should equal limit
            return (index, target)
        # Store the weight inside of a hashtable
        hash_table_insert(ht, weights[index], index)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
