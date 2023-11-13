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


def alphanumeric_key(e):
    return ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"][int(str(e)[0])]


def digit_sort(e):
    return -10000*len(str(e))+e

def data_sorter(data):
    
    
    lst = sorted(data, key=alphanumeric_key)
    lst1 = sorted(data, key=digit_sort)



    







    # alpha_num = {0:"zero", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}
    # sorted = False
    # lst = data[:]
    # lst1 = data[:]

    # while sorted == False:
    #     sorted = True
    #     for i in range(len(lst)):
    #         if i == 0:
    #             continue
    #         if alpha_num[int(str(lst[i])[0])] < alpha_num[int(str(lst[i-1])[0])]:
    #             switch = lst[i]
    #             lst[i] = lst[i-1]
    #             lst[i-1] = switch
    #             sorted = False

    # sorted = False
    # while sorted == False:
    #     sorted = True
    #     for i in range(len(lst1)):
    #         if i == 0:
    #             continue

    #         if len(str(lst1[i])) > len(str(lst1[i-1])):
    #             switch = lst1[i]
    #             lst1[i] = lst1[i-1]
    #             lst1[i-1] = switch
    #             sorted = False

    #         elif len(str(lst1[i])) == len(str(lst1[i-1])):
    #             if lst1[i] < lst1[i-1]:
    #                 switch = lst1[i]
    #                 lst1[i] = lst1[i-1]
    #                 lst1[i-1] = switch
    #                 sorted = False


    

        
    return lst, lst1


def phonetic_translation(a_str):
    # alpha_lst = []
    # for chr in a_str:
    #     chr = chr.upper()
    #     for item in PHONETIC_ALPHABET:
    #         if chr == item[0]:
    #             alpha_lst.append(item)


    # return alpha_lst
    
    return [PHONETIC_ALPHABET[ord(char)-97] for char in a_str.lower() if char in "abcdefghijklmnopqrstuvwxyz"]

def words_by_letter(a_str):
    unique_words = {}

    a_str = a_str.split()

    for word in a_str:
        word = word.lower()
        if word[0] not in unique_words.keys():
            unique_words[word[0]] = {word}
        
        else:
            unique_words[word[0]].add(word)

    return unique_words

    




def main():
    # you may use this function to manually test your code if you feel the need
    # to do so.
    print(euclidean_distance([1,2],[1,5]))
    print(data_sorter([10,3000,5,20,10,3,100,3000,3120,100]))
    print(phonetic_translation("alpha"))
    print(words_by_letter("The cat in the hat is back with a bright blue bat out in " \
        "the back"))

if __name__ == "__main__":
    main()