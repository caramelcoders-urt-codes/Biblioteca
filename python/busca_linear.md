# Busca linear

## 📚 Introdução

A busca linear é um algoritmo simples de busca que percorre todos os elementos de um vetor até encontrar o valor desejado.

Ela funciona em qualquer vetor, mesmo que ele não esteja ordenado. Porém, por verificar elemento por elemento, sua complexidade é **O(n)**, onde `n` é a quantidade de elementos do vetor.

Digamos que você tenha o seguinte vetor e queira encontrar o número `8`:

```py
vetor = [5, 2, 9, 1, 8, 3]
```

O algoritmo percorre o vetor da esquerda para a direita:

1. Verifica o `5`: não é o valor procurado
2. Verifica o `2`: não é o valor procurado
3. Verifica o `9`: não é o valor procurado
4. Verifica o `1`: não é o valor procurado
5. Verifica o `8`: encontrou o elemento

Nesse caso, o algoritmo precisou de 5 verificações para encontrar o valor.

## 🤓 Implementação

```py
def busca_linear(vetor, elemento):
    for i in range(len(vetor)):
        if vetor[i] == elemento:
            return i

    return -1

vetor = [5, 2, 9, 1, 8, 3]
elemento = 8

print(busca_linear(vetor, elemento))
# 4 (índice do elemento)
```

## ⚠️ Observações

A busca linear é fácil de implementar e funciona em vetores ordenados ou não ordenados.

Apesar disso, para vetores grandes e ordenados, a busca binária costuma ser muito mais eficiente, pois possui complexidade **O(log n)**.
