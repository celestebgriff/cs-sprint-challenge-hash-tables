def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    # create cache using dict
    n = len(weights)
    cache = dict()

    # traverse through the weights
    for i in range(n):
        current_weight = weights[i]

        # add current weight if not in cache
        if current_weight not in cache:
            cache[current_weight] = i

        counter_weight  = limit - current_weight

        # if the counter weight is already in the cache and value is not i
        if counter_weight in cache and cache[counter_weight] is not i:
            counter_weight = cache[counter_weight]

            # if i is greater than or equal to the counter weight
            if i >= counter_weight:
                return [i, counter_weight]
            # else counter weight is greater than i
            else:
                return [cache[counter_weight], i]
            
    # if pair does not exist for the given input weights return none
    return None
