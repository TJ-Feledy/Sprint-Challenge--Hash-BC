#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * (length-1)

    # Iterate through each ticket
    for ticket in tickets:
        # insert an element into the hashtable using source and destination as key and value.
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    source = None
    last_destination = 'NONE'

    # for each node in the hashtable
    for i in range(length-1):
        # set the source to equal the last_destination
        source = hash_table_retrieve(hashtable, last_destination)
        print(source)
        # set the route at current index to equal the source
        route[i] = source
        # set the last_destination to now equal the current source
        last_destination = source

    return route
