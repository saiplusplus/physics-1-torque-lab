import random

class physicsTorqueLab:
    
    def tableGenerator(radiusStart, radiusEnd, massStart, massEnd):
        fixed_mass = 300 # Change to your fixed mass
        fixed_radius = 25 # Change to your fixed radius
        trial_number = 6 # Change to your desired number of trials
        print("Radius\t Mass\t")
        for i in range(trial_number):
            radius = random.randint(radiusStart, radiusEnd)
            expectedMass = (radius * fixed_mass)/fixed_radius
            print(str(radius) + "\t" + str(expectedMass))

    tableGenerator(15, 30, 200, 300) # Change your numbers accordingly