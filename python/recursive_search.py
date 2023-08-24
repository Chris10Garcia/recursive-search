"""
i know how to do this iteratively
    for element in arr:
        if element == target:
            return True
    return False

For recursion you need a basecase....
We can pop the end of the array
if the pop result is the target, return true
if not, then the new array gets passed into the function again
the base case can be if the length of the array == 0, then return False
"""


def recursive_search(arr, target):

    if len(arr) == 0:
        return False

    if arr.pop() == target:
        return True
    else:
        return recursive_search(arr, target)



if __name__ == "__main__":

    test_values = [
        ([1,2,3], 2),
        ([3,2,1], 4),
    ]

    test_answers = [
        True,
        False,
    ]
    

    for value, answer in zip(test_values, test_answers):
        result = recursive_search(*value)
        assert result == answer, f"Test failed for {value}, expecting {answer}, got {result}"
        print(f"Test successful!")