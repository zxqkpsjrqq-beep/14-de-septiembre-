import os
os.system("cls")


print("===CLASIFICACION DE COMPETENCIA===")
try:
    
    velocidad = float(input("Puntaje de velocidad\n"))
    precision = float(input("puntaje de precicion\n"))
    resistencia = float(input("puntaje de resistencia\n"))
    
    
    if(velocidad < 0 or velocidad > 100 or precision < 0 or precision > 100 or resistencia < 0 or precision > 100):
        print("ERROR los puntajes deben estar en el rango de 0 a  100")
    else:
        puntaje_final = (velocidad * 0.30 + precision * 0.40 + resistencia * 0.30)
        
        print(f" Puntaje final: {puntaje_final}")
        
        if (velocidad < 40 or precision < 40 or resistencia < 40 ):
            print("CLASIFICACION: No aprobados")
        elif (puntaje_final >=90):
            print("CLASIFICACION: Excelente")
        elif (puntaje_final >= 75):
            print("CALSIFICACION: Muy bueno ")
        elif(puntaje_final >=60):
            print("CLASIFICACION: Aprobado")
        else:
            print("CLASIFICACION: No aprobado")   
            
        if(velocidad > 95 and precision > 95 and resistencia > 95):
            print("Rendimiento exepcional ")
            
except:
    print("los valores deben ser numericos ")