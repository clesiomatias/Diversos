import turtle as tu

tu2 = tu.Turtle()

# _Settings_____
height = 720
width = 1280
speed = 0
thickness = 4
squareThickness = 6

# _Math_____


lines = height / 6 * 4
distance = height / 8

# ____________________
tu.setup(width, height)
tu.pensize(thickness)
tu.speed(speed)

# __Basic Coordinates___
x = 0 + distance
y = height / 2 - distance

# _Coordinates_____
Coord = {
    'GamefieldX': x,
    'GamefieldY': y,
    'x1': x,
    'y1': y,
    'x2': x + (lines / 3),
    'y2': y,
    'x3': x + (lines / 3) * 2,
    'y3': y,
    'x4': x,
    'y4': y - (lines / 3),
    'x5': x + (lines / 3),
    'y5': y - (lines / 3),
    'x6': x + (lines / 3) * 2,
    'y6': y - (lines / 3),
    'x7': x,
    'y7': y - (lines / 3) * 2,
    'x8': x + (lines / 3),
    'y8': y - (lines / 3) * 2,
    'x9': x + (lines / 3) * 2,
    'y9': y - (lines / 3) * 2,
}

# _Field_Status
Field = {
    'Field1': 0,
    'Field2': 0,
    'Field3': 0,
    'Field4': 0,
    'Field5': 0,
    'Field6': 0,
    'Field7': 0,
    'Field8': 0,
    'Field9': 0,
}


# _Gamefield gets build up
def gamefield(x, y):
    global lines
    boxwidth = lines / 3
    d = 1
    i = 0
    while (i < 2):
        tu.penup()
        tu.goto(x, y - boxwidth * d)
        tu.seth(0)
        tu.pendown()
        tu.fd(lines)
        d = d + 1
        i = i + 1
    i = 0
    d = 1
    while (i < 2):
        tu.penup()
        tu.goto(x + boxwidth * d, y)
        tu.seth(270)
        tu.pendown()
        tu.fd(lines)
        d = d + 1
        i = i + 1


def cross(x, y):
    tu.penup()
    tu.goto(x + (((lines / 3) / 6) * 1), y - (((lines / 3) / 6) * 1))
    tu.seth(315)
    tu.pendown()
    tu.fd((((lines / 3) / 6) * 5.5))

    tu.penup()
    tu.goto(x + (((lines / 3) / 6) * 1), y - lines / 3 + (((lines / 3) / 6) * 1))
    tu.seth(45)
    tu.pendown()
    tu.fd((((lines / 3) / 6) * 5.5))


def circle(x, y):
    tu.penup()
    tu.goto(x + ((lines / 3) / 2), y - lines / 3 + lines / 3 / 6 * 1)
    tu.pendown()
    tu.seth(0)
    tu.circle(lines / 3 / 6 * 2)


# _checks if a field is reserved
def fieldReserved(x):
    frei = 0
    if Field['Field' + str(x)] == 0:
        return frei
    elif Field['Field' + str(x)] == 1:
        frei = 1
        return frei
    elif Field['Field' + str(x)] == 2:
        frei = 2
        return frei


# _checks wich number was pressed
def Field1():
    global fieldNumber
    fieldNumber = 1


def Field2():
    global fieldNumber
    fieldNumber = 2


def Field3():
    global fieldNumber
    fieldNumber = 3


def Field4():
    global fieldNumber
    fieldNumber = 4


def Field5():
    global fieldNumber
    fieldNumber = 5


def Field6():
    global fieldNumber
    fieldNumber = 6


def Field7():
    global fieldNumber
    fieldNumber = 7


def Field8():
    global fieldNumber
    fieldNumber = 8


def Field9():
    global fieldNumber
    fieldNumber = 9


def click():
    global player

    while (1):
        try:
            global field
            field = int(tu.textinput("Player " + str(player) + " Choose your Field", "On wich field you want to set?"))
            break
        except ValueError:
            tu2.clear()
            tu2.penup()
            tu2.goto(-lines, 0)
            tu2.pendown()
            tu2.write("only integer allowed! again...")

    if field == 1:
        Field1()
    if field == 2:
        Field2()
    if field == 3:
        Field3()
    if field == 4:
        Field4()
    if field == 5:
        Field5()
    if field == 6:
        Field6()
    if field == 7:
        Field7()
    if field == 8:
        Field8()
    if field == 9:
        Field9()


def gewinner():
    # horizontal player 1
    if Field['Field1'] == 1 and Field['Field2'] == 1 and Field['Field3'] == 1:
        return 1
    if Field['Field4'] == 1 and Field['Field5'] == 1 and Field['Field6'] == 1:
        return 1
    if Field['Field7'] == 1 and Field['Field8'] == 1 and Field['Field9'] == 1:
        return 1

    # vertikal player 1
    if Field['Field1'] == 1 and Field['Field4'] == 1 and Field['Field7'] == 1:
        return 1
    if Field['Field2'] == 1 and Field['Field5'] == 1 and Field['Field8'] == 1:
        return 1
    if Field['Field3'] == 1 and Field['Field6'] == 1 and Field['Field9'] == 1:
        return 1

    # slope player 1
    if Field['Field1'] == 1 and Field['Field5'] == 1 and Field['Field9'] == 1:
        return 1
    if Field['Field7'] == 1 and Field['Field5'] == 1 and Field['Field3'] == 1:
        return 1

    # ================================PLAYER 2==================================
    # horizontal player 2
    if Field['Field1'] == 2 and Field['Field2'] == 2 and Field['Field3'] == 2:
        return 2
    if Field['Field4'] == 2 and Field['Field5'] == 2 and Field['Field6'] == 2:
        return 2
    if Field['Field7'] == 2 and Field['Field8'] == 2 and Field['Field9'] == 2:
        return 2

    # vertikal player 2
    if Field['Field1'] == 2 and Field['Field4'] == 2 and Field['Field7'] == 2:
        return 2
    if Field['Field2'] == 2 and Field['Field5'] == 2 and Field['Field8'] == 2:
        return 2
    if Field['Field3'] == 2 and Field['Field6'] == 2 and Field['Field9'] == 2:
        return 2
    # slope player 2
    if Field['Field1'] == 2 and Field['Field5'] == 2 and Field['Field9'] == 2:
        return 2
    if Field['Field7'] == 2 and Field['Field5'] == 2 and Field['Field3'] == 2:
        return 2
    # ===========================Nobody won================================
    if Field['Field1'] != 0 and Field['Field2'] != 0 and Field['Field3'] != 0 and Field['Field4'] != 0 and Field[
        'Field5'] != 0 and Field['Field6'] != 0 and Field['Field7'] != 0 and Field['Field8'] != 0 and Field[
        'Field9'] != 0:
        return 3


def spielen():
    while (1):
        global player
        player = 1
        winner = 0
        while (1):
            while (1):
                print("Player " + str(player) + " it's your turn")
                while (1):
                    global field
                    click()
                    if field == 1 or field == 2 or field == 3 or field == 4 or field == 5 or field == 6 or field == 7 or field == 8 or field == 9:
                        break
                    else:
                        print("The Number has to be between 1 and 9")
                        tu2.clear()
                        tu2.penup()
                        tu2.goto(-lines, 0)
                        tu2.pendown()
                        tu2.write("The Number has to be between 1 and 9")
                belegt = fieldReserved(fieldNumber)
                if belegt == 0:
                    break
                else:
                    tu2.clear()
                    tu2.penup()
                    tu2.goto(-lines, 0)
                    tu2.pendown()
                    tu2.write("This field is reserved")
            if player == 1:
                cross(Coord['x' + str(fieldNumber)], Coord['y' + str(fieldNumber)])
            else:
                circle(Coord['x' + str(fieldNumber)], Coord['y' + str(fieldNumber)])
            Field['Field' + str(fieldNumber)] = player

            if player == 1:
                player = 2
            else:
                player = 1

            winner = gewinner()

            if winner == 1:
                tu2.clear()
                tu2.penup()
                tu2.goto(-lines, 0)
                tu2.pendown()
                tu2.write("Player 1 won")
                break
            if winner == 2:
                tu2.clear()
                tu2.penup()
                tu2.goto(-lines, 0)
                tu2.pendown()
                tu2.write("Player 2 won")
                break
            if winner == 3:
                tu2.clear()
                tu2.penup()
                tu2.goto(-lines, 0)
                tu2.pendown()
                tu2.write("nobody won")
                break

        break


# __mittelLinie____
tu.penup()
tu.goto(0, +height / 2)
tu.seth(270)
tu.pendown()
tu.fd(height)

gamefield(Coord['GamefieldX'], Coord['GamefieldY'])

spielen()

tu.exitonclick()
