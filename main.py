if __name__ == '__main__':
    arr = map(int, input().split())
    arr_list = list(arr)
    arr_list.sort(reverse=True)
    print(arr_list[1])
    