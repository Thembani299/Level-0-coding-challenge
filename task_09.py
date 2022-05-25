def find_vowels(word):
    word=word.upper()
    similar_vowels=""
    lower_vowels="aeiou"
    upper_vowels="AEIOU"

    for i in word:
        check_repeating=word.count(i)
        if check_repeating>1:
            word=word.replace(i,"",1)
        similar_check_upper=upper_vowels.find(i)
        if similar_check_upper !=-1:
            i=lower_vowels[similar_check_upper]
        similar_check_lower=lower_vowels.find(i)
        if similar_check_lower!=-1 and check_repeating==1:
            similar_vowels+=" "+i+","
            
    similar_vowels=similar_vowels[:-1]
    print("Vowels:"+ similar_vowels)

find_vowels("Umuzi")
