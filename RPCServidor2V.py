from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import os
from os import remove
#import cgi
import shutil

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Creamos a funcionalidad de Servidor
with SimpleXMLRPCServer(('localhost', 8000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    def crear_Archivo(name):
        file = open(name, "w")
        file.close()
        return True
    server.register_function(crear_Archivo, 'Crear')

    def renombrar_Archivo(viejo, nuevo):
        os.rename(viejo, nuevo)
        return True
    server.register_function(renombrar_Archivo, 'ReName')

    def Borrar_Archivo(name):
        os.remove(name)
        return True
    server.register_function(Borrar_Archivo, 'KillFile')

    def Leer_Archivo(name):
        archivo = open(name, "r+")
        salida = archivo.read()
        archivo.close()
        return salida
    server.register_function(Leer_Archivo, 'Leer')

    def Escribir_Archivo(name, text):
        archivo = open(name, "a")
        archivo.write('\n' + text)
        archivo.close()
        return True
    server.register_function(Escribir_Archivo, 'Escribir')
    def Crea_Directorio(name):
        try:
            os.mkdir(name)
        except OSError:
            return False
        else:
            return True
    server.register_function(Crea_Directorio, 'NuevoDir')

    def Eliminar_Directorio(dir):
        try:
            os.rmdir(dir)
        except OSError:
            shutil.rmtree(dir)
            return True
        else:
            return True
    server.register_function(Eliminar_Directorio, 'DelDir')

    def Lista_Directorios():
        return os.listdir(".")
    server.register_function(Lista_Directorios, 'ListDir')


   #Inicio del Servidor
    server.serve_forever()