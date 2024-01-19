from itertools import permutations

# Lista de colores posibles en el cubo de Rubik
colores = ['A', 'B', 'C', 'D', 'E', 'F']

# Generar todas las configuraciones posibles del cubo de Rubik
def generar_configuraciones():
    for color1 in colores:
        for color2 in colores:
            if color1 != color2:
                cubo = {
                    'cara_arriba': color1,
                    'cara_abajo': color2,
                    'cara_izquierda': color1,
                    'cara_derecha': color2,
                    'cara_frente': color1,
                    'cara_trasera': color2
                }
                yield cubo

# Realizar permutaciones de rotaciones en un cubo de Rubik
def permutar_rotaciones(cubo):
    permutaciones_rotaciones = list(permutations(colores))
    rotaciones = []
    for permutacion in permutaciones_rotaciones:
        nueva_cara_arriba = cubo['cara_arriba']
        nueva_cara_abajo = cubo['cara_abajo']
        nueva_cara_izquierda = cubo['cara_izquierda']
        nueva_cara_derecha = cubo['cara_derecha']
        nueva_cara_frente = cubo['cara_frente']
        nueva_cara_trasera = cubo['cara_trasera']

        nueva_cara_arriba = permutacion[colores.index(nueva_cara_arriba)]
        nueva_cara_abajo = permutacion[colores.index(nueva_cara_abajo)]
        nueva_cara_izquierda = permutacion[colores.index(nueva_cara_izquierda)]
        nueva_cara_derecha = permutacion[colores.index(nueva_cara_derecha)]
        nueva_cara_frente = permutacion[colores.index(nueva_cara_frente)]
        nueva_cara_trasera = permutacion[colores.index(nueva_cara_trasera)]

        nueva_cubo = {
            'cara_arriba': nueva_cara_arriba,
            'cara_abajo': nueva_cara_abajo,
            'cara_izquierda': nueva_cara_izquierda,
            'cara_derecha': nueva_cara_derecha,
            'cara_frente': nueva_cara_frente,
            'cara_trasera': nueva_cara_trasera
        }
        rotaciones.append(nueva_cubo)
    return rotaciones

# Probar el programa
def probar():
    for configuracion in generar_configuraciones():
        print('Configuración inicial:')
        print(configuracion)

        rotaciones = permutar_rotaciones(configuracion)
        print('Rotaciones posibles:')
        for rotación in rotaciones:
            print(rotación)
        print('\n')

probar()