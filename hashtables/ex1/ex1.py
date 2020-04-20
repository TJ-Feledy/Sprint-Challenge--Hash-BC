#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    # loop through weights using index and value
    for i, weight in enumerate(weights):
        # iterate through weights and add each weight to hashtable
        # check to see if weight already exists in the hashtable
            # if exists return tuple
        if hash_table_retrieve(ht, weight) is not None:
            j = hash_table_retrieve(ht, weight)

            return (i, j)
        # create key and insert the weight
        key = limit - weight
        hash_table_insert(ht, key, i)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
