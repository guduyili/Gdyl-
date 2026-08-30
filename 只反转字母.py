from typing import List


def reverse_string(s) ->str:
    char = list(s)
    tmp_s = [c for c in char if c.isalpha()]
    # tmp_s.reverse()
    tmp_s = tmp_s[::-1]


    idx = 0
    for i in range(len(char)):
        if char[i].isalpha():
            char[i] = tmp_s[idx]

            idx += 1


    return ''.join(char)


def reverse_only_letters_two_ptr(s: str) -> str:
    arr = list(s)
    left, right = 0, len(arr)-1
    while left < right:
        # 左指针找字母
        while left < right and not arr[left].isalpha():
            left += 1
        # 右指针找字母
        while left < right and not arr[right].isalpha():
            right -= 1
        # 交换
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return "".join(arr)



if __name__ == "__main__":
    s = "hello"
    print(reverse_string(s))  # Output: "olleh"
    print(reverse_string("a1b-cd!E"))   # E1d-cb!a
    print(reverse_string("Ab-cd"))      # dc-bA
    print(reverse_string("123!@中文xY")) # 123!@中文Yx    
    print(reverse_only_letters_two_ptr("123!@中文xY")) # 123!@中文Yx    