def find_median(nums):
    '''
    A function built to find the median of an array of random numbers. It will sort then find the median.
    If there is an even number of numbers then it will find the average between the two middle numbers;
    if it is odd then just take the middle most number... then return "mid".
    '''
    nums.sort()
    mid = nums[0]
    if len(nums) % 2 == 0:
        val = len(nums) // 2
        mid = (nums[val] + nums[val + 1]) / 2
    else:
        val = len(nums) // 2
        mid = nums[val]
    return mid

def pet(num):
    '''
    A function that generates a random pet or random animal given a certain number.
    No real function to the code besides entertainment for the user and the code developer for a finite amount of time.
    Uses a switch-case function using "if" statements since python (to my knowledge) does not have switch functions. 
    The code otherwise speaks for itself.
    '''
    if num <= 0:
        print("No pets for you. >:(")
    elif num >= 1 and num <= 10:
        print("You have now adopted " + str(num) + " dogs.")
    elif num > 10 and num <= 20:
         print("You seemed to have FOUND " + str(num) + " cats and now are roaming around your home.")
    elif num > 20 and num <= 30:
        print("You traveled to the tropics and stole " + str(num - 20) + " monkeys.")
    elif num > 30 and num <= 40:
        print("You somehow acquired a dolphin?" + "Eeee-eee-eee! Keee-kiki-kikik! Squeeee-eee-ee! Click-click-click-eeeek!")
    elif num > 40 and num <= 50:
        print("An iguana in running around, catch it before it is too late!")
        print(3)
        print(2)
        print(1)
        print("Oop. Too late; he escaped from your grasp.")
    elif num > 50 and num <= 70:
        print("You can have Pikachu.")
    elif num > 70 and num <= 98:
        print("Woah!")
        print("There goes a fat flying squirrel!!")
    elif num == 99:
        print("Here is a special Blobfish; the cutest animal to ever exist. :)")
    else:
        print("Go Chicago Blackhawks!")

print("The median is: " + str(find_median([1,3,7,9,11,16,20])))
print("The median is: " + str(find_median([130,91,42,9,-1,8])))
print("The median is: " + str(find_median([1,1,1,1,1,1,1,1,1,1,1,1,1,1,9,68,1,9,6,9,101])))

pet(13)
pet(101)
pet(-500)