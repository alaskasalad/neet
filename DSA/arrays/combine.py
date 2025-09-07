# time: O(n)
# space: O(1)

def combine(num1, num2):
    i = j = 0
    array = [0]

    while i < len(num1) and j < len(num2):
        if num1[i] < num2[j]:
            array.append(num1[i])
            i += 1
        else:
            array.append(num2[j])
            j += 1

    while i < len(num1):
        array.append(num1[i])

    while j < len(num2):
        array.append(num2[j])

    return array