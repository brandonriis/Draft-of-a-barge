#201358937 Tonge_Brandon-CA01.py
#October 2018
#This program accepts the users imputs regarding the specification of a barge
#and then uses these inputs to calculate the draft of said barge. This
#calculation is made assuming the barge is constructed using iron. The
#program will then output each of the calculated values for the user.

print("This program will calculate the draft of an iron barge using the \ninputed user values.")
print()

#User inputs
length = float(input("Please enter the length of the barge in metres: "))
height = float(input("Please enter the height of the barge in metres: "))
breadth = float(input("Please enter the breadth of the barge in metres: "))

#Set the value for the weight of iron
weight_of_iron = 1.06

#Calculations for the draft
area_of_barge = (2*height)*(length+breadth)+(length*breadth)

mass_of_barge = area_of_barge*weight_of_iron

draft_of_barge = mass_of_barge/(length*breadth)

#User Outputs
print("")
print("The length is: {0:.2f}" .format(length) + "m")
print("The height is: {0:.2f}" .format(height) + "m")
print("The breadth is: {0:.2f}" .format(breadth) + "m")
print("The draft of the barge is: {0:.3f}" .format(draft_of_barge) + "m")

#Test outputs
#print("The weight of iron is: " + str(weight_of_iron) + "kg per square meter")
#print("The area of the barge is: " + str(area_of_barge) + " meters squared")
#print("The mass of the barge is: " + str(mass_of_barge) + "kg")
