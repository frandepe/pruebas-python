## Dos palabras q al ordenarlas son iguales

def is_anagrama(word_one, word_two):
    if word_one.lower() == word_two.lower():
        return False
    return sorted(word_one.lower()) == sorted(word_two.lower())

print(is_anagrama("Amor", "Roma"))