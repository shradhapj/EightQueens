#import random to generate random population
import random
#import sleep to slow down computation
from time import sleep

class EightQueens:
    #solution - one of the pre-defined soution to 8-Queen's problem
    solution = [0, 4, 7, 5, 2, 6, 1, 3]
    
    #computed_solution - this list will have the final computed solution to 8-Queen's problem
    computed_solution = [None] * len(solution)
    
    #GlobalPopulation - List of all elements with fitness/score not equal to 0/
    GlobalPopulation = []

    #Function to generate initial population(of 5 members) having length as that of the solution 
    def generatePopulation(self):
        population = []
        for i in range(0,5):
            element = []
            while len(element) < len(self.solution):
                number = random.randint(0,len(self.solution))
                if number not in element:
                    element.append(number)
            population.append(element)
        return population

    #Function to score the population and store the list along-with score in a dictionary
    def scorePopulation(self,population,solution):
        score_dict = {}
        for i in range(0,len(population)):
            score = 0
            current_pop = population[i]
            for j in range(0,len(population[i])):
                if solution[j] == population[i][j]:
                    score += 1
            if score > 0:
                self.GlobalPopulation.append(population[i])
                score_dict[tuple(current_pop)] = score        
        return score_dict

    '''Below is the Function for Crossover and Mutation
        Crossover : An element with highest score is selected as Pivot and is combined with other elements in population
        Mutation : One unmatched element in pivot is mutated or altered to have a value from the actual solution
    '''
    def crossoverAndMutation(self,score_dict):
         sorted_dict = sorted(score_dict.items(),key = lambda kv : (kv[1],kv[0]),reverse=True)
         newPopulation = []
         pivot = list(sorted_dict[0][0])
         print("Pivot: {}\n".format(pivot))
         flag = [False] * len(pivot)
         
         for i in range(0,len(pivot)):
             if pivot[i] != self.solution[i]:
                 pivot[i] = self.solution[i]
                 flag[i] == True
                 break
                 
         for i in range(0,len(pivot)):
             if pivot[i] == self.solution[i]:
                 flag[i] = True

         for j in range(1,len(score_dict)):
             element = []
             for i in range(0,len(pivot)):
                 if flag[i] == True:
                     element.append(pivot[i])
                     continue
                 else:
                     element.append(list(sorted_dict[j][0])[i])
             self.GlobalPopulation.append(element)      
         return self.GlobalPopulation    

    #Function to check if new popuation contains the solution, if yes it returns true.     
    def check(self,newPopulation1,solution):
        for i in range(0,len(newPopulation1)):
            if newPopulation1[i]==solution:
                self.computed_solution = newPopulation1[i]
                return True
            
            
    
            
            
#Creating object of the EightQueens class.                
eq = EightQueens()

#Calling generatePopulation function to generate initail population
population = eq.generatePopulation()
print("Population : {}\n".format(population))


#Calling the scorePopulation to calculate the score of initial population
score_dict = eq.scorePopulation(population,eq.solution)

#Calling Mutation and crossover function
newPop= eq.crossoverAndMutation(score_dict)

#checking if the population has the solution
answer = eq.check(newPop,eq.solution)

#while population does not have the solution, run the above steps on repeat
while not answer:
    score_dictionary = eq.scorePopulation(newPop,eq.solution)
    newPopulation = eq.crossoverAndMutation(score_dictionary)
    print("Population : {}\n".format(newPopulation))
    answer = eq.check(newPopulation,eq.solution)
    sleep(7)

#When population has the solution, the problem is solved eventually    
if answer:
    print("Solution arrived! This is the solution: {}\n".format(eq.computed_solution))    
    
    


    



