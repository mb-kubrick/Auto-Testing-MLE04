def how_many_shared_lists(list_a, list_b):
    num_shared_lists = 0
    for a in list_a:
        if type(a) == list:
            for b in list_b:
                if a is b:
                    num_shared_lists += 1

    return num_shared_lists
