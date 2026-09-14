import os 
os.system("cls")

print("==Para=tener=una=contraeña=valida=debe==")
print(" tener al menos 8 caracateres")
print(" Tener al menos una letra mayuscula ")
print(" Tener al menos una letra minusculas")
print(" Tener al menos un numero ")
print(" No puede tener espacios")
print(" No puede comenzar con un numero ")

contraseña=input(" Ingrese su contraseña")

tiene_8 = len (contraseña)>=8
tiene_mayuscula= False
tiene_minuscula= False
tiene_numero = False
tiene_espacio= ""in contraseña
comienza_numero = False

for caracter  in contraseña:
    
    if caracter.isupper():
        tiene_mayuscula = True
        
    if caracter.islower():
        tiene_minuscula = True
    
    if caracter.isdigit():
        tiene_numero = True
        
if len (contraseña) >0:
    if contraseña [0].isdigit():
        comienza_numero = True
        
print("\n== RESULTADO==")

if tiene_8:
    print("✓ Tiene al menos 8 caracteres")
else:
    print("✗ Debe tener al menos 8 caracteres")

if tiene_mayuscula:
    print("✓ Tiene mayúsculas")
else:
    print("✗ Debe tener al menos una mayúscula")

if tiene_minuscula:
    print("✓ Tiene minúsculas")
else:
    print("✗ Debe tener al menos una minúscula")

if tiene_numero:
    print("✓ Tiene números")
else:
    print("✗ Debe tener al menos un número")

if tiene_espacio == False:
    print("✓ No contiene espacios")
else:
    print("✗ No puede contener espacios")

if comienza_numero == False:
    print("✓ No comienza con número")
else:
    print("✗ No puede comenzar con número")


# Resultado final
if (tiene_8 and tiene_mayuscula and tiene_minuscula
    and tiene_numero and tiene_espacio == False
    and comienza_numero == False):

    print("\nContraseña válida")
else:
    print("\nContraseña no válida")
    
        
