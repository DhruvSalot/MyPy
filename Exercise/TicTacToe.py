theBoard = {"tl" : " ", "tm" : " ", "tr" : " ",
            "ml" : " ", "mm" : " ", "mr" : " ",
            "bl" : " ", "bm" : " ", "br" : " "}

def printBoard(theBoard):
    print (theBoard["tl"] + "|" + theBoard["tm"] + "|" + theBoard["tr"])
    print ("-+-+-")
    print (theBoard["ml"] + "|" + theBoard["mm"] + "|" + theBoard["mr"])
    print ("-+-+-")
    print (theBoard["bl"] + "|" + theBoard["bm"] + "|" + theBoard["br"])

turn = "X"
for i in range (9):
        print ()
        printBoard(theBoard)
        print ()
        print (" It's " + turn + "'s turn.")
        print (" Select the area you want to make your " + turn + "'s move.")

        move            = input("> ")
        theBoard[move]  = turn
        if turn        == "X"    :
            turn = "O"
        else                     :
            turn = "X"


printBoard(theBoard)
