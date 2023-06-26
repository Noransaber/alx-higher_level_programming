def complex_delete(a_dictionary, value):
    del_list = []
    for k, v in a_dictionary:
        if v in value:
            del_list.append(k)
            
    for k in del_list:
        del a_dictionary[k]
    return a_dictionary
