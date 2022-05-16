def common_letters(letter1,letter2):
    common_letters=""
    for i in letter1:
        check_common=letter2.find(i) 
        
        if check_common!=-1 and letter1.count(i)==1:
           common_letters+=i+","
        else:
           letter1= letter1.replace(i,"",1)

    common_letters=common_letters[:-1]
    print("common letters : " + common_letters)
