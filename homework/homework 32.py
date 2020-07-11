def binary_search(ds, low, high, key):
    print('ds:',ds)
    print('low:', low)
    print('high:', high)

    mid = (high + low) // 2
    if low > high:
        return None
    elif key == ds[mid]:
        return mid
    elif key < ds[mid]:
        return binary_search(ds, low, mid - 1, key)
    else:
        return binary_search(ds, mid + 1, high, key)

li = [1, 2, 3, 4, 5]
print(binary_search(li, 0, len(li) - 1, 3))
