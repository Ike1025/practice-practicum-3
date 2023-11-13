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
    lst1 = lst[:]
    lst2 = lst[:]

    while sorted == False:
        sorted = True
        for i in range(len(lst)):
            if i == 0:
                continue
            if alpha_num[int(str(lst[i])[0])] < alpha_num[int(str(lst[i-1])[0])]:
                switch = lst[i]
                lst[i] = lst[i-1]
                lst[i-1] = switch
                sorted = False


    sorted = False
    while sorted == False:
        sorted = True
        for i in range(len(lst1)):
            if i == 0:
                continue
            if int(str(lst1[i])[0]) < int(str(lst1[i-1])[0]):
                switch = lst1[i]
                lst1[i] = lst1[i-1]
                lst1[i-1] = switch
                sorted = False
            elif int(str(lst1[i])[0]) == int(str(lst1[i-1])[0]):
                for j in range(len(str(lst[i]))):
                    if j == 0:
                        continue

                    try:
                        if int(str(lst1[i])[j]) < int(str(lst[i])[j-1]):
                            switch = lst1[i]
                            lst1[i] = lst1[i-1]
                            lst1[i-1] = switch
                            sorted = False

                    except:
                        if len(str(lst1[i])) < len(str(lst[i-1])):
                            switch = lst1[i]
                            lst1[i] = lst1[i-1]
                            lst1[i-1] = switch
                            sorted = False

        
    return lst, lst1


def phonetic_translation(a_str):
    alpha_lst = []
    for chr in a_str:
        chr = chr.upper()
        for item in PHONETIC_ALPHABET:
            if chr == item[0]:
                alpha_lst.append(item)


    return alpha_lst




def main():
    # you may use this function to manually test your code if you feel the need
    # to do so.
    print(euclidean_distance([1,2],[1,5]))
    print(data_sorter([6,55,45,41,3,2,1]))
    print(phonetic_translation("alpha"))
    

if __name__ == "__main__":
    main()