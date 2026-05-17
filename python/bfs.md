# Busca em largura — BFS

## 📚 Introdução

A busca em largura, conhecida como **BFS** (*Breadth-First Search*), é um algoritmo usado para percorrer grafos ou árvores por níveis.

Diferente da DFS, que explora um caminho até o fim antes de voltar, a BFS visita primeiro todos os vizinhos mais próximos do vértice inicial.

Ela é muito utilizada para encontrar o menor caminho em grafos não ponderados, verificar conectividade, resolver problemas de labirinto e calcular distâncias mínimas em quantidade de arestas.

Considere o seguinte grafo:

```txt
1 -- 2 -- 4
|    |
3 -- 5
```

Se começarmos a BFS pelo vértice `1`, primeiro visitamos os vizinhos de `1`, depois os vizinhos desses vizinhos.

Uma possível ordem de visita seria:

```txt
1, 2, 3, 4, 5
```

## 🤔 Como funciona

A BFS utiliza uma fila.

O algoritmo funciona assim:

1. Coloca o vértice inicial na fila
2. Marca esse vértice como visitado
3. Remove o primeiro elemento da fila
4. Adiciona seus vizinhos ainda não visitados na fila
5. Repete o processo até a fila ficar vazia

## 🤓 Implementação

```py
from collections import deque


def bfs(grafo, inicio):
    fila = deque([inicio])
    visitados = set([inicio])

    while fila:
        vertice = fila.popleft()
        print(vertice)

        for vizinho in grafo[vertice]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)


grafo = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 5],
    4: [2],
    5: [2, 3]
}

bfs(grafo, 1)
```

## 📌 BFS para menor caminho

Como a BFS percorre o grafo por níveis, ela pode calcular a distância mínima a partir de um vértice inicial em grafos sem peso.

```py
from collections import deque


def bfs_distancia(grafo, inicio):
    distancia = {inicio: 0}
    fila = deque([inicio])

    while fila:
        vertice = fila.popleft()

        for vizinho in grafo[vertice]:
            if vizinho not in distancia:
                distancia[vizinho] = distancia[vertice] + 1
                fila.append(vizinho)

    return distancia

print(bfs_distancia(grafo, 1))
# {1: 0, 2: 1, 3: 1, 4: 2, 5: 2}
```

## ⚠️ Observações

A complexidade da BFS é **O(V + E)**, onde:

- `V` é a quantidade de vértices
- `E` é a quantidade de arestas

Para implementar BFS de forma eficiente em Python, é recomendado usar `deque`, pois remover elementos do início de uma lista comum pode ser custoso.
