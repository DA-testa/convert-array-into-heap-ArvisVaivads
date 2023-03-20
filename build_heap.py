# python3

def build_heap(data):
    swaps = []

    def sift_down(i):
        min_index = i
        left_child = 2 * i + 1
        if left_child < len(data) and data[left_child] < data[min_index]:
            min_index = left_child
        right_child = 2 * i + 2
        if right_child < len(data) and data[right_child] < data[min_index]:
            min_index = right_child
        if i != min_index:
            data[i], data[min_index] = data[min_index], data[i]
            swaps.append((i, min_index))
            sift_down(min_index)

    for i in range(len(data) // 2, -1, -1):
        sift_down(i)

    return swaps

def main():

    input_type = input("I or F")

    if input_type.upper() == 'I':
        n = int(input())
        data = list(map(int, input().split()))
    elif input_type.upper() == 'F':
        file_name = input("File name: ")
        with open("tests/" + file_name, 'r', encoding="utf-8") as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))
    else:
        print("Invalid input type")
        return

    assert len(data) == n
    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()