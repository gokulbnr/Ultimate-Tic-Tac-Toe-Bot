import simulator
b=simulator.Board()
c = [['x','x','x','o'],['-','-','-','-'],['-','-','-','-'],['-','-','-','-']]
for i in range(4):
    for j in range(4):
        b.board_status[i][j]=c[i][j]
b.print_board()

def partial(i,j,board):
    player='o'
    opponant='x'
    addfac=5
    URet = 0
    for IT in range(4):
        flag=0
        utility=0
        for it in range(4):
            if(board.board_status[i*4+it][j*4+IT]!=player  and flag==1):
                print "1",IT," ",it
                flag=0
            elif(board.board_status[i*4+it][j*4+IT]==player  and flag==0):
                flag=1
            elif(board.board_status[i*4+it][j*4+IT]==player and flag==1):
                print "add1 ",it
                utility+=addfac*2
        URet+=utility
        flag=0
        utility=0
        for it in range(4):
            if(board.board_status[i*4+IT][j*4+it]!=player  and flag==1):
                print "2",IT," ",it
                flag=0
            elif(board.board_status[i*4+IT][j*4+it]==player  and flag==0):
                flag=1
            elif(board.board_status[i*4+IT][j*4+it]==player and flag==1):
                print "add2 ",it
                utility+=addfac*2
        URet+=utility
        flag=0
        utility=0
        for it in range(4):
            if(board.board_status[i*4+it][j*4+IT]!=opponant  and flag==1):
                flag=0
                print "3",IT," ",it
                print "streak broken"
                if(board.board_status[i*4+it][j*4+IT]==player):
                    print "4",IT," ",it
                    print "streak broken by opponant"
                    utility*=-1/4
            elif(board.board_status[i*4+it][j*4+IT]==opponant  and flag==0):
                flag=1
            elif(board.board_status[i*4+it][j*4+IT]==opponant and flag==1):
                print "add3 ",it
                utility-=addfac
        URet+=utility
        flag=0
        utility=0
        for it in range(4):
            if(board.board_status[i*4+IT][j*4+it]!=opponant  and flag==1):
                flag=0
                print "streak broken"
                if(board.board_status[i*4+IT][j*4+it]==player):
                    print "streak broken by opponant ",utility
                    utility*=-1.0/4
                    print utility
            elif(board.board_status[i*4+IT][j*4+it]==opponant  and flag==0):
                flag=1
            elif(board.board_status[i*4+IT][j*4+it]==opponant and flag==1):
                print "add4 ",it
                utility-=addfac
        URet+=utility

    flag=0
    utility=0
    for it in range(4):
        if(board.board_status[i*4+it][j*4+it]!=player  and flag==1):
            print "5"," ",it
            flag=0
        elif(board.board_status[i*4+it][j*4+it]==player  and flag==0):
            flag=1
        elif(board.board_status[i*4+it][j*4+it]==player and flag==1):
            print "add5 ",it
            utility+=addfac*2
    URet+=utility
    flag=0
    utility=0
    for it in range(4):
        if(board.board_status[i*4+it][j*4+it]!=opponant  and flag==1):
            flag=0
            print "6"," ",it
            if(board.board_status[i*4+it][j*4+it]==player):
                print "7"," ",it
                utility*=-1/4
        elif(board.board_status[i*4+it][j*4+it]==opponant  and flag==0):
            flag=1
        elif(board.board_status[i*4+it][j*4+it]==opponant and flag==1):
            print "add6"," ",it
            utility-=addfac
    URet+=utility
    flag=0
    utility=0
    for it in range(4):
        if(board.board_status[i*4+it][j*4+3-it]!=player  and flag==1):
            print "8"," ",it
            flag=0
        elif(board.board_status[i*4+it][j*4+3-it]==player  and flag==0):
            flag=1
        elif(board.board_status[i*4+it][j*4+3-it]==player and flag==1):
            utility+=addfac*2
            print "add7 ",it
    URet+=utility
    flag=0
    utility=0
    for it in range(4):
        if(board.board_status[i*4+it][j*4+3-it]!=opponant  and flag==1):
            flag=0
            print "9"," ",it
            if(board.board_status[i*4+it][j*4+3-it]==player):
                print "10"," ",it
                utility*=-1/4
        elif(board.board_status[i*4+it][j*4+3-it]==opponant  and flag==0):
            flag=1
        elif(board.board_status[i*4+it][j*4+3-it]==opponant and flag==1):
            print "add8 ",it
            utility-=addfac
    URet+=utility
    return URet
print partial(0,0,b)
