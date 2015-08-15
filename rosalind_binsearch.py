from bisect import bisect_left

def binary_search(a, x, lo=0, hi=None):    
    hi = hi if hi is not None else len(a)  
    pos = bisect_left(a,x,lo,hi)           
    return (pos if pos != hi and a[pos] == x else -1) 



if __name__ == '__main__':

    # Read the input data.
    with open('C:\\Users\\dmitry.shulgin\\Desktop\\test.txt') as input_data:
        n, m = [int(input_data.readline().strip()) for repeat in xrange(2)]
        A = map(int, input_data.readline().strip().split())
        k = map(int, input_data.readline().strip().split())
    

    result = [binary_search(A, k_i) for k_i in k]

   
    result = [str(index + 1) if index >= 0 else str(-1) for index in result]
    print result
