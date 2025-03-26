#Inveritr la cadena
def invertir_cadena(cadena):
    if len(cadena) == 0:  
        return cadena
    return cadena[-1] + invertir_cadena(cadena[:-1])  


texto = "Hola Mundo"
resultado = invertir_cadena(texto)
print(resultado) 
