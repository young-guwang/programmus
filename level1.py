# def solution(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
# print(solution(5))

# result = sub(3,2)    
# print(result) 

# def add(a, b):
#     c = a + b
#     return c
# add(3,4)
# print(add)
# result = add(3,4)
# print("OK")



def solution(n):
    answer = ''
    for a in range(1, n+1):
        if a % 2 == 0:
            answer = answer + "박"
        else:
            answer = answer + "수"
    return answer
solution(3)