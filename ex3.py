def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    # create cache to store the amount of times a number is used
    cache = dict()

    # traverse each sublist in the input array
    for list in arrays:

        # traverse each number in the sublists
        for num in list:

            # if number exists in cache increase count by 1
            if num in cache:
                cache[num] += 1
            # else set count to 1 at the current index in cache
            else:
                cache[num] = 1
            
    # create result list for itersection numbers
    result = []

    # create a list of key value tuples for numbers and their respective counts
    for tuple in cache.items():

        # if the current numbers count = length of the input array
        # add current number to result
        if tuple[1] == len(arrays):
            result.append(tuple[0])
        # else continue the loop
        else:
            continue 

    # return intersection numbers in result
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
