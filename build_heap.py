# Python3

def parent(i):

    return (i - 1) // 2

def left_child(i):
   
    return 2 * i + 1

def right_child(i):

    return 2 * i + 2


def sift_down(data, i, swaps):
   
    min_index = i
    l = left_child(i)

    if l < len(data) and data[l] < data[min_index]:
        min_index = l
    r = right_child(i)

    if r < len(data) and data[r] < data[min_index]:
        min_index = r

    if i != min_index:
        data[i], data[min_index] = data[min_index], data[i]
        swaps.append((i, min_index))
        sift_down(data, min_index, swaps)

def build_heap(data):
    swaps = []
    for i in range(len(data) // 2, -1, -1):
        sift_down(data, i, swaps)
    return swaps

def main():

    input_source = input("I or F")
    if input_source == 'F':
        file_name = input("File name: ")
        with open( "tests/" + file_name, 'r', encoding="utf-8") as f:
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
