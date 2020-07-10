#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    # create cache to store flights
    # create list of none for route
    cache = dict()
    route = [None] * length

    # add each flight to cache using tickets using source, key and destination as its value
    for ticket in tickets:
        cache[ticket.source] = ticket.destination

    # start at the first flight that has a key of None
    current_flight = cache['NONE']

    # traverse each element in route
    # overwrite it with the current flight
    # update the current_flight variable
    # continue the loop
    for i in range(length):
        route[i] = current_flight
        current_flight = cache[current_flight]
    
    # return the updated route
    return route
