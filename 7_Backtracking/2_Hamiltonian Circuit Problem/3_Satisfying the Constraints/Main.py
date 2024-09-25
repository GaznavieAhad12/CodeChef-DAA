def check(v, next_v, circuit, mat):
    # Check if 'next_v' vertex can be added after vertex 'v'
    if not mat[v][next_v] or next_v in circuit:
        return False
    return True

def backtrack(v, n, circuit, ans, mat):
    if len(circuit) == n:  # Circuit is completed
        if mat[circuit[0]][v]:  # Check if cycle is completed, starting should be adjacent to ending
            circuit.append(circuit[0])
            ans.append(list(circuit))
            circuit.pop()
        return

    for i in range(1, n + 1):
        # Calling the check function
        if not check(v, i, circuit, mat):
            continue

        # If not visited and is adjacent, add it to our candidate solution
        circuit.append(i)
        backtrack(i, n, circuit, ans, mat)
        circuit.pop()

# Number of vertices and adjacency matrix
def hamiltonian_circuit(n, mat):
    circuit = []  # Initially empty circuit
    ans = []  # To store all the circuits

    for i in range(1, n + 1):  # Fix the starting vertex
        circuit.append(i)  # Add i to circuit
        backtrack(i, n, circuit, ans, mat)
        circuit.pop()  # Remove i from circuit

    return ans

if __name__ == "__main__":
    n, m = map(int, input().split())

    # Adjacency matrix
    mat = [[False] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        mat[a][b] = True
        mat[b][a] = True

    cycles = hamiltonian_circuit(n, mat)
    cycles.sort(key=lambda x: str(x))

    for cycle in cycles:
        print(" ".join(map(str, cycle)))
