# Busca em profundidade — DFS

## 📚 Introdução

A busca em profundidade, conhecida como **DFS** (*Depth-First Search*), é um algoritmo utilizado para percorrer grafos ou árvores.

A ideia da DFS é explorar o máximo possível um caminho antes de voltar e tentar outros caminhos.

Ela é muito usada em problemas de conectividade, componentes conexos, labirintos, árvores, ciclos e ordenação topológica.

Considere o seguinte grafo:

```txt
1 -- 2 -- 4
|    |
3 -- 5
```

Representando esse grafo com lista de adjacência:

```py
grafo = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 5],
    4: [2],
    5: [2, 3]
}
```

Se começarmos a DFS pelo vértice `1`, o algoritmo pode seguir por `2`, depois `4`, voltar, ir para `5`, depois `3`, e assim por diante.

## 🤔 Como funciona

O algoritmo funciona assim:

1. Marca o vértice atual como visitado
2. Percorre seus vizinhos
3. Para cada vizinho ainda não visitado, chama a DFS novamente
4. Quando não houver mais vizinhos não visitados, retorna para o vértice anterior

## 🤓 Implementação

```py
def dfs(grafo, vertice, visitados):
    visitados.add(vertice)
    print(vertice)

    for vizinho in grafo[vertice]:
        if vizinho not in visitados:
            dfs(grafo, vizinho, visitados)


grafo = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 5],
    4: [2],
    5: [2, 3]
}

visitados = set()
dfs(grafo, 1, visitados)
```

## ⚠️ Observações

A complexidade da DFS é **O(V + E)**, onde:

- `V` é a quantidade de vértices
- `E` é a quantidade de arestas

Em Python, para grafos muito grandes, a versão recursiva pode gerar erro de limite de recursão. Nesses casos, pode ser melhor usar uma implementação iterativa com pilha.
