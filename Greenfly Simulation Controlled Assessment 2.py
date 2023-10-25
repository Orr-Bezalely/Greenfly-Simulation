import random, time, os.path

#this function gets an inputfrom the user, which is then validated to check whether it is an integer within the given range
def inputValidInt(message = "Please enter a number between 1 and 2: ", min = 1, max = 2, noMax = False): #There are default values for the def arguments. These are message - which is the prompt displayed to the user, min - the minimum number which will be accepted in the validation routine, max - the maximum number which will be accepted in the validation routine, and noMax - which if set to True, removes the upper bound check
    while True: #repeat inner block forever
        num_choice = input(message)
        try: #checks for errors within the blocks
            num_choice = int(num_choice) #raise an exception if num_choice doesn’t contain an integer
            if num_choice >= min and (noMax == True or num_choice <= max): #check the number is within the bounds and ignore upper bound if noMax is set to True
                return num_choice #if num_choice is within the given bounds then end def by returning the valid choice
        except:
            continue #if an exception was raised when checking the number was an integer, return to the beginning of the while loop
        print("You have entered a number out of range.") #if this place is reached,then the number was a valid integer, but it wasn’t in the bounds, so give an appropriate message

#this function gets an inputfrom the user, which is then validated to check whether it is a float within the given range
def inputValidFloat(message = "Please enter a number between 0 and 1: ", min = 0, max = 1, noMax = False): #There are default values for the def arguments. These are message - which is the prompt displayed to the user, min - the minimum number which will be accepted in the validation routine, max - the maximum number which will be accepted in the validation routine, and noMax - which if set to True, removes the upper bound check
    while True: #repeat inner block forever
        num_choice = input(message)
        try: #checks for errors within the blocks
            num_choice = float(num_choice) #raise an exception if num_choice doesn’t contain a float
            if num_choice >= min and (noMax == True or num_choice <= max): #check the number is within the bounds and ignore upper bound if noMax is set to True
                return num_choice #if num_choice is within the given bound then end def by returning the valid choice
        except:
            continue #if an exception was raised when checking the number was a float, return to the beginning of the while loop
        print("You have entered a number out of range.") #if this place is reached,then the number was a valid float, but it wasn’t in the bounds, so give an appropriate message

#this function gets the initial conditions from the user
def getInitialConditions():
    generation0 = [] #this list will be used to store the various initial conditions that the user will enter 
    initial_number_of_juveniles = inputValidInt("Please enter the initial number of juveniles: ", min = 0, noMax = True) #a validation def is used to validate the user’s input
    generation0.append(initial_number_of_juveniles) #append that value to the list of generation0
    initial_number_of_adults = inputValidInt("Please enter the initial number of adults: ", min = 0, noMax = True) #a validation def is used to validate the user’s input
    generation0.append(initial_number_of_adults) #append that value to the list of generation0
    initial_number_of_seniles = inputValidInt("Please enter the initial number of seniles: ", min = 0, noMax = True) #a validation def is used to validate the user’s input
    generation0.append(initial_number_of_seniles) #append that value to the list of generation0
    juveniles_survival_rate = inputValidFloat("Please enter a number for the survival rate of juveniles: ", min = 0, max = 1) #a validation def is used to validate the user’s input
    generation0.append(juveniles_survival_rate) #append that value to the list of generation0
    adults_survival_rate = inputValidFloat("Please enter a number for the survival rate of adults: ", min = 0, max = 1) #a validation def is used to validate the user’s input
    generation0.append(adults_survival_rate) #append that value to the list of generation0
    seniles_survival_rate = inputValidFloat("Please enter a number for the survival rate of seniles: ", min = 0, max = 1) #a validation def is used to validate the user’s input
    generation0.append(seniles_survival_rate) #append that value to the list of generation0
    birth_rate = inputValidFloat("Please enter a number for the birth rate: ", min = 0, noMax = True) #a validation def is used to validate the user’s input
    generation0.append(birth_rate) #append that value to the list of generation0
    number_of_generations = inputValidInt("Please enter a number for the number of generations: ", min = 5, max = 25) #a validation def is used to validate the user’s input
    generation0.append(number_of_generations) #append that value to the list of generation0
    return generation0 # return all of the choices in 1 list

#this function gives the user the opportunity to either set a disease trigger point or to decide not to use a trigger point
def setTriggerPoint():
    triggerPoint = 0
    doTrigger = inputValidInt("Please type 1 or 2 respectively as to whether you want to have a disease trigger or not: ") #asks the user whether they want a trigger or not
    if doTrigger == 1: #if they decided to use a trigger
        triggerPoint = inputValidFloat("Please enter a number of 0 or above for the disease trigger point (in thousands): ", min = 0, noMax = True ) #get a valid trigger point from the user
    return doTrigger , triggerPoint #return whether they want to use the trigger point as a Boolean, and the trigger point itself

#this function displays to the user the initial conditions they have entered
def displayGeneration0(generation0):
    print("Number of Juveniles: ", generation0[0])
    print("Number of Adults: ", generation0[1])
    print("Number of Seniles: ", generation0[2])
    print("Survival rate of Juveniles: ", generation0[3])
    print("Survival rate of Adults: ", generation0[4])
    print("Survival rate of Seniles: ", generation0[5])
    print("Birth Rate: ", generation0[6])
    print("Number of Generations: ", generation0[7])
    
#this function does all the necessary calculations to find the number of juveniles, adults and seniles in each generation and displays the results
def runSimulation(generation0, doTrigger, triggerPoint):
    generations = [["Generation", "Juveniles", "Adults", "Seniles", "Total"]] #the list that will contain all the data
    genx = [] #a temporary list to hold the values of each generation separately
    gen0 = [0, generation0[0], generation0[1], generation0[2], (generation0[0] + generation0[1] + generation0[2])] #input initial population to the 'generations' list
    print(generations)
    print(gen0)
    generations.append(gen0) #puts initial conditions into list
    for gen in range(2, generation0[7] + 2): #for each generation
        number_of_juveniles = generations[gen - 1][1] * generation0[3] #set the current generation’s number of juveniles to be equal to the previous number of juveniles multiplied by their survival rate
        number_of_adults = generations[gen - 1][2] * generation0[4] #set the current generation’s number of adults to be equal to the previous number of adults multiplied by their survival rate
        number_of_seniles = generations[gen - 1][3] * generation0[5] #set the current generation’s number of seniles to be equal to the previous number of seniles multiplied by their survival rate
        if doTrigger == True and (float(number_of_juveniles + number_of_adults + number_of_seniles)) >= triggerPoint: #if the user has requested for the trigger point and total population is bigger than the trigger point
            diseaseFactor = random.randint(20,50) / 100 #creates a random variable between 0.2 and 0.5
            number_of_juveniles = number_of_juveniles * diseaseFactor #multiply juveniles by the disease factor
            number_of_seniles = number_of_seniles * diseaseFactor #multiply seniles the disease factor
        TEMP_number_of_juveniles = number_of_adults * generation0[6] #this variable must be made to calculate the new amount of juveniles without affecting the number for later calculations
        TEMP_number_of_adults = number_of_juveniles #this variable must be made to calculate the new amount of juveniles without affecting the number for later calculations    
        number_of_seniles = round(number_of_seniles + number_of_adults, 3) #set number of new seniles
        number_of_juveniles = round(TEMP_number_of_juveniles, 3) #set number of new juveniles
        number_of_adults = round(TEMP_number_of_adults, 3) #set number of new adults
        total = round(number_of_juveniles + number_of_adults + number_of_seniles, 3) #calculates the total number of greenflies
        genx.append(gen - 1) #append value to the temporary list 'genx'
        genx.append(number_of_juveniles) #append value to the temporary list 'genx'
        genx.append(number_of_adults) #append value to the temporary list 'genx'
        genx.append(number_of_seniles) #append value to the temporary list 'genx'
        genx.append(total) #append value to the temporary list 'genx'
        print(genx) #displays the generation’s result with the number of generation
        generations.append(genx) #add a new entry to the list for the generation
        genx = []
    return generations #returns the results calculated

#this function saves the results of the calculation to a file
def saveFile(generations):
    save = False #the value of save is set to True when the file has been saved
    while save == False: #keeps running until the file is successfully saved
        Valid = False #the value of valid is set to True when the file name has been validated
        while Valid == False: #keeps running until the file name is successfully validated
            filename = input("Please enter a suitable file name: ")
            Valid = True #to break the while loop if there are no invalid characters
            for c in filename: #check whether user entered suitable file name by checking whether each character is a number or letter.
                if not c.isalnum(): #if the character is not a letter
                    Valid = False #change valid to false to continue the while loop
                    print(filename, " is not valid, please enter a valid name. ")
                    break
        filename = os.path.expanduser("~\\" + filename + ".csv") #creates a space on computer to put the file in
        print(filename)
        if os.path.isfile(filename) == True: #if the file already exists
            print("This file already exists")
            answer = inputValidInt("Would you like to rewrite this file? \n1. Yes\n2. No \n", 1, 2) 
        else:
            answer = 1 #if we get to this else clause, then the file does not exist, so answer is set to 1, which means the program will write the file 
        if answer == 1:
            with open(filename, "w") as txtfile:
                for generation in generations: #for each generation
                    txtfile.write('"' + str(generation[0]) + '","' + str(generation[1]) + '","' + str(generation[2]) + '","' + str(generation[3]) + '","' + str(generation[4]) + '"\n') #writes the row of generation x
                txtfile.close() #closes the file
                print("The file has been written.")
                save = True #breaks out of the loop

generations = [] #make an empty list which will later on be the data structure which will contain all of the generations’ data
initialConditionsEntered = False #set variable to False to restrict the user from choosing some options over the others in the future
runSimulationChosen = False #set variable to False to restrict the user from choosing some options over the others in the future
doTrigger = False #until the user chooses to use a trigger point, the default is to not use a trigger point
triggerPoint = 0 #initialise the triggerpoint variable
while True: #repeat forever
    print("\nMenu options are:" \
    "\n 1. Enter the initial conditions" \
    "\n 2. Have a total population size trigger point for disease" \
    "\n 3. Choose to display the initial conditions" \
    "\n 4. Run the simulation" \
    "\n 5. Export the simulation results" \
    "\n 6. Quit")
    menu = inputValidInt("Please enter the number of your option: ", 1, 6) #makes sure the user enters a valid menu option
    if (menu == 3 or menu == 4 or menu == 5) and initialConditionsEntered == False: #unless the user has chosen to input conditions, some of the menu options make no sense and therefore are restricted
        print("This is not an option until you have entered the initial conditions")
        continue
    if menu == 5 and runSimulationChosen == False: # unless the user has run the simulation, the program won't let them export the data
        print("This is not an option until you have run the simulation")
        continue
    if menu == 1: #if the user chose the first menu option
        generation0 = getInitialConditions() #get the initial conditions of the juveniles, adults and seniles; their survival rates; birth rate; and number of generations put in a variable
        generations = [] #there are new initial conditions to put into the generations list and therefore we get rid of the old ones 
        initialConditionsEntered = True #unlocks other menu entries
    if menu == 2: #if the user chose the second menu option
        doTrigger, triggerPoint = setTriggerPoint() #stores the results of whether the user wants to use a trigger point and on what level
    if menu == 3: #if the user chose the third menu option
        displayGeneration0(generation0) #displays the initial conditions of the juveniles, adults and seniles; their survival rates; birth rate; and number of generations to the user
    if menu == 4: #if the user chose the fourth menu option
     generations = runSimulation(generation0, doTrigger, triggerPoint)#run simulation and save the results in the generations list
     runSimulationChosen = True
    if menu == 5: #if the user chose the fifth menu option
        saveFile(generations) #saves the file with a suitable name and exports it to a text file
    if menu == 6: #if the user chose the sisxth menu option
        print("Program is now closing, press ENTER to accept")
        time.sleep(2)
        exit() #quits this simulation
