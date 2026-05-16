"""
Estruturas de Dados Básicas - Exemplos essenciais para competição
Complexidade: Varia de O(1) a O(n)

Uso em Competição: Manipulação eficiente de dados é fundamental
"""


def inverter_lista(arr):
    """
    Inverte uma lista in-place.
    
    Complexidade: O(n)
    Espaço: O(1)
    
    Args:
        arr: Lista a ser invertida
        
    Returns:
        Lista invertida
    """
    esquerda = 0
    direita = len(arr) - 1
    
    while esquerda < direita:
        arr[esquerda], arr[direita] = arr[direita], arr[esquerda]
        esquerda += 1
        direita -= 1
    
    return arr


def encontrar_min_max(arr):
    """
    Encontra o mínimo e máximo de uma lista em uma única passagem.
    
    Complexidade: O(n)
    Espaço: O(1)
    
    Args:
        arr: Lista de números
        
    Returns:
        Tupla (mínimo, máximo)
    """
    if not arr:
        return None, None
    
    minimo = maximo = arr[0]
    
    for num in arr[1:]:
        if num < minimo:
            minimo = num
        if num > maximo:
            maximo = num
    
    return minimo, maximo


def contar_frequencias(arr):
    """
    Conta a frequência de cada elemento em uma lista.
    
    Complexidade: O(n)
    Espaço: O(k) onde k é o número de elementos únicos
    
    Args:
        arr: Lista de elementos
        
    Returns:
        Dicionário com frequências
    """
    frequencias = {}
    
    for elemento in arr:
        frequencias[elemento] = frequencias.get(elemento, 0) + 1
    
    return frequencias


def elemento_mais_frequente(arr):
    """
    Encontra o elemento mais frequente em uma lista.
    
    Complexidade: O(n)
    Espaço: O(k)
    
    Args:
        arr: Lista de elementos
        
    Returns:
        Elemento mais frequente e sua frequência
    """
    if not arr:
        return None, 0
    
    frequencias = contar_frequencias(arr)
    elemento_max = max(frequencias, key=frequencias.get)
    
    return elemento_max, frequencias[elemento_max]


def remover_duplicatas(arr):
    """
    Remove duplicatas mantendo a ordem original.
    
    Complexidade: O(n)
    Espaço: O(k)
    
    Args:
        arr: Lista que pode conter duplicatas
        
    Returns:
        Lista sem duplicatas
    """
    visto = set()
    resultado = []
    
    for elemento in arr:
        if elemento not in visto:
            visto.add(elemento)
            resultado.append(elemento)
    
    return resultado


# Exemplos de Uso
if __name__ == "__main__":
    print("=" * 60)
    print("ESTRUTURAS DE DADOS BÁSICAS - EXEMPLOS")
    print("=" * 60)
    
    # Exemplo 1: Inverter Lista
    print("\n--- 1. INVERTER LISTA ---")
    lista = [1, 2, 3, 4, 5]
    print(f"Original: {lista}")
    invertida = inverter_lista(lista.copy())
    print(f"Invertida: {invertida}")
    
    # Exemplo 2: Min e Max
    print("\n--- 2. ENCONTRAR MÍNIMO E MÁXIMO ---")
    numeros = [42, 17, 89, 5, 63, 28]
    minimo, maximo = encontrar_min_max(numeros)
    print(f"Array: {numeros}")
    print(f"Mínimo: {minimo}, Máximo: {maximo}")
    
    # Exemplo 3: Contar Frequências
    print("\n--- 3. CONTAR FREQUÊNCIAS ---")
    dados = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    freq = contar_frequencias(dados)
    print(f"Array: {dados}")
    print(f"Frequências: {freq}")
    
    # Exemplo 4: Elemento Mais Frequente
    print("\n--- 4. ELEMENTO MAIS FREQUENTE ---")
    elemento, frequencia = elemento_mais_frequente(dados)
    print(f"Array: {dados}")
    print(f"Elemento mais frequente: {elemento} (aparece {frequencia}x)")
    
    # Exemplo 5: Remover Duplicatas
    print("\n--- 5. REMOVER DUPLICATAS ---")
    com_duplicatas = [1, 2, 2, 3, 1, 4, 3, 5]
    sem_duplicatas = remover_duplicatas(com_duplicatas)
    print(f"Com duplicatas: {com_duplicatas}")
    print(f"Sem duplicatas: {sem_duplicatas}")
    
    print("\n" + "=" * 60)
