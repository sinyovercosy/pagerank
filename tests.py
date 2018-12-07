from pagerank import rank

def main():
    links = [[1,2,3],[3],[0,3],[0,2]]
    result = rank(links)
    print("testing simple")
    print("INPUT:")
    print(links)
    print("OUTPUT:")
    print(result)
    assert (result == [3, 0, 2, 1])
    print("passed!")

    links = [[1,2,3],[3],[0,3],[]]
    result = rank(links)
    print("testing dangling")
    print("INPUT:")
    print(links)
    print("OUTPUT:")
    print(result)
    assert (result == [3, 0, 2, 1])
    print("passed!")

    links = [[1,2,3], [3,4], [0,3], [1,6], [6], [4,7], [5], [5,6]]
    result = rank(links)
    print("testing reducible")
    print("INPUT:")
    print(links)
    print("OUTPUT:")
    print(result)
    assert (result == [5, 6, 4, 7, 3, 1, 0, 2])
    print("passed!")

    links = [[1, 5], [2, 5], [1, 3, 5], [4], [1, 5], [2, 6], [0, 1]]
    result = rank(links)
    print("testing given sample 1")
    print("INPUT:")
    print(links)
    print("OUTPUT:")
    print(result)
    assert (result == [5, 2, 1, 6, 3, 4, 0] or result == [5, 2, 1, 6, 4, 3, 0])
    print("passed!")

    links = [[1,3,4],[0,2,4],[3,6],[2,4,6],[5,8],[4,6,8],[0,7,9],[0,6,8],[2,9],[0,2,8]]
    result = rank(links)
    print("testing given sample 2")
    print("INPUT:")
    print(links)
    print("OUTPUT:")
    print(result)
    assert (result == [2,6,8,0,3,9,4,5,7,1] or result == [2,6,8,0,4,3,9,5,7,1])
    print("passed!")

if __name__ == "__main__":
    main()
