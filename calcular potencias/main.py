print("Bienvenido a la calculadora de POTENCIAS, trabajo con decimales")
x = float(input("Escribe la base: "))
y = float(input("Escribe el exponente: "))

if x == 0:
        if y == 0:
                print("¡Acabas de proponer un auténtico reto!"),
        print("La base es cero, cualquier numero por cero siempre va a ser cero, Demostración ( Sólo funciona \nen caso de que base y exponente sean desigual a 0, por eso si introduciste 0 en la base y el \nexponente saldrá 1 ya que se aplica la regla abajo impresa ): ", pow(x,y))
elif x < 0:
        print("Tu base es bajo cero", pow(x,y))
elif x > 0:
        print("El resultado es", pow(x,y))
if y == 0:
        print("Cualquier número elevado a 0 es 1")
