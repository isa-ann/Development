'''
You have a variable called hours which equals 24, the number of hours in a day.
Print There are 24 hours in a day. Make sure to use your variable.
First, print using commas. Remember that using commas automatically adds spaces!
Now, print using string concatenation. Remember to cast hours to a string and manually add the spaces!
'''
hours = 24
print("There are",hours,"hours in a day.")
Code works well but let's concatenate
print('There are ' + str(hours) + ' hours in a day. ')
print(f'There are {hours} hours in a day')
