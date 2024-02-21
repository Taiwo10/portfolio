
# sum list of numbers
def list_sum(num_list):
    # check if the length of input list is 1
    if len(num_list) == 1:
        # if the list has only one element, return that element
        return num_list[0]
    else:
        # if the list has more than one lement, return the sum of the first element and the result of the recursively calling the list_sum function on the rest of the list
        return num_list[0] + list_sum(num_list[1:])
    # printt the result of the calling the list_sum function with the input[2,4,5,6,7]
print(list_sum([2,4,5,6,7]))
    
    # let's see whteher it worked