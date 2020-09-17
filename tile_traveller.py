# def R11(direction):
#     if direction == 'n' or 'N':
#         x = 1

x=1
y=1

while not ((x==3) and (y==1)):
    
    if x==1 and y==1:
        print('You can travel: (N)orth.')
        direction = input('Direction:')
        if (direction == 'N') or (direction =='n') :
            y = y+1
        else:
            print('Not a valid direction!')
            
    elif x==1 and y==2:
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
            print('Victory!')
        else:
            print('Not a valid direction!')
    

        



    
    

        
