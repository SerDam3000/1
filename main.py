import random
while True:

    meme_dict = {
                "КРИНЖ": "Что-то очень странное или стыдное",
                "ЛОЛ" : 'шутка',
                'ЩИЩ' : 'одобрение или восторг',
                'КРИПОВЫЙ'  :'страшный, пугающий',
                'АГРИТЬСЯ' : 'злиться',
                }
    
    m_d = ["КРИНЖ","ЛОЛ","ЛОЛ",'ЩИЩ','КРИПОВЫЙ','АГРИТЬСЯ']
    print('1 - uznat kakoeto slovo')
    print('2 - viktorina')
    que = input('1 or 2: ')
    if que == '1':
    
    
        word = input("Введите непонятное слово (КРИНЖ , ЛОЛ , ЩИЩ , КРИПОВЫЙ , АГРИТЬСЯ): ")
        if word in meme_dict.keys():
            print(meme_dict[word])
            ('__________________')
            
        else:
            print ('takovo slovo net')
            ('__________________')
    
    elif que == '2':
        print("sto obaznatsiaet slovo: ")
        print('__________________')
         
        print(random.choice(m_d))
        print('__________________')
        
        print ("1 - Что-то очень странное или стыдное")
        
    
        print ("2 - шутка")
        
    
        print ("3 - одобрение или восторг")
        
    
        print ("4 - страшный, пугающий")
        
    
        print ("5 - злиться")
        quest = input('=?=: ')
        
        
        if random.choice(m_d) == 'КРИНЖ':
            quest == '1'
            print('pravilno')
            print('__________________')
        
        elif random.choice(m_d) == 'ЛОЛ':
            quest == '2'
            print('pravilno')
            ('__________________')
        
        elif random.choice(m_d) == 'ЩИЩ':
            quest == '3'
            print('pravilno')
            ('__________________')
        
        elif random.choice(m_d) == 'КРИПОВЫЙ':
            quest == '4'
            print('pravilno')
            ('__________________')
        
        elif random.choice(m_d) == 'АГРИТЬСЯ':
            quest == '5'
            print('pravilno')
            ('__________________')
        else:
            print('ne pravilno')
            print('__________________')
