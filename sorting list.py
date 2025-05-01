def sort_lst(lst):
    def return_max_list(lstt) :
        maximum = lstt[0]
        for i in lstt :
            if i>maximum :
                maximum = i
        return maximum
    the_sort_list = []
    if not lst :
        
        return "the list is empty"
    else:
        while lst:
            the_max=return_max_list(lst)
            the_sort_list.append(the_max)
            lst.remove(the_max)
            
    return the_sort_list
            
       
       
       
       
# there is another way to sort the list 
def sorting_list(lst):
    for i in range(len(lst)-1):
        for i in range(len(lst)-1):
            if lst[i] < lst[i+1]:
                swp = lst[i] # to swap the two variable 
                lst[i] = lst[i+1]
                lst[i+1] = swp 
    
    return lst


print(sorting_list([9,7,5,111,21,100,4,6,3,700]))            
                
        
    

        
                
                
            