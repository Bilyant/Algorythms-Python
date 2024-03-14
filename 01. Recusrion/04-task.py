def generate_vectors(idx, vector):

    if idx >= len(vector):
        print(*vector, sep='')
        return

    for n in range(2):
        vector[idx] = n
        generate_vectors(idx + 1, vector)


num = 3
vector = [None] * num
generate_vectors(0, vector)

