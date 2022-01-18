from my_utils.memory import how_many_shared_lists

def test_with_one_shared_list():
    x = [3]
    list_a = [1,2,x]
    list_b = [1,2,x]
    actual_result = how_many_shared_lists(list_a,list_b)
    expected_result = 1
    assert actual_result==expected_result
    
def test_with_zero_shared_lists():
    list_c = [4,5]
    list_d = [6,7]
    actual_result = how_many_shared_lists(list_c,list_d)
    expected_result = 0
    assert actual_result==expected_result