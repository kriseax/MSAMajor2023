"""
Write a python program that calculates Einstein's theory of relativity E = MC^2
Prompt the user to enter the mass
C = 300000000
Output: "Value of E: _____"
"""

#Get inputs
C = 300000000

#Prompt user to enter mass
mass = int(input("Enter mass: "))

#Process: Calculate E
E = mass * C**2

print(f"Value of E: {E}")
