"""
Implement your solution to the practicum in this file.

@author Oscar Capraro
"""

'''Isaiah Velazquez'''
PHONETIC_ALPHABET = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot",
    "Golf", "Hotel", "India", "Juliett", "Kilo", "Lima", "Mike", "November", 
    "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform", 
    "Victor", "Whiskey", "X-ray", "Yankee", "Zulu"]


def euclidean_distance(a,b):
    if len(a) != len(b):
        return None
    
    distance = 0

    for i in range(len(a)):
        distance += (a[i] - b[i]) ** 2

    distance = distance ** .5
    return distance


def data_sorter(lst):
    alpha_num = {0:"zero", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}
    sorted = False
    while sorted == False:
        sorted = True
        for i in range(len(lst)):
            if i == 0:
                continue
            if alpha_num[lst[i]] < alpha_num[lst[i-1]]:
                switch = lst[i]
                lst[i] = lst[i-1]
                lst[i-1] = switch
                sorted = False
        
    return lst

def main():
    # you may use this function to manually test your code if you feel the need
    # to do so.
    print(euclidean_distance([1,2],[1,5]))
    print(data_sorter([1,2,3,4,5,6]))
    

if __name__ == "__main__":
    main()