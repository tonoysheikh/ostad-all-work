def merge_dict(dict1 , dict2):
    new_dict = dict1.copy()
    new_dict.update(dict2)
    return new_dict
    # dict1.update(dict2)
    # return dict1
    

dict1 = {
    "a" : 1,
    "b" : 2
}
dict2 = {
    "b" : 3,
    "d" : 4
}
print(merge_dict(dict1 , dict2))