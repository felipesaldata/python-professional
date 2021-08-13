#we need to create a solution that remove duplicates of a list and return the result
#for example
# [1,1,2,2,4] -> [1,2,4]

def remove_duplicates(some_list):
    without_duplicates = []
    for element in some_list:
        if element not in without_duplicates:
            without_duplicates.append(element)
    return without_duplicates


#The challenges is to do the same but with sets


def remove_duplicates_with_sets(some_list):
    return list(set(some_list))

def run():
    random_list = [1,1,2,2,4]
    print("Removing duplicates with for loop: ", remove_duplicates(random_list))
    print("Removing duplicates with sets: ", remove_duplicates_with_sets(random_list))
    
if __name__ == '__main__':
    run()