"""
Busca Binária - Algoritmo eficiente para buscar em arrays ordenados
Complexidade de Tempo: O(log n)
Complexidade de Espaço: O(1)

Uso em Competição: Essencial para problemas que envolvem busca em dados ordenados
"""


def busca_binaria(arr, alvo):
    """
    Realiza busca binária em um array ordenado.
    
    Args:
        arr: Lista ordenada de elementos
        alvo: Elemento a ser procurado
        
    Returns:
        Índice do elemento se encontrado, -1 caso contrário
    """
    esquerda = 0
    direita = len(arr) - 1
    
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        
        if arr[meio] == alvo:
            return meio
        elif arr[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    
    return -1


def busca_binaria_recursiva(arr, alvo, esquerda=0, direita=None):
    """
    Versão recursiva da busca binária.
    
    Args:
        arr: Lista ordenada de elementos
        alvo: Elemento a ser procurado
        esquerda: Índice esquerdo (padrão: 0)
        direita: Índice direito (padrão: len(arr) - 1)
        
    Returns:
        Índice do elemento se encontrado, -1 caso contrário
    """
    if direita is None:
        direita = len(arr) - 1
    
    if esquerda > direita:
        return -1
    
    meio = (esquerda + direita) // 2
    
    if arr[meio] == alvo:
        return meio
    elif arr[meio] < alvo:
        return busca_binaria_recursiva(arr, alvo, meio + 1, direita)
    else:
        return busca_binaria_recursiva(arr, alvo, esquerda, meio - 1)


# Exemplos de Uso
if __name__ == "__main__":
    # Array ordenado para teste
    numeros = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    
    print("Array:", numeros)
    print()
    
    # Teste iterativo
    print("--- BUSCA BINÁRIA ITERATIVA ---")
    print(f"Buscando 7: índice {busca_binaria(numeros, 7)}")  # Output: 3
    print(f"Buscando 1: índice {busca_binaria(numeros, 1)}")  # Output: 0
    print(f"Buscando 19: índice {busca_binaria(numeros, 19)}")  # Output: 9
    print(f"Buscando 10: índice {busca_binaria(numeros, 10)}")  # Output: -1
    print()
    
    # Teste recursivo
    print("--- BUSCA BINÁRIA RECURSIVA ---")
    print(f"Buscando 7: índice {busca_binaria_recursiva(numeros, 7)}")  # Output: 3
    print(f"Buscando 1: índice {busca_binaria_recursiva(numeros, 1)}")  # Output: 0
    print(f"Buscando 20: índice {busca_binaria_recursiva(numeros, 20)}")  # Output: -1
