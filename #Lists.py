#Lists
#megan rivera
#1/8/24

#Initialize
#mySchedule stores a list of the classes you are currently taking at Jones and your lunch period as strings

Class = ["AP Lang", "Bio", "AP Calc", "AP Comp Sci", "Spanish", "Civics", "ACES Dance"]
#Main

#Complete the following tasks using list/array methods. Print the result for each task.

#Task 1: Print your 1st - 7th period classes in a list in the correct order (index 0 should be your 1st period class)


print (Class)

#Task 2: Print only your 3rd period class

print (Class[2])

#Task 3: Add your lunch period in between your 3rd and 4th period using a list method
Class.insert (4, "Lunch")
print (Class)
#Final Task: Remove your least favorite class using a list method
Class.remove ("Civics")
print (Class)

