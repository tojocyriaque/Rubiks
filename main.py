import py5
from piece import *


pieces = []
count = 27

def setup():
    global pieces, cam
    py5.size(600, 600, py5.P3D)
    for x in [-1,0,1]:
        for y in [-1, 0, 1]:
            for z in [-1,0,1]:
                pieces.append(Piece(numpy.array([
                    [1, 0, 0, x],
                    [0, 1, 0, y],
                    [0, 0, 1, z],
                    [0, 0, 0, 1]
                ])))

                if x == -1 and y == -1 and z == 1:
                    pieces[-1].light = True

                elif x == 1 and y == 1 and z == 1:
                    pieces[-1].light = True

def show_faces(p):
    for face in p.faces:
        py5.push_matrix()
        py5.rect_mode(py5.CENTER)

        py5.translate(face.nrml[0]*0.5, face.nrml[1]*0.5, face.nrml[2]*0.5)
        
        if face.nrml[0] != 0:
            py5.rotate_y(py5.HALF_PI)
        if face.nrml[1] != 0:
            py5.rotate_x(py5.HALF_PI)


        py5.fill(face.col[0], face.col[1], face.col[2])
        py5.square(0,0,1)

        py5.pop_matrix()

def show_piece(p):
    m = p.mat

    py5.push_matrix()
    py5.apply_matrix(m)

    py5.no_fill()

    py5.stroke_weight(0.05)
    py5.box(1)

    show_faces(p)

    py5.pop_matrix()

def move_ud(key):
    global pieces
    index = [-1, 1][key in "dD"]
    angle = (-1,1)[key.islower()] * py5.PI/2
    for p in pieces:
        if p.y == index:
            p.turn_u(angle)
            for i in range(6):
                p.faces[i].turn_ud(angle)

def move_rl(key):
    global pieces
    index = [1, -1][key in "lL"]
    angle = (-1,1)[key.islower()] * py5.PI/2
    for p in pieces:
        if p.x == index:
            p.turn_r(angle)
            for i in range(6):
                p.faces[i].turn_lr(angle)

def move_fb(key):
    global pieces
    index = [-1, 1][key in "fF"]
    angle = (-1, 1)[key.islower()] * py5.PI/2
    for p in pieces:
        if p.z == index:
            p.turn_f(angle)
            for i in range(6):
                p.faces[i].turn_fb(angle)

def key_pressed():
    global pieces

    if py5.key in "uUdD":
        move_ud(py5.key)

    elif py5.key in "rRlL":
        move_rl(py5.key)

    elif py5.key in "fFbB":
        move_fb(py5.key)

def draw():
    global pieces
    py5.background(10,10,50)
    py5.translate(py5.width/2, py5.height/2)
    
    py5.rotate_x(-py5.mouse_y * 0.01)
    py5.rotate_y(-py5.mouse_x * 0.01)

    py5.scale(60)
    for p in pieces:
        show_piece(p)

py5.run_sketch()

