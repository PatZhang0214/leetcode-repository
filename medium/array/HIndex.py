def hIndex(citations: List[int]) -> int:
    '''
    [3, 0, 6, 1, 5]
    sort
    [6, 5, 3, 1, 0] i = 5
    
    [1,3,1]
    sort
    [3, 1, 1] i = 3
    
    [6, 5, 3, 1]
    [1, 3, 5, 6]
    i = 0, at least 1 paper with 1 citation
    i = 1, at least 2 papers with 2 citations
    i = 2, at least 3 papers with 3 citations
    
    [4, 4]
    '''
    citations.sort(reverse=True)
    count = 0
    for i in range(len(citations)):
        if citations[i] >= (i + 1):
            count += 1
    return count

if __name__ == '__main__':
    print(hIndex([0]))