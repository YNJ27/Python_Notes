questions=["(I) Total number of alphabets in English are?","(II) National Animal of India is ?","(III) Current president of India is ?","(IV) Full form of FAME is ?","(V) Only Indian to win noble prize for chemistry ?"]
answers=[[26,28,25,23],["Lion","Leopard","Tiger","Bison"],["Narendra Modi","Draupadi Murmu","Amit Shah","Yogi Adityanath"],["Faster Adoption and Manufacturing of EVs","Faltu Agar Magar Easter","Fast Awesome Mindblowing EV","None of these"],["Mother Teresa","Rabindranath Tagore","C V Raman","Vekatraman Ramakrishnan"]]
correct_ans=[26,"Tiger","Draupadi Murmu","Faster Adoption and Manufacturing of EVs","Vekatraman Ramakrishnan"]

winning_amount=0
num1=0

for val in questions:
    print(val)
    list1=answers[num1]
    i=1
    for val in list1:
        print("%d) %s"%(i,val))
        i+=1
    
    option_no=int(input("Enter the correct option number: "))
    # print(list1[option_no])
    # print(correct_ans[num1])
    if list1[option_no-1]==correct_ans[num1]: #imp step
        winning_amount += 10**(num1+3)
    
    else:
        break
    print("")
    num1+=1

if winning_amount==11111000:
    print("\nBadhai ho aap Crorepati bangaye aur apne pure",winning_amount,"rupaye jite hai")
else:
    print("\nTotal amount won by you is:",winning_amount)