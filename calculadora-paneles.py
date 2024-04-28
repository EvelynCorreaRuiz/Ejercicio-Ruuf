def cantidad_paneles(a, b, x, y):
    # Calcula cuántos paneles caben en la orientación vertical (a en x, b en y)
    cant_vertical = (x // a) * (y // b)
    
    # Calcula el espacio restante en el techo después de colocar los paneles verticales
    espacio_restante_y = y - (b * (y // b))
    
    # Calcula cuántos paneles adicionales caben en la orientación horizontal rotada (b en x, a en y) con el espacio restante
    cant_horizontal_rotado = (x // b) * (espacio_restante_y // a)
    
    # Retorna la suma de los paneles verticales y horizontales rotados
    return cant_vertical + cant_horizontal_rotado

if __name__ == "__main__":
    # Solicita al usuario que ingrese las dimensiones de los paneles y del techo
    a = int(input("Ingrese el ancho del panel solar (a): "))
    b = int(input("Ingrese la longitud del panel solar (b): "))
    x = int(input("Ingrese el longitud del techo (x): "))
    y = int(input("Ingrese la ancho del techo (y): "))

    # Calcula la cantidad de paneles que caben en el techo y muestra el resultado
    resultado = cantidad_paneles(a, b, x, y)
    print("La cantidad máxima de paneles que caben es:", resultado)
