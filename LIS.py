def LISlen(numbers: list) -> int:
    '''
    LENGTH of longest increasing subsequence in O(n^2)
    https://youtu.be/fV-TF4OvZpk
    '''
    if(len(numbers) == 1):
        return 1

    lislength = [1 for i in range(len(numbers))]

    # задает каждому элементу длину возрастающей последовательности оканчивающейся на нём
    # O(n^2) т.к. цикл в цикле
    for i in range(1, len(numbers)):
        for j in range(0, i):
            # >= для неубывающей последовательности; > для возрастающей последовательности и тд. (убыв; невозраст.)
            if(numbers[i] > numbers[j]):
                if(lislength[i] <= lislength[j]):
                    lislength[i] = lislength[j] + 1

    maximum = max(lislength)
    return maximum


# метод ввода
def getsequence():
    a = []
    while(True):
        c = input()
        if(c == ''):
            break
        a.append(int(c))
    if(len(a) == 0):
        print("too few numbers")
        exit(0)
    return a


# ввод: число, enter, число enter .....  число, enter, enter
if __name__ == "__main__":
    lislength = LISlen(getsequence())
    print("Length of LIS:", lislength)
