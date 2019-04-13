import pdb

def rotate_by_one(list_numbers, n):
    temp = list_numbers[0]
    for i in range(n-1):
        list_numbers[i] = list_numbers[i+1]
    list_numbers[n-1] = temp

def rotate_left(list_numbers,k):
    for i in range(k):
        rotate_by_one(list_numbers,len(list_numbers))
        
    
def printArray(arr, size): 
    for i in range(size): 
        print ("% d"% arr[i], end =" ")  


def main():
	c = [1, 2, 3, 4, 5, 6, 7]
	pdb.set_trace()
	rotate_left(c,2)
	printArray(c,len(c))


   
# Driver program to test above functions */ 

if __name__ == '__main__':
	main()
    


