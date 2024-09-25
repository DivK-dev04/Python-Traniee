#Replace negative numbers with zero
#Given a list of numbers nums = [-3, -1, 0, 1, 5, -7],write a list comprehension that replaces negative numbers with 0 and leaves non-negative numbers unchanged.

nums = [-3, -1, 0, 1, 5, -7]
new5 = [0 if x < 0 else x for x in nums]                              #[0 ....... else x .....] having issue with 0 and else x 
print(new5)
