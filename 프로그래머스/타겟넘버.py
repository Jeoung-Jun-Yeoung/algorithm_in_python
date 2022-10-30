numbers = [1, 1, 1, 1]

target = 2
answer = 0


sum = 0


def dfs(index, sum):
    if (index == len(numbers)):
        if(sum == target):
            answer += 1
            return
    dfs(index + 1, sum + numbers[index])
    dfs(index + 1, sum - numbers[index])
