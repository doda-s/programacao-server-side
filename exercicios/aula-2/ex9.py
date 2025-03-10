if __name__ == "__main__":
    nums = []
    nums.append(int(input("Digite um número\n>> ")))
    nums.append(int(input("Digite um número\n>> ")))
    nums.append(int(input("Digite um número\n>> ")))
    nums.append(0)
    
    if nums[0] < nums[1]:
        nums[3] = nums[0]
        nums[0] = nums[1]
        nums[1] = nums[3]
    
    if nums[0] < nums[2]:
        nums[3] = nums[0]
        nums[0] = nums[2]
        nums[2] = nums[3]
    
    if nums[1] < nums[2]:
        nums[3] = nums[1]
        nums[1] = nums[2]
        nums[2] = nums[3]
    
    nums.pop()
    print(nums)