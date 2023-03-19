# python3


def build_heap(data):
    swaps = []
    n=len(data)
    
    for i in range(n//2,-1,-1):
        sm_data(data,swaps,n,i)
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)

    return swaps

def sm_data(data, swaps, n, i):
    n=len(data)
    left_n=2*i*2
    right_n=2*i+1
    smallest_n=i
    if left_n<n and data[left_n]<data[smallest_n]:
        smallest_n=left_n
    if right_n<n and data[right_n]<data[smallest_n]:
        smallest_n=right_n
    if smallest_n !=i:
        swaps.append((i,smallest_n))
        data[i],data[smallest_n]=data[smallest_n],data[i]
        sm_data(data,swaps,n,smallest_n)
    

def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file


    # input from keyboard
    n = int(input())
    data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
