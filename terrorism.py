"""
NAME: AKINTAYO LANRE MOSHOOD
MATRIC NO: 222460
"""
def get_sum(_list):
    summation = 0
    for num in _list:
        summation += int(num)

    return summation

def get_id(feature, index, all_features):
    feature_sum = get_sum(feature)
    id = ""
    for each_index in range(len(all_features)):
        current_feature = all_features[each_index]
        current_feature_sum = get_sum(current_feature)

        if current_feature_sum == feature_sum and feature == current_feature:
            if index != each_index:
                id = each_index + 1
    
    return id

def display_output(all_features, ids):
    print("{0:10} {1:27} {2:10} {3:15} {4:15}".format("S/N", "Features", "Sum", "Similarity ID", "Duplicate"))
    print("_________________________________________________________________________")
    for index in range(len(all_features)):
        current_feature = all_features[index]
        current_id = ids[index]
        summation = get_sum(all_features[index])
        duplicate = all_features.count(current_feature)
        
        print("{0:<10} {1:10} {2:10} {3:10} {4:14}".format(index + 1, ', '.join(current_feature), summation, current_id, duplicate))
        print("_________________________________________________________________________")

def main():
    file = open("terrorist.txt")

    no_of_features = int(file.readline())
    all_features = []
    ids = []

    for index in range(no_of_features):
        feature = file.readline().strip('\n').split(",")
        all_features.append(feature)
    
     
    for each_index in range(len(all_features)):
        feature = all_features[each_index]
        id = get_id(feature, each_index, all_features)
        ids.append(id)

    display_output(all_features, ids)

    file.close()

main()