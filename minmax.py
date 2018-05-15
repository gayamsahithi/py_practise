num_list = [1,2,3,4,5,6,7,8,9]
def small_no( num_list ):
    min = num_list[0]
    for var in num_list:
        if var < min:
            min = var              
    return min
def large_no( num_list ):
    max = num_list[0]
    for var in num_list:
        if var > max:
            max = var
    return max
print( small_no(num_list) )
print( large_no(num_list) )
