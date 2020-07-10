# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    # create cache and result list
    cache = dict()
    result = []

    # traverse each path in the files input array
    for path in files:

        # each path stores a filename at the end
        # split each path at / and grab filename at -1 index
        split_up_path = path.split("/")
        path_filename = split_up_path[-1]

        # if current filename is not in cache
        # add it to cache with a value of an empty list
        if path_filename not in cache:
            cache[path_filename] = []

        # append current path to the cache
        # use filename as its key and current path as its value
        cache[path_filename].append(path)

    # traverse each filename in the queries input array
    for query_filename in queries:

        # if the filename is already in cache extend the result list
        # add the list of paths stored at the current index in the cache
        if query_filename in cache:
            result.extend(cache[query_filename])

    # return the queried filenames
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
