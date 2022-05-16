def find_vowels(word):
    similar_vowels=""
    vowels="aeiouAEIOU"
    for i in word:
        similar_check=vowels.find(i) 
        check_repeating=word.count(i)
        upper_vowels=vowels.upper()
        if similar_check==-1 or check_repeating>1 or i==upper_vowels[similar_check]:
         word=word.replace(i,"",1)
        else:
            similar_vowels+=i+","
    similar_vowels=similar_vowels[:-1]
    print("Vowels : "+similar_vowels)