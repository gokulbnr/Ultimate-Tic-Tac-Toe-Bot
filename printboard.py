def print_board(b):
    # for printing the state of the board
    print '==============Board State=============='
    for i in range(16):
        if i%4 == 0:
            print
        for j in range(16):
            if j%4 == 0:
                print "",
            print b[i][j],
        print
    print

    # print '==============Block State=============='
    # for i in range(4):
    #     for j in range(4):
    #         print self.block_status[i][j],
    #     print
    # print '======================================='
    print
    print
