#!/usr/bin/env python3

import sys
import math
import MiscFunctions as misc
import Car as Car

# add a CLOSED set for duplicates/ or for states that we've already achieved

CarNotIn = 'Car not in the Board'

class Board:
    width, height = 6, 6
    boardArr = [[0 for i in range(width)] for j in range(height)]

    def __init__(self):
        self.width, self.height = 6, 6
        defaultString = "  o aa|  o   |xxo   |ppp  q|     q|     q" #default construction as directed
        rows = defaultString.split('|')
        for i in range(len(rows)):
            row = rows[i]
            rowElements = list(row)
            self.boardArr[i] = rowElements


    def createBoard(self, inp): #inp will be the string from the cammand line argument
        rows = inp.split('|')
        for i in range(len(rows)):
            row = rows[i]
            rowElements = list(row)
            self.boardArr[i] = rowElements

    def printBoard(self):
        print '  - - - - - -  '
        for i in range(len(self.boardArr)):
            row = self.boardArr[i]
            print '|',
            for element in row:
                print element,
            if i == 2: # exit position in the board
                print ' '
            else:
                print '|'
        print '  - - - - - -  '

    def isDone(self): # here I'm just ahrd coding the [2,5] position to be the winning one
        if self.boardArr[2][5] == 'x' and self.boardArr[2][4] == 'x': # assuming the car is just two characters long
            return True
        else:
            return False

    def clone(self, board): # cloning data from "board" to self)
        self.width = board.width
        self.height = board.height
        self.boardArr = []
        for row in board.boardArr:
            a  = []
            for e in row:
                a.append(e)
            self.boardArr.append(a)


    def isCarInBoard(self, carCh):
        distinctElem = []
        for row in self.boardArr:
            for element in row:
                if element not in distinctElem:
                    distinctElem.append(element)
        distinctElem.remove(' ')
        if carCh not in distinctElem:
            return False
        else:
            return True

    def replaceCarPos(self, carInit, carFin): # to be only used in moveCar()
        #print 'Car INIT'
        #carInit.printDetails()
        #print 'Car FIN'
        #carFin.printDetails()
        initPos = misc.findAll(self.boardArr, carInit.carChar)
        finPos = carFin.allCoordinates
        for i in initPos:
            self.boardArr[i[0]][i[1]] = ' '
        for j in finPos:
            self.boardArr[j[0]][j[1]] = carFin.carChar

    def moveCar(self, carCh, direction, units):
        #' and i >=0 print carCh, direction, units
        if self.isCarInBoard(carCh) == False:
            print 'MoveCar(): ',CarNotIn
            return
        car = Car.Car(self.boardArr, carCh)
        boardClone = Board()
        boardClone.clone(self)
        # direction can only be 'up', 'down', 'left' and 'right'
        try:
            if direction == 'up' and car.orientation == 'vertical':
                for i in range(car.end1[0]-units, car.end1[0]): # checking for path hindrances # from 0 to the start of the car
                    if self.boardArr[i][car.end1[1]] != ' ' or i < 0 or i > 5:
                        #print 'moveCar(): cannot move car - path hindrance'
                        return
                newCar = Car.Car(self.boardArr, carCh)
                newCoordinates = []
                for i in range(car.end1[0] - units, car.end2[0] - units + 1):
                    newCoordinates.append([i, car.end1[1]])
                newCar.modifyCar(carCh, newCoordinates)
                self.replaceCarPos(car, newCar)
            elif direction == 'down' and car.orientation == 'vertical':
                for i in range(car.end2[0] + 1, car.end2[0] + units + 1):
                    if self.boardArr[i][car.end1[1]] != ' ' or i < 0 or i > 5:
                        #print 'moveCar(): cannot move car - path hindrance'
                        return
                newCar = Car.Car(self.boardArr, carCh)
                newCoordinates = []
                for i in range(car.end1[0] + units, car.end2[0] + units + 1):
                    newCoordinates.append([i, car.end1[1]])
                newCar.modifyCar(carCh, newCoordinates)
                self.replaceCarPos(car, newCar)
            elif direction == 'left' and car.orientation == 'horizontal':
                for i in range(car.end1[1]-units, car.end1[1]):
                    if self.boardArr[car.end1[0]][i] != ' ' or i < 0 or i > 5:
                        #print 'moveCar(): cannot move car - path hindrance'
                        return
                newCar = Car.Car(self.boardArr, carCh)
                newCoordinates = []
                for i in range(car.end1[1] - units, car.end2[1] - units + 1):
                    newCoordinates.append([car.end1[0], i])
                newCar.modifyCar(carCh, newCoordinates)
                self.replaceCarPos(car, newCar)
            elif direction == 'right' and car.orientation == 'horizontal':
                for i in range(car.end2[1] + 1, car.end2[1] + units + 1):
                    if self.boardArr[car.end2[0]][i] != ' ' or i < 0 or i > 5:
                        #print 'moveCar(): cannot move car - path hindrance'
                        return
                newCar = Car.Car(self.boardArr, carCh)
                newCoordinates = []
                for i in range(car.end1[1] + units, car.end2[1] + units + 1):
                    newCoordinates.append([car.end1[0], i])
                newCar.modifyCar(carCh, newCoordinates)
                self.replaceCarPos(car, newCar)
            #else:
                #print 'cme',
                #print 'car is horizontal/vertical and you\'re tring to move it vertically/horizontally.'
            #self.printBoard()
            return self.boardArr
        except IndexError:
            pass
            #print 'eh.. IndexError'

    def next_for_car(self, carCh): # can take arguments as character
        CLOSED = [] # list to store the states that have already been achieved
        if misc.isCarInBoard(self.boardArr, carCh) == False:
            print 'next_for_car(): ', CarNotIn
        car = Car.Car(self.boardArr, carCh)
        cloneBoard = Board()
        #car.printDetails()
        if car.orientation == 'horizontal':
            directions = ['left', 'right']
            for direction in directions:
                for i in range(1,5):
                    cloneBoard.clone(self)
                    newBoardArr = cloneBoard.moveCar(carCh, direction, i)
                    #cloneBoard.printBoard()
                    if newBoardArr not in CLOSED and newBoardArr is not None:
                        #print newBoardArr
                        #CLOSED.append(cloneBoard)
                        CLOSED.append(newBoardArr)
        elif car.orientation == 'vertical':
            directions = ['down', 'up']
            for direction in directions:
                for i in range(1,5):
                    cloneBoard.clone(self)
                    newBoardArr = cloneBoard.moveCar(carCh, direction, i)
                    #cloneBoard.printBoard()
                    if newBoardArr not in CLOSED and newBoardArr is not None:
                        #print newBoardArr
                        #CLOSED.append(cloneBoard)
                        CLOSED.append(newBoardArr)
        #CLOSED.remove(None)
        #print CLOSED
        #misc.printCLOSED(CLOSED)
        for board in CLOSED:
            #print board
            #board.printBoard()
            misc.printBoardArr(board)
            #for row in board:
                #print row
            #print
        return CLOSED

    def next(self): # call next_for_car() for all the cars
        CLOSED = []
        #CLOSED.append('kms')
        #print 'CLOSED HERE: ', CLOSED
        distinctElements = []
        for row in self.boardArr:
            for element in row:
                if element not in distinctElements:
                    distinctElements.append(element)
        distinctElements.remove(' ')
        for carCh in distinctElements:
            CLOSED.append(self.next_for_car(carCh))
            #print 'in Loop: ',CLOSED
        #CLOSED.remove(None)
        #for board in CLOSED:
            #misc.printBoardArr(board)
        #CLOSED.remove([])
        #misc.printCLOSED(CLOSED)


