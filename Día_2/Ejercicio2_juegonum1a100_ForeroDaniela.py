import random ##Toma de otro código 

def play_game():
    number_to_guess = random.randint(1, 100) ##Rango de los números posibles
    attempts_left = 10
    print("Adivina el número del 1 al 100. Tienes solamente 10 intentos.")

    while attempts_left > 0: ##Se repite hasta que el usuario se quede sin intentos
        user_guess = int(input("Ingresa un número: ")) ##El usuario ingresa un número 
        if user_guess < number_to_guess - 5 or user_guess > number_to_guess + 5:
            print("Tu número esta muy lejos.") ##Si el número del usuario es menor al num-5 o mayor al num+5 
        elif abs(user_guess - number_to_guess) <= 2:##Si su resta es mayor igual a 2
            print("Muy cerca")
        else:
            print("Tu número esta cerca pero no mucho.")##Si no cumple con ninguna y es muy mayor o menor 

        attempts_left -= 1
        if user_guess == number_to_guess: ##Cuando se acierta al número se felicita al usuario 
            print(f"¡Felicidades! Adivinaste el número {number_to_guess} en {11 - attempts_left} intentos")
            
    
    if attempts_left == 0 and user_guess != number_to_guess: ##Si el usuario se queda sin intentos=fin del juego 
        print(f"Fin del juego. El número correcto era: {number_to_guess}.")

play_game()
