def merge_descending(list1, list2):
    # Sort lists in descending order first
    list1 = sorted(list1, reverse=True)
    list2 = sorted(list2, reverse=True)

    i, j = 0, 0
    merged = []

    # Merge both lists while keeping descending order
    while i < len(list1) and j < len(list2):
        if list1[i] >= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    # Add remaining elements
    while i < len(list1):
        merged.append(list1[i])
        i += 1

    while j < len(list2):
        merged.append(list2[j])
        j += 1

    return merged


# ---- Driver Code ----
list_1 = [2, 8, 6]
list_2 = [1, 3.5, 4]

result = merge_descending(list_1, list_2)
print(result)

output:
[8, 6, 4, 3.5, 2, 1]



