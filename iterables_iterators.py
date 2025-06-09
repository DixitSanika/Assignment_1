from itertools import combinations

def probability_of_a():
    n = int(input("Enter how many letters you want: "))
    letters = input("Please type the letters, separated by spaces: ").split()
    k = int(input("Enter how many letters do you want to pick at a time: "))


    all_combinations = list(combinations(letters, k))

    count_with_a = 0
    for group in all_combinations:
        if 'a' in group:
            count_with_a += 1  
    if len(all_combinations) > 0: 
        probability = count_with_a / len(all_combinations)
    else:
        probability = 0  

    print(f"The chance of picking at least one 'a' is: {probability:.4f}")
probability_of_a()