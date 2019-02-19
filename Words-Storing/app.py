# First we need to to know how much words user needs to store


how_much = int(input("Enter how many words you want to put: "))


# Then, we need an arry box to store user's words


words_array = []
i=0


while i<how_much :
    words_body= input("Enter: ")
    words_array.insert(i, words_body)
    i+=1


print(words_array)