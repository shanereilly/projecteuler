#!/usr/bin/env python3

nums = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}

summation = 0
for i in range(1,1000):
    if i in nums:
        summation += len(nums[i])
    else:
        tempstr = ""
        num = i
        if num // 100 > 0:
            tempstr += nums[num//100] + "hundred"
            num = num % 100
            if num > 0:
                tempstr += "and"
        if num in nums:
            tempstr += nums[num]
        else:
            tempstr += nums[(num//10) * 10] + nums[num % 10]
            nums[i] = tempstr
        summation += len(tempstr)
summation += len("onethousand")
print(summation)
