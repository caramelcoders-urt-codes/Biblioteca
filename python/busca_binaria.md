# Busca binária

## 📚 Introdução

A busca binária é um algoritmo extremamente útil de busca que utiliza a técnica de divisão e conquista, ela é utilizada para buscar um elemento em um vetor ordenado.

A busca binária é um algoritmo de complexidade O(log n), ou seja, ele é muito mais rápido que uma busca linear, que tem complexidade O(n).

Digamos que você tenha um vetor de números inteiros ordenados, e queira buscar o número 7.

```py
vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

O algoritmo da busca binária funciona da seguinte forma:

1. Verifica o elemento do meio do vetor
2. Se o elemento do meio for o que você está procurando, retorna o índice dele
3. Se o elemento do meio for maior que o que você está procurando, repita o processo na primeira metade do vetor
4. Caso o elemento do meio for menor que o que você está procurando, repita o processo na segunda metade do vetor

Vamos ver um exemplo:

```py
vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# O elemento do meio é o 5
# 5 é menor que 7, então vamos procurar na segunda metade do vetor
# [6, 7, 8, 9, 10]

# O elemento do meio é o 8
# 8 é maior que 7, então vamos procurar na primeira metade do vetor
# [6, 7]

# O elemento do meio é o 7
# 7 é o que estamos procurando, então retornamos o índice dele
```

Perceba a redução em passos necessários para encontrar um elemento em um vetor ordenado, enquanto uma busca linear precisaria de 7 passos para encontrar o número 7, a busca binária só precisou de 3 passos.

Se tivessemos um vetor com 1 milhão de elementos, a busca linear precisaria de 1 milhão de passos (no pior caso), enquanto a busca binária precisaria de apenas 20 passos (também no pior caso).

## 🤓 Implementação

```py
def busca_binaria(vetor, elemento):
    inicio = 0
    fim = len(vetor) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if vetor[meio] == elemento:
            return meio
        elif vetor[meio] > elemento:
            fim = meio - 1
        else:
            inicio = meio + 1

    return -1

vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
elemento = 2

print(busca_binaria(vetor, elemento))
# 1 (índice do elemento)
```

É importante notar que a busca binária só funciona pois o vetor está ordenado. Caso o vetor não esteja ordenado, o algoritmo não funciona.
