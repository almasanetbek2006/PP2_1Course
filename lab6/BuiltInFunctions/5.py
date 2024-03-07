def all_true_elements(tuple_data):
    boolean =  True
    for i in tuple_data:
        if i != True:
            boolean = False

    if boolean:
        return True
    else:
        return f"elements of tuple is different"