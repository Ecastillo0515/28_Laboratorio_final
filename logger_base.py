#La libreria logging es para warnings
import logging as log

#%(asctime)s -> Agrega tiempo (Fecha y hora) al log
#%(levelname)s --> Agrega si fue debug, info, warning, Error o critical
#%(filename)s -> Nombre del archivo que lo arrojo
#%lineno)s -> linea de codigo en la que surgio el log
#(message)s --> Muestra el mensaje que hemos agregado al log
#%I Hora
#%M Mintos
#%S Segundos
#%p si es pm o am
log.basicConfig(level=log.WARNING,
                #Format es el formato
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                #datefmt es el formato de fecha que queramos
                datefmt='%I:%M:%S %p',
                #Manejador
                handlers=[
                    #FileHanlder('File') Manda el log a un archivo, si no existe lo crea
                    log.FileHandler('capa_datos.log'),
                    #StreamHandler() Manda el mensaje a nivel consola
                    #log.StreamHandler()
                ])

if __name__ == '__main__':
    log.debug('Mensaje a nivel debug')
    log.info('Mensaje a nivel info')
    log.warning('Mensaje a nivel de warning')
    log.error('Mensaje a nivel de error')
    log.critical('Mensaje a nivel critical')