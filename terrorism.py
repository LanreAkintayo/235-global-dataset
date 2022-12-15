"""
NAME: AKINTAYO LANRE MOSHOOD
MATRIC NO: 222460
"""
def get_sum(_list):
    summation = 0
    for num in _list:
        summation += int(num)

    return summation

def get_id(test, index, all_tests):
    test_sum = get_sum(test)
    id = "No ID"
    for each_index in range(len(all_tests)):
        current_test = all_tests[each_index]
        current_test_sum = get_sum(current_test)

        if current_test_sum == test_sum and test == current_test:
            if index != each_index:
                id = each_index + 1
    
    return id

def display_output(all_tests, ids):
    print("\nS/N\t\t\tTests\t\t\t\t\tSum\t\tSimilarity ID")
    print("____________________________________________________________")
    for index in range(len(all_tests)):
        current_test = all_tests[index]
        current_id = ids[index]
        summation = get_sum(all_tests[index])
        
        print(f" {index + 1}        {', '.join(current_test)} \t\t {summation}         {current_id} ")
        print("____________________________________________________________")

def main():
    file = open("terrorist.txt")

    test_cases = int(file.readline())
    all_tests = []
    ids = []

    for test_case_index in range(test_cases):
        test = file.readline().strip('\n').split(",")
        all_tests.append(test)
    

    for each_index in range(len(all_tests)):
        test = all_tests[each_index]
        id = get_id(test, each_index, all_tests)
        ids.append(id)

    display_output(all_tests, ids)

main()