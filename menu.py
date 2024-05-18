from usuario import Usuario
from usuario_dao import UsuarioDAO
from logger_base import log

opcion = None
while opcion != 5:
    print()
    print('Opciones: ')
    print()
    print('1- Mostrar usuarios')
    print('2- Agregar usuario')
    print('3- Modificar usuario')
    print('4- Eliminar usuario')
    print('5- Salir')
    opcion = int(input('Elige una opcion (1-5): '))
    if opcion == 1:
        print()
        usuarios = UsuarioDAO.seleccionar()
        for usuario in usuarios:
            #log.info(usuario)
            print(usuario)
    elif opcion == 2:
        print()
        username_var = input('Nombre de usuario: ')
        password_var = input('Contraseña: ')
        usuario = Usuario(username=username_var,password=password_var)
        usuarios_insertados = UsuarioDAO.insertar(usuario)
        #log.info(f'Usuarios insertados: {usuarios_insertados}')
        print(f'Usuarios insertados: {usuarios_insertados}')
    elif opcion == 3:
        print()
        id_usuario_var = int(input('ID del usuario a modificar: '))
        username_var = input('Nuevo nombre de usuario: ')
        password_var = input('Nueva contraseña: ')
        usuario = Usuario(id_usuario_var, username_var, password_var)
        usuarios_actualizados = UsuarioDAO.actualizar(usuario)
        #log.info(f'Usuarios actualizados: {usuarios_actualizados}')
        print(f'Usuarios actualizados: {usuarios_actualizados}')
    elif opcion == 4:
        print()
        id_usuario_var = int(input('ID del usuario a eliminar: '))
        usuario = Usuario(id_usuario=id_usuario_var)
        usuarios_eliminados = UsuarioDAO.eliminar(usuario)
        #log.info(f'Usuarios eliminados: {usuarios_eliminados}')
        print(f'Usuarios eliminados: {usuarios_eliminados}')
    else:
        print()
        print('Saliendo de la aplicacion')
        #log.info('Saliendo de la aplicacion')