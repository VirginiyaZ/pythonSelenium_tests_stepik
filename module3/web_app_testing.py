# assert abs(-42) == -42, "Should be absolute value of a number"

# print("Let's count together: {}, then goes {}, and then {}".format("one", "two", "three"))

# str1 = "one"
# str2 = "two"
# str3 = "three"
# print(f"Let's count together: {str1}, then goes {str2}, and then {str3}")

# s = 'My Name is Julia'

# if 'Name' in s:
#     print('Substring found')

# index = s.find('Name')
# if index != -1:
#     print(f'Substring found at index {index}')


# def test_input_text(expected_result, actual_result):
    # assert expected_result == actual_result, f"expected {expected_result}, got {actual_result}"



# def test_abs1():
#     assert abs(-42) == 42, "Should be absolute value of a number" 

# if __name__ == "__main__":
#     test_abs1()
#     print("All tests passed!")



def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"

def test_abs2():
    assert abs(-42) == -42, "Should be absolute value of a number"

if __name__ == "__main__":
    test_abs1()
    test_abs2()
    print("Everything passed")