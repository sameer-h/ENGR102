"""
By submitting this document, I agree to the following:
"Aggies do not lie, cheat, or steal, nor tolerate those who do."
"I have not given or recieved any unauthorized aid on this assignment."

Names: Sameer Hussain

ENGR 102 - 214

Professor: Dr.Socolofsky
Assignment: Lab 05b
Date: 09/18/2019
shussain2@tamu.edu
Script: Labo07bChess.py
Individual Lab

Chess board moves of a game
"""
#Chess board
board = [["R", "N", "B", "Q", "K", "B", "N", "R"],
         ["P", "P", "P", "P", "P", "P", "P", "P"],
         [".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", "."],
         ["p", "p", "p", "p", "p", "p", "p", "p"],
         ["r", "n", "b", "q", "k", "b", "n", "r"]]
def showboard():
    for i in range(len(board)):
        print(board[i])
showboard()
d={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8}
while True:
    row=int(input("Enter your row number (1-8) for the piece you want to move"))
    coll=input("Enter your column number (a-h) for the piece you want to move")
    col=d[coll]
    if board[row-1][col-1]==".":
        exit("Sorry, there is not a piece there")
    else:
        row1 = int(input("Enter your row number (1-8) for where you want to move the piece"))
        coll1 = input("Enter your column number (a-h) for where you want to move the piece")
        col1=d[coll1]
        if row1>8 or col1>8 or row1<1 or col1<1:
            print("Moved your piece off the board. It has been captured.")
        else:
            board[row1-1][col1-1]=board[row-1][col-1]
        board[row-1][col-1]="."
    showboard()
