def build_heap(data):
    swaps = []
    for i in range(len(data) // 2, -1, -1):
        min_index = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < len(data) and data[l] < data[min_index]:
            min_index = l
        if r < len(data) and data[r] < data[min_index]:
            min_index = r
        if i != min_index:
            data[i], data[min_index] = data[min_index], data[i]
            swaps.append((i, min_index))
            j = min_index
            while j < len(data):
                l = 2 * j + 1
                r = 2 * j + 2
                if l < len(data) and data[l] < data[j]:
                    data[l], data[j] = data[j], data[l]
                    swaps.append((l, j))
                    j = l
                elif r < len(data) and data[r] < data[j]:
                    data[r], data[j] = data[j], data[r]
                    swaps.append((r, j))
                    j = r
                else:
                    break
    return swaps

def main():
    input_source = input("I or F")
    if input_source == 'F':
        file_name = input("File name: ")
        with open(file_name, 'r', encoding="utf-8") as f:
            n = int(f.readline().strip())
            data = list(map(int, f.readline().strip().split()))
    else:
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps), end=" ")
    for i, j in swaps:
        print(i, j, end=" ")

if __name__ == "__main__":
    main()