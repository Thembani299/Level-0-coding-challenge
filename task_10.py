def common_letters(letter1,letter2):
    common=""
    for i in letter1:   
        letter_capital=letter2.upper()
        letter_small=letter2.lower()
        check_common_capital=letter_capital.find(i)
        check_common_small=letter_small.find(i)

        if check_common_small!=-1 or check_common_capital!=-1 and letter1.count(i)==1:
           i=i.lower()
           common+=" "+i+","
           letter2=letter2.replace(i,"")
        else:
           letter1= letter1.replace(i,"",1)

    common=common[:-1]
    print("Common letters:"+ common)

common_letters("house","computers")
