import numpy as np
import json
import os

# Definir funciones auxiliares
def is_num():
    while True:
        try:
            x = input("Ingrese una opción: ")
            x = int(x)
            return x
        except ValueError:
            print("Error, debe ingresar un número, reintente.")

def is_medicamento():
    while True:
        try:
            x = input("Ingrese un medicamento: ")
            x = str(x)
            return x
        except ValueError:
            print("Error, debe ingresar un número, reintente.")

def is_valid_codigo():
    while True:
        try:
            x = input("Ingrese el código: ")
            x = str(x)
            return x
        except ValueError:
            print("Error, debe ingresar un número, reintente.")

def show_menu():
    print("\nATENCIÓN MÉDICA VETERINARIA")
    print("--------------------------------------------")
    print("1) Crear ficha de un paciente")
    print("2) Buscar por código de paciente")
    print("3) Eliminar por código de paciente")
    print("4) Buscar medicamentos recetados")
    print("5) Listar pacientes ingresados")
    print("6) Listar posición de los pacientes ingresados")
    print("7) Salir")
    print("--------------------------------------------")

def mostrar_posiciones_mascotas(mascotas, num_mascotas):
    print("\nPosiciones ocupadas en la lista de pacientes:")
    for i in range(num_mascotas):
        if mascotas[i, 0] != "":
            print(f"Posición {i}: {mascotas[i, 0]}")
    print("--------------------------------------------")

# Inicializar la matriz de pacientes
mascotas = np.empty([50, 8], dtype="object")
num_mascotas = 0

# Leer datos de los archivos JSON y TXT
if os.path.exists("mascotas.json"):
    with open("mascotas.json", "r") as archivo_json:
        data = json.load(archivo_json)
        for mascota in data["mascotas"]:
            encontrado = False
            for i in range(num_mascotas):
                if mascotas[i, 1] == mascota["codigo"]:
                    encontrado = True
                    break
            if not encontrado:
                mascotas[num_mascotas] = [
                    mascota["nombre"],
                    mascota["codigo"],
                    mascota["edad"],
                    mascota["peso"],
                    mascota["raza"],
                    mascota["especie"],
                    mascota["diagnostico"],
                    mascota["medicamento"]
                ]
                num_mascotas += 1

if os.path.exists("mascotas.txt"):
    with open("mascotas.txt", "r") as archivo_txt:
        for linea in archivo_txt:
            if linea.startswith("Nombre:"):
                nombre = linea.split(":")[1].strip()
                codigo = archivo_txt.readline().split(":")[1].strip()
                edad = archivo_txt.readline().split(":")[1].strip()
                peso = archivo_txt.readline().split(":")[1].strip()
                raza = archivo_txt.readline().split(":")[1].strip()
                especie = archivo_txt.readline().split(":")[1].strip()
                diagnostico = archivo_txt.readline().split(":")[1].strip()
                medicamento = archivo_txt.readline().split(":")[1].strip()
                encontrado = False
                for i in range(num_mascotas):
                    if mascotas[i, 1] == codigo:
                        encontrado = True
                        break
                if not encontrado:
                    mascotas[num_mascotas] = [
                        nombre,
                        codigo,
                        edad,
                        peso,
                        raza,
                        especie,
                        diagnostico,
                        medicamento
                    ]
                    num_mascotas += 1
                archivo_txt.readline()

# Bucle principal del programa
while True:
    show_menu()
    opcion = is_num()

    if opcion == 1:
        mascota = [
            input("Ingrese el nombre del paciente: "),
            is_valid_codigo(),
            input("Ingrese la edad del paciente: "),
            input("Ingrese el peso del paciente: "),
            input("Ingrese la raza del paciente: "),
            input("Ingrese la especie animal del paciente: "),
            input("Ingrese el diagnóstico del paciente: "),
            is_medicamento()
        ]
        # Verificar si ya existe un paciente con el mismo código
        duplicado_encontrado = False
        for i in range(num_mascotas):
            if mascotas[i, 1] == mascota[1]:
                print("Error: El código ya existe, ingrese un código diferente.")
                duplicado_encontrado = True
                break
        if not duplicado_encontrado:
            mascotas[num_mascotas] = mascota
            num_mascotas += 1
            print("Ficha del paciente ingresada correctamente.")
            print("--------------------------------------------")
            mostrar_posiciones_mascotas(mascotas, num_mascotas)

    elif opcion == 2:
        codigo_busqueda = is_valid_codigo()
        encontrado = False
        for i in range(num_mascotas):
            if mascotas[i, 1] == codigo_busqueda:
                print(f"Nombre: {mascotas[i, 0]}")
                print(f"Código: {mascotas[i, 1]}")
                print(f"Edad: {mascotas[i, 2]}")
                print(f"Peso: {mascotas[i, 3]}")
                print(f"Raza: {mascotas[i, 4]}")
                print(f"Especie: {mascotas[i, 5]}")
                print(f"Diagnóstico: {mascotas[i, 6]}")
                print(f"Medicamento: {mascotas[i, 7]}")
                print("--------------------------------------------")
                encontrado = True
                break
        if not encontrado:
            print("Error, código no encontrado.")
            print("--------------------------------------------")

    elif opcion == 3:
        codigo_busqueda = is_valid_codigo()
        encontrado = False
        for i in range(num_mascotas):
            if mascotas[i, 1] == codigo_busqueda:
                mascotas[i] = ["", "", "", "", "", "", "", ""]
                num_mascotas -= 1
                print("Ficha del paciente eliminada correctamente.")
                print("--------------------------------------------")
                mostrar_posiciones_mascotas(mascotas, num_mascotas)
                encontrado = True
                break
        if not encontrado:
            print("Error, código no encontrado.")
            print("--------------------------------------------")

    elif opcion == 4:
        codigo_busqueda = is_valid_codigo()
        encontrado = False
        for i in range(num_mascotas):
            if mascotas[i, 1] == codigo_busqueda:
                print(f"Medicamento: {mascotas[i, 7]}")
                print("--------------------------------------------")
                encontrado = True
                break
        if not encontrado:
            print("Error, código no encontrado.")
            print("--------------------------------------------")

    elif opcion == 5:
        print("Listado de pacientes ingresados:")
        for i in range(num_mascotas):
            if mascotas[i, 0] != "":
                print(f"Nombre: {mascotas[i, 0]}")
                print(f"Código: {mascotas[i, 1]}")
                print(f"Edad: {mascotas[i, 2]}")
                print(f"Peso: {mascotas[i, 3]}")
                print(f"Raza: {mascotas[i, 4]}")
                print(f"Especie: {mascotas[i, 5]}")
                print(f"Diagnóstico: {mascotas[i, 6]}")
                print(f"Medicamento: {mascotas[i, 7]}")
                print("--------------------------------------------")

    elif opcion == 6:
        mostrar_posiciones_mascotas(mascotas, num_mascotas)

    elif opcion == 7:
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida, reintente.")

# Guardar la información de los pacientes en un archivo JSON
json_data = {
    "mascotas": [
        {
            "nombre": mascotas[i, 0],
            "codigo": mascotas[i, 1],
            "edad": mascotas[i, 2],
            "peso": mascotas[i, 3],
            "raza": mascotas[i, 4],
            "especie": mascotas[i, 5],
            "diagnostico": mascotas[i, 6],
            "medicamento": mascotas[i, 7]
        }
        for i in range(num_mascotas)
    ]
}

with open("mascotas.json", "w") as archivo_json:
    json.dump(json_data, archivo_json, indent=4)

# Guardar la información de los pacientes en un archivo TXT
with open("pacientes.txt", "w") as archivo_txt:
    for i in range(num_mascotas):
        if mascotas[i, 0] != "":
            archivo_txt.write(f"Nombre: {mascotas[i, 0]}\n")
            archivo_txt.write(f"Código: {mascotas[i, 1]}\n")
            archivo_txt.write(f"Edad: {mascotas[i, 2]}\n")
            archivo_txt.write(f"Peso: {mascotas[i, 3]}\n")
            archivo_txt.write(f"Raza: {mascotas[i, 4]}\n")
            archivo_txt.write(f"Especie: {mascotas[i, 5]}\n")
            archivo_txt.write(f"Diagnóstico: {mascotas[i, 6]}\n")
            archivo_txt.write(f"Medicamento: {mascotas[i, 7]}\n")
            archivo_txt.write("----------------------------\n")