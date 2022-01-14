import sys

T = int(sys.stdin.readline())
# 1 : 흰색
# 2 : 빨간색
# 3 : 초록색
# 4 : 오랜지색
# 5 : 파란색
# 6 : 노란색

def rotate(color, pm):
    if pm == '+':
        cube[color][0], cube[color][1], cube[color][2],\
        cube[color][3], cube[color][4], cube[color][5],\
        cube[color][6], cube[color][7], cube[color][8] = \
        cube[color][6], cube[color][3], cube[color][0],\
        cube[color][7], cube[color][4], cube[color][1],\
        cube[color][8], cube[color][5], cube[color][2]
    else:
        cube[color][0], cube[color][1], cube[color][2],\
        cube[color][3], cube[color][4], cube[color][5],\
        cube[color][6], cube[color][7], cube[color][8] = \
        cube[color][2], cube[color][5], cube[color][8],\
        cube[color][1], cube[color][4], cube[color][7],\
        cube[color][0], cube[color][3], cube[color][6]

for i in range(T):
    n = int(sys.stdin.readline())
    a = list(sys.stdin.readline().split())
    cube = {'w': ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
            'y': ['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y'],
            'r': ['r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r'],
            'b': ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
            'o': ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
            'g': ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g']}
    for x in a:
        if x == "U+":
            cube['r'][:3], cube['g'][2::3], cube['o'][8:5:-1], cube['b'][:3] = \
                cube['b'][:3], cube['r'][:3], cube['g'][2::3], cube['o'][8:5:-1]
            rotate('w', '+')
        elif x == 'U-':
            cube['r'][:3], cube['g'][2::3], cube['o'][8:5:-1], cube['b'][:3] = \
                cube['g'][2::3], cube['o'][8:5:-1], cube['b'][:3], cube['r'][:3]
            rotate('w', '-')
        elif x == "D+":
            cube['r'][6:], cube['g'][::3], cube['o'][2::-1], cube['b'][6:] = \
                cube['g'][::3], cube['o'][2::-1], cube['b'][6:], cube['r'][6:]
            rotate('y', '+')
        elif x == "D-":
            cube['r'][6:], cube['g'][::3], cube['o'][2::-1], cube['b'][6:] = \
                cube['b'][6:], cube['r'][6:], cube['g'][::3], cube['o'][2::-1]
            rotate('y', '-')
        elif x == "L+":
            cube['w'][::3], cube['r'][::3], cube['y'][::3], cube['o'][::3] = \
                cube['o'][::3], cube['w'][::3], cube['r'][::3], cube['y'][::3]
            rotate('g', '+')
        elif x == "L-":
            cube['w'][::3], cube['r'][::3], cube['y'][::3], cube['o'][::3] = \
                cube['r'][::3], cube['y'][::3], cube['o'][::3], cube['w'][::3]
            rotate('g', '-')
        elif x == "R+":
            cube['w'][2::3], cube['r'][2::3], cube['y'][2::3], cube['o'][2::3] = \
                cube['r'][2::3], cube['y'][2::3], cube['o'][2::3], cube['w'][2::3]
            rotate('b', '+')
        elif x == "R-":
            cube['w'][2::3], cube['r'][2::3], cube['y'][2::3], cube['o'][2::3] = \
                cube['o'][2::3], cube['w'][2::3], cube['r'][2::3], cube['y'][2::3]
            rotate('b', '-')
        elif x == "F+":
            cube['w'][6:], cube['b'][::3], cube['y'][2::-1], cube['g'][6:] = \
                cube['g'][6:], cube['w'][6:], cube['b'][::3], cube['y'][2::-1]
            rotate('r', '+')
        elif x == "F-":
            cube['w'][6:], cube['b'][::3], cube['y'][2::-1], cube['g'][6:] = \
                cube['b'][::3], cube['y'][2::-1], cube['g'][6:], cube['w'][6:]
            rotate('r', '-')
        elif x == "B+":
            cube['w'][:3], cube['b'][2::3], cube['y'][8:5:-1], cube['g'][:3] = \
                cube['b'][2::3], cube['y'][8:5:-1], cube['g'][:3], cube['w'][:3]
            rotate('o', '+')
        elif x == "B-":
            cube['w'][:3], cube['b'][2::3], cube['y'][8:5:-1], cube['g'][:3] = \
                cube['g'][:3], cube['w'][:3], cube['b'][2::3], cube['y'][8:5:-1]
            rotate('o', '-')
    for x in range(0,7,3):
        print('%c%c%c'%(cube['w'][x],cube['w'][x+1],cube['w'][x+2]))






