# Here we wish to create a code that takes any arbitrary vector in R3 and provide the dot and cross product

import numpy as np
import matplotlib.pyplot as plt
def return_vector_list(vec1, vec2, vec3):

    vector_list = [vec1, vec2, vec3]
    check_length = []
    for i in vector_list:
        length = len(i)
        # print(length)
        check_length.append(length)
        # print(f'vector is {length} dimensions')
    print(f'vectors have length {check_length} respectively')
    return vector_list






def cross_dot(vectors):
    if vectors[0][0] == str:
        # not mathematical:
        cross = (f'({vectors[1][1]}{vectors[2][2]} - {vectors[1][2]}{vectors[2][1]}){vectors[0][0]}'
            f' + ({vectors[1][2]}{vectors[2][0]} - {vectors[1][0]}{vectors[2][2]}){vectors[0][1]}'
             f' + ({vectors[1][0]}{vectors[2][1]} - {vectors[1][1]}{vectors[2][0]}){vectors[0][2]}')
        dot = (f'{vectors[0][0]}{vectors[1][0]}{vectors[2][0]}'
            f' + {vectors[0][1]}{vectors[1][1]}{vectors[2][1]}'
            f' + {vectors[0][2]}{vectors[1][2]}{vectors[2][2]}')

    elif vectors[0][0] == int:
        # mathematical
        cross, dot = 1, 2

    else:
        print('vectors are not completely strings or integers')

        #print(f'cross product: {cross}')
        #print(f'dot product: {dot}')
    return cross, dot

"""[
v1x v1y v1z
v2x v2y v2z
v3x v3y v3z]"""



#eval(input('enter v1, v2, v3: '))
#print(v1)
#print(v2)




if __name__ == "__main__":
    # Input your components into the x1, y2, ..., z3:
    #v1, v2, v3 = ['x1', 'y1', 'z1'], ['x2', 'y2', 'z2'], ['x3', 'y3', 'z3']

    # If you have numbers comment above code and input here:
    v1, v2, v3 = [[1, 2, 3], [2, 0, 1], [2, 3, 4]]

    # Error test:
    #v1, v2, v3 = [[1, 2, a], ['s', 0, 0], [1, 1, 1]]
    cross_dot(return_vector_list(v1, v2, v3))

