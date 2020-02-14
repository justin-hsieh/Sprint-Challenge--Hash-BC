#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    # insert ticket key, values into hastable
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    # index first value of route with value associated with NONE key
    route[0] = hash_table_retrieve(hashtable, 'NONE')

    # loop through the rest of the cities and retrieve associated key, values
    # Use previous destintation as lookup for next destination
    for index in range(1, length):
        
        route[index] = hash_table_retrieve(hashtable, route[index-1])
    
    # return final route without None values
    return route[0:length-1]

    
