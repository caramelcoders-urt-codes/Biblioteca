# BFS

## 📚 Introdução

**busca em largura**.

Ela é um algoritmo usado para percorrer grafos e árvores por níveis. Primeiro visitamos os vértices mais próximos do início, depois os mais distantes.

A BFS utiliza uma **fila** para controlar a ordem de visita.

A complexidade da BFS é **O(V + E)**, onde:

```text
V = número de vértices
E = número de arestas
```

## 🤔 Como funciona

Imagine o seguinte grafo:

```text
0 -- 1 -- 3
|    |
2 -- 4
```

Se começarmos a BFS pelo vértice `0`, o algoritmo pode visitar os vértices na seguinte ordem:

```text
0, 1, 2, 3, 4
```

O funcionamento básico é:

1. Coloca o vértice inicial na fila
2. Marca esse vértice como visitado
3. Remove o primeiro elemento da fila
4. Adiciona seus vizinhos ainda não visitados na fila
5. Repete até a fila ficar vazia

## 🤓 Implementação

```java
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class Main {
    static List<Integer>[] grafo;
    static boolean[] visitado;

    public static void bfs(int inicio) {
        Queue<Integer> fila = new LinkedList<>();

        visitado[inicio] = true;
        fila.add(inicio);

        while (!fila.isEmpty()) {
            int vertice = fila.poll();
            System.out.print(vertice + " ");

            for (int vizinho : grafo[vertice]) {
                if (!visitado[vizinho]) {
                    visitado[vizinho] = true;
                    fila.add(vizinho);
                }
            }
        }
    }

    public static void main(String[] args) {
        int n = 5;

        grafo = new ArrayList[n];
        visitado = new boolean[n];

        for (int i = 0; i < n; i++) {
            grafo[i] = new ArrayList<>();
        }

        grafo[0].add(1);
        grafo[1].add(0);

        grafo[0].add(2);
        grafo[2].add(0);

        grafo[1].add(3);
        grafo[3].add(1);

        grafo[1].add(4);
        grafo[4].add(1);

        grafo[2].add(4);
        grafo[4].add(2);

        bfs(0);
        // Saída: 0 1 2 3 4
    }
}
```

## ⚠️ Observações

A BFS é muito útil para encontrar o menor caminho em grafos **não ponderados**, ou seja, grafos em que todas as arestas têm o mesmo custo.

Ela também é bastante usada em problemas com matrizes, labirintos e mapas.
