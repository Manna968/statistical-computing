dict = {"FirstName": "Mohamed", "lastName":"Farag", "birthYear": 1990, "nationality": "Egyptian"}

def delete_keys(list, dictionary):
    tem = dictionary.copy()
    if (len(list) == 0):
        return dictionary
    for key in list:
        if key in dictionary.keys():
            tem.pop(key)

    return tem

print(delete_keys(["lastName", "birthYear"], dict))
