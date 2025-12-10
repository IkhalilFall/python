def deco(func):
    def wrapper(*args, **kwargs):
        print("Avant l'exécution")
        result = func(*args, **kwargs)
        print("Après l'exécution")
        return result
    return wrapper

@deco
def say_hello(name):
    print(f"Hello {name}")

say_hello("Alice")





import time

def timer(func):
    """Décorateur qui mesure le temps d'exécution d'une fonction"""
    def wrapper(*args, **kwargs):
        start_time = time.time()          # Temps avant exécution
        result = func(*args, **kwargs)    # Appel de la fonction
        end_time = time.time()            # Temps après exécution
        elapsed_time = end_time - start_time
        print(f"La fonction '{func.__name__}' a mis {elapsed_time:.6f} secondes.")
        return result
    return wrapper

# Exemple d'utilisation
@timer
def somme_nombres(n):
    total = 0
    for i in range(n):
        total += i
    return total

result = somme_nombres(1000000)
print("Résultat :", result)


