"""
NAME: AKINTAYO LANRE MOSHOOD
MATRIC NO: 222460
"""
import numpy as np
import matplotlib.pyplot as plt

def get_sum(_list):
    summation = 0
    for num in _list:
        summation += int(num)

    return summation

def get_unique_features(all_features):
    unique_features = []
    for each_feature in all_features:
        if each_feature not in unique_features:
            unique_features.append(each_feature)
    return unique_features

def get_labels(all_features):
    labels = []
    for each_feature in all_features:
        labels.append(",".join(each_feature))
    return labels


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

def display_feature_with_duplicate(all_features, ids):
    unique_features = get_unique_features(all_features)

    print("\n\nFeatures and its Duplicates")
    print("{0:10} {1:27}  {2:15}".format("S/N", "Features",  "Duplicate"))
    print("______________________________________________________")
    for index in range(len(unique_features)):
        current_feature = unique_features[index]
        current_id = ids[index]
        summation = get_sum(unique_features[index])
        duplicate = all_features.count(current_feature)
        
        print("{0:<10} {1:10} {2:10}".format(index + 1, ', '.join(current_feature),  duplicate))
        print("_____________________________________________________")

def draw_chart(s_n, duplicates, bar_labels):
    x = np.arange(len(s_n))  # the label locations
    width = 0.5  # the width of the bars

    fig, ax = plt.subplots()
    fig.set_figheight(15)
    fig.set_figwidth(15)
    hbars = ax.bar(x, duplicates, width, align='center')
    
    ax.bar(x, duplicates, width, label="features", color="#1a001a")

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Duplicates')
    ax.set_xlabel("S/N")
    ax.set_title('A graph showing global Terrorism data set')
    ax.set_xticks(x, s_n)
    ax.legend()

    ax.bar_label(hbars, labels=bar_labels,
                padding=1, color='#1a001a')

    plt.show()


def main():
    file = open("terrorist.txt", "r")

    no_of_features = int(file.readline())
    all_features = []
    ids = []
    duplicates = []


    for index in range(no_of_features):
        feature = file.readline().strip('\n').split(",")
        all_features.append(feature)
    
    unique_features = get_unique_features(all_features)
    
     
    for each_index in range(len(all_features)):
        feature = all_features[each_index]
        id = get_id(feature, each_index, all_features)
        ids.append(id)

    for each_index in range(len(unique_features)):
        feature = unique_features[each_index]
        duplicates.append(all_features.count(feature))

    display_output(all_features, ids)

    display_feature_with_duplicate(all_features, ids)
   
    s_n = list(range(1, len(get_unique_features(all_features))+1))
    labels = get_labels(unique_features)
    draw_chart(s_n, duplicates, labels )

    file.close()

main()