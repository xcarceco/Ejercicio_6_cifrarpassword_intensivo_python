def validarcontrasena():
    print('Has puesto:', contra)
    if len(contra) == 6:
        print('Bien!, la contraseña tiene 6 caracteres')
        bescorrecto = True
    else:
        if len(contra) > 6:
            print('Ojo!, la contraseña tiene más de 6 caracteres')
            bescorrecto = False
        else:
            if len(contra) < 6:
                print('La contraseña es menor de 6 caracteres')
                bescorrecto = False
            else:
                print('Error desconocido')
                bescorrecto = False
    return bescorrecto

contra = input("Introduce una contraseña de 6 caracteres: ")

if validarcontrasena() == True:
    password = contra.replace('a', '').replace('e', '').replace('e', '').replace('i', '').replace('o', '').replace('u','').replace('1', '2').replace('3', '4').replace('6', '7').replace('9', '0')
    password2 = password + '¡' + '1''a' + '1''a' + '1''a' + '1''a' + '1''a' + '1''a' + '1''a' + '1''a' + '1''a' + '1''a' + '1''a' + '1''a' + '1' + '1''a' + '1''a' + '1''a' + '1''a' + '1''a' + '1''a'

    if len(password2) < 32:
        print('nueva contraseña menor que 31: ', password2+password2[:32])
    elif len(password2)==32:
        print('El password es:', password2)
    elif len(password2) >32:
        print('El password es:', password2[:32])
    else:
        print('Contraseña no valida')

