def solution(a:list):
    count = 0
    frequency = {}
    
    for num in a:
        sorted_num = ''.join(sorted(str(num)))
        frequency[sorted_num] = frequency.get(sorted_num, 0) + 1
    
    for value in frequency.values():
        if value > 1:
            count += value * (value - 1) // 2

    return count
            
print(solution([25, 35, 872, 228, 53, 278, 872]))