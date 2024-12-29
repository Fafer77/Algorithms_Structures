def find_source(A):
    n = len(A)
    candidate = 0
    # Etap eliminacji kandydatów
    for i in range(1, n):
        # Jeśli kandydat nie ma krawędzi do i, to kandydat odpada, i staje się nowym kandydatem
        if A[candidate][i] == 0:
            candidate = i
    
    # Etap weryfikacji kandydata
    for j in range(n):
        if j != candidate:
            # Kandydat musi mieć krawędź do j
            if A[candidate][j] == 0:
                return None
            # Do kandydata nie może wchodzić krawędź z j
            if A[j][candidate] == 1:
                return None
    
    # Jeżeli dotarliśmy tutaj, candidate jest źródłem
    return candidate

# Przykład użycia:
if __name__ == "__main__":
    # Przykładowy digraf z 4 wierzchołkami (0,1,2,3)
    # Załóżmy, że wierzchołek 2 jest źródłem:
    #   2 -> 0, 2 -> 1, 2 -> 3, brak krawędzi do 2 z innego wierzchołka.
    A = [
        [0, 1, 0, 0],  # 0 -> 1
        [0, 0, 0, 0],  # 1 brak krawędzi wychodzących
        [1, 1, 0, 1],  # 2 -> 0, 2 -> 1, 2 -> 3
        [0, 0, 0, 0]   # 3 brak krawędzi wychodzących
    ]
    source = find_source(A)
    if source is not None:
        print("Źródło w digrafie to wierzchołek:", source)
    else:
        print("W digrafie nie ma źródła.")
