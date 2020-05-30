import xmlrpc.client
import datetime
s = xmlrpc.client.ServerProxy('http://localhost:8000')

def ingresaDatos(opc):
    if(opc == 1):
        print("Nombre para el nuevo Archivo: ")
        x = input()
        x = x + ".txt"
        return x
    else:
        if(opc == 2):
            print("Nombre de archivo a editar: ")
            x = input()
            x = x + ".txt"
            return x
        else:
            if(opc == 3):
                print("Archivo a renombrar: ")
                x = input()
                x = x + ".txt"
                print("Nuevo nombre: ")
                y = input()
                y = y + ".txt"
                return x, y
            else:
                if(opc == 4):
                    print("Archivo a elimiar: ")
                    x = input()
                    x = x + ".txt"
                    return x
                else:
                    if(opc == 5):
                        print("Nuevo directorio: ")
                        x = input()
                        return x
                    else:
                        if(opc == 6):
                            print("Directorio a Borrar: ")
                            x = input()
                            return x

def Lectura_Escritura(nombre):
    edit = -1
    print("Nota: Para dejar de introducir texto escribe \"exit\" para salir, y ver el archivo")
    while edit != 0:
        text = "exit"
        while edit != 0:
            if text == "exit":
                print("Archivo:", nombre + ".")
                print(s.Leer(nombre) + "\n")
                print("0-salir\n1-Escribir")
                edit = int(input())
            if(edit == 1):
                print("Texto: ")
                text = input()
                if(text != "exit"):
                    resp = s.Escribir(nombre, text)
                if(resp == True):
                    print("**********************************")

def opciones(opc):
    if opc == 1:
        x = ingresaDatos(opc)
        resp = s.Crear(x)
        if(resp == True):
            print("\nArchivo", x ,"Creado.\n")
        else:
            print("\nError.\n")
    else:
        if opc == 2:
            x = ingresaDatos(opc)
            Lectura_Escritura(x)
        else:
            if opc == 3:
                x, y = ingresaDatos(opc)
                resp = s.ReName(x, y)
                if(resp == True):
                    print("\nArchivo Renombrado.\n")
                else:
                    print("\nError al Renombrar.\n")
            else:
                if opc == 4:
                    x = ingresaDatos(opc)
                    resp = s.KillFile(x)
                    if(resp == True):
                        print("\nArchivo", x , "Eliminado.\n")
                else:
                    if(opc == 5):
                        x = ingresaDatos(opc)
                        resp = s.NuevoDir(x)
                        if(resp == True):
                            print("\nDirectorio creado.\n")
                        else:
                            print("\nError al crear el directorio.\n")
                    else:
                        if(opc == 6):
                            x = ingresaDatos(opc)
                            resp = s.DelDir(x)
                            if(resp == True):
                                print("\nDirectorio Eliminado.\n")
                            else:
                                print("\nError al eliminar el Directorio.\n")
                        else:
                            if(opc == 7):
                                print("Revisando directorios...\n")
                                lista = s.ListDir()
                                for t in lista:
                                    print("*- ", t)
                                print("\n")


def Calc_menu():
    ciclo = -1
    while ciclo != 0:
        print("1-Crear Archivo\n2-Leer y Escribir en Archivo\n3-Renombrar Archivo\n4-Borrar Archivo"
              "\n5-Crear Directorio\n6-Borrar Directorio\n7-Lista del Directorio\n0-Salir")
        ciclo = int(input())
        if ciclo != 0:
            opciones(ciclo)

Calc_menu()
print("¡Adios!")