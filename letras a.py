#função para contar todas as letras "A" que aparecer
def contarLetra_A(frase):
    return frase.lower().count('a')


#aqui apenas digite uma frase
frase = input("Digite uma frase: ")


#aqui a função é chamadas para a frase digitada
letras_A = contarLetra_A(frase)


#enfim, é impresso a quantidade de letras "A"
print(f"A letra 'a' aparece {letras_A} vezes na frase.")