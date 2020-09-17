# Notandi er staddur í hálfgerðu völundarhúsi, forritið segir honum hvaða átt hann má fara
# og notandi velur þá hvaða átt hann fer. Ef notandi slær inn átt sem er ''lokuð'' lætur forritið
# notandann vita að sú leið er ekki í boði og lætur hann aftur vita hvaða áttir eru í boði
# þegar notandi er kominn á endareit hefur notandi ''unnnið''
# Hver reitur í völundarhúsinu er táknaður í forritinu sem x og y hnit
# Með því að stimpla inn leyfilega átt, þá annaðhvort stækkar eða minnkar x og y 



x=1
y=1

while not ((x==3) and (y==1)): # forritið heldur áfram á meðan x er ekki 3 og y er ekki 1 þar sem það er endareiturinn
    
    if x==1 and y==1: # notandi byrjar í reit (1,1)
        print('You can travel: (N)orth.') # þessi átt er í boði á fyrsta reit
        direction = input('Direction:') #notandi slær inn átt sem hann vill fara
        if (direction == 'N') or (direction =='n') : # ef notandi slær inn rétta átt fer hann á næsta viðeigandi reit
            y = y+1 # þannig að y hækkar um 1 og þar af leiðandi kominn á annann reit
        else:
            print('Not a valid direction!') # ef notandi stimplaði inn eitthvað annað kemur þessi melding upp
            
    elif x==1 and y==2: #endurtekur sig fyrir hvern reit
        print('You can travel: (N)orth or (E)ast or (S)outh.')
        direction = input('Direction:')
        if (direction == 'N') or (direction == 'n'):
            y = y + 1
        elif (direction == 'E') or (direction == 'e'):
            x = x + 1
        elif (direction == 'S') or (direction == 's'):
            y = y - 1
        else:
            print('Not a valid direction!')
            

    elif x==1 and y==3:
        print('You can travel: (E)ast or (S)outh.')
        direction = input('Direction:')
        if (direction == 'E') or (direction == 'e'):
            x = x + 1
        elif (direction == 'S') or (direction == 's'):
            y = y - 1
        else:
            print('Not a valid direction!')
            
    elif x==2 and y==3:
        print('You can travel: (E)ast or (W)est.')
        direction = input('Direction:')
        if (direction == 'E') or (direction == 'e'):
            x = x + 1
        elif (direction == 'W') or (direction == 'w'):
            x = x - 1
        else:
            print('Not a valid direction!')
            
    elif x==2 and y==2:
        print('You can travel: (S)outh or (W)est.')
        direction = input('Direction:')
        if (direction == 'S') or (direction == 's'):
            y = y - 1
        elif (direction == 'w') or (direction == 'W'):
            x = x - 1
        else:
            print('Not a valid direction!')
            
    elif x==2 and y==1:
        print('You can travel: (N)orth.')
        direction = input('Direction:')
        if (direction == 'N') or (direction == 'n'):
            y = y+1
        else:
            print('Not a valid direction!')
            
    elif x==3 and y==3:
        print('You can travel: (S)outh or (W)est.')
        direction = input('Direction:')
        if (direction == 'S') or (direction == 's'):
            y = y - 1
        elif (direction == 'W') or (direction == 'w'):
            x = x - 1
        else:
            print('Not a valid direction!')
        
    elif x==3 and y==2:
        print('You can travel: (N)orth and (S)outh.')
        direction = input('Direction:')
        if (direction == 'N') or (direction == 'n'):
            y = y+1
        elif (direction == 'S') or (direction == 's'):
            y = y - 1
            print('Victory!') # hér er notandi kominn á reit (3,1) sem er endareitur
        else:
            print('Not a valid direction!')
    

        



    
    

        
