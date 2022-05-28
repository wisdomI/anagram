def find_anagram(w1, w2):
    if(len(w1) == len(w2)):
        sorted_w1=sorted(w1)
        sorted_w2=sorted(w2)

        if (sorted_w1 == sorted_w2):
                print("True")
        else: print("False")

    else: 
        print("False")


w1 = "loop"
w2 = "pool"

find_anagram(w1, w2)

def find_anagram(w3, w4):
    if(len(w3) == len(w4)):
        sorted_w3=sorted(w3)
        sorted_w4=sorted(w4)

        if (sorted_w3 == sorted_w4):
                print("True")
        else: print("False")

    else: 
        print("False")


w3 = "Scoop"
w4 = "pool"

find_anagram(w3, w4)
