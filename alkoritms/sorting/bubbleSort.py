class BubbleSort:
    @staticmethod
    def sort(arr):
        n = len(arr)
        state = ""
        copy = [x for x in arr]
        for i in range(n-1):
            for j in range (n - i - 1):
                state = "Comparing"
                yield copy, [j, j+1], state
                if(copy[j] > copy[j + 1]):
                    copy[j], copy[j+1] = copy[j+1], copy[j]
                    state = "Swapped"
                    yield copy, [j, j+1], state
        state = "Sorted"
        yield copy, [], state
