print("\tAnalizador de texto \n")
texto= input("Por favvor ingresa el texto a anlizar: ")
palabras= []
texto= texto.lower()
palabras.append(input("Ingresa la primera letra: ".lower()))
palabras.append(input("Ingresa la segunda letra: ".lower()))
palabras.append(input("Ingresa la tercera letra: ".lower()))

print("\nCANTIDAD DE LETRAS")
cantidad_de_letras1=texto.count(palabras[0])
cantidad_de_letras2=texto.count(palabras[1])
cantidad_de_letras3=texto.count(palabras[2])
print(f"Logramos encontrar dentro del texto la letra {palabras[0]} repetida {cantidad_de_letras1} veces")
print(f"Logramos encontrar dentro del texto la letra {palabras[1]} repetida {cantidad_de_letras2} veces")
print(f"Logramos encontrar dentro del texto la letra {palabras[2]} repetida {cantidad_de_letras3} veces \n")

print("CANTIDAD DE PALABRAS")
texto= texto.split()
print(f"Hemos encontrado {len(texto)} palabras dentro del texto \n")

print("PALABRA DE INICIO Y FIN")
letras_inicio= texto[0]
letras_fin= texto[-1]
print(f"La palabra de inicio del texto es: {letras_inicio}")
print(f"La palabra final del texto es: {letras_fin}")

print("\nTEXTO INVERTIDO")
texto.reverse()
texto_invertido= " ".join(texto)
print(f"El texto invertido es: {texto_invertido}")

print("\nBUSCAR PALABRA")
buscar_palabra= "debes" in texto
dic = {True:"si",False:"no"}
print(f"La palabra debes {dic[buscar_palabra]} se encuentra dentro del texto")
