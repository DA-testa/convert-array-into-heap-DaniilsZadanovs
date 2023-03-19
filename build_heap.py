# python3


def build_heap(data):
    swaps = []
    n=len(data)
    
    for i in range(n//2,-1,-1):
        sm_data(data,swaps,i)
   
    return swaps

def sm_data(data,swaps,i):
    n=len(data)
    left_n=2*i+1
    right_n=2*i+2
    smallest_n=i
    if left_n<n and data[left_n]<data[smallest_n]:
        smallest_n=left_n
    if right_n<n and data[right_n]<data[smallest_n]:
        smallest_n=right_n
    if smallest_n !=i:
        swaps.append((i,smallest_n))
        data[i],data[smallest_n]=data[smallest_n],data[i]
        sm_data(data,swaps,smallest_n)
    

def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    in_num=input()
    
    if "I" in in_num:
        n=int(input())
        data = list(map(int, input().split()))
    elif "F" in in_num:
        file_name=input()
        if "a" not in file_name:
            with open('/tests/'+file_name,'r') as f:
                n=int(f.readline())
                data=list(map(int,f.readline().split()))
                          
        
    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))

    assert len(swaps)<=4*n
    print(len(swaps))
           
    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
