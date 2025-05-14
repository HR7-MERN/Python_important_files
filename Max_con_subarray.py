def sub_arr(arr):
    if not arr:
        return 0, []
    sub_array = max_sum = arr[0]
    start = end = temp_start = 0
    for i in range(1, len(arr)):
        if arr[i] > (sub_array + arr[i]):  # -2 1 3 -1 4 5 2 1
            sub_array = arr[i]
            temp_start = i
        else:
            sub_array += arr[i]
        if sub_array > max_sum:
            max_sum = sub_array
            start = temp_start
            end = i
    return max_sum, arr[start:end+1]


arr = list(map(int, input("Please enter the input: ").strip().split()))
max_sum, result_str = sub_arr(arr)
final = ""
for i in result_str:
    final += str(i) + " "
print(final)
print(max_sum)
