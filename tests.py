from pagerank import rank

def main():
    links = [[1,2,3],[3],[0,3],[0,2]]
    result = rank(links)
    print("testing simple")
    assert (result == [3, 0, 2, 1])
    print("passed!")

    links = [[1,2,3],[3],[0,3],[]]
    result = rank(links)
    print("testing dangling")
    assert (result == [3, 0, 2, 1])
    print("passed!")

    links = [[1,2,3], [3,4], [0,3], [1,6], [6], [4,7], [5], [5,6]]
    result = rank(links)
    print("testing reducible")
    assert (result == [5, 6, 4, 7, 3, 1, 0, 2])
    print("passed!")

if __name__ == "__main__":
    main()