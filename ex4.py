def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    # create cache and results list
    cache = dict()
    result = []

    # traverse each number in the input array
    for i in a:

        # adding each number to the cache with a value of 1
        cache[i] = 1

        # if current number is not zero and it's inverse is already in the cahce:
        # add current number's absolute value to the result list
        if i != 0 and -i in cache:
            result.append(abs(i))

    # return results list
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
