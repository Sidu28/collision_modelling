# Do NOT add any other import statements.
# Don't remove these import statements.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import copy
from numpy.linalg import inv

#force calculator method
def force_vector_calc(distances,size):
    force_vec = np.empty([size-1,1])
    for i in range(1,len(distances)):
        force=0
        for j in range(1,len(distances)):
            if(i != j):
                force+= 1/(distances[j]-distances[i])
        force_vec[i-1] = force
        
    return force_vec

#one iteration of the problem
def problem_iteration(distances, force_vec,size):
    derivative_matrix = np.empty([size-1,size-1])
    for i in range (size-1):
        derivative_array = [0]
        for j in range (size-1):
            if(i !=j ):
                force_derivative = (-1)/((distances[j] - distances[i])**2)
                derivative_array.append(force_derivative)
        derivative_matrix[i] = derivative_array
    
    for i in range (len(derivative_matrix)):
        for j in range (len(derivative_matrix[0])):
            if derivative_matrix[i][j]<0:
                derivative_matrix[i][j] *= -1
                
            
            
    print("This is Derivative Matrix: ")
    print(derivative_matrix)
    
    inverse_matrix = np.linalg.inv(derivative_matrix)
    delta_r_array = np.dot(inverse_matrix,force_vec)
    
    return delta_r_array
        
        
def problem_loop(distances,size):
    #distances = np.genfromtxt(filename, delimiter=",",dtype='unicode').astype(float)
    
    #distances = [1,4,9,16]
    force_vec = force_vector_calc(distances,size)
    delta_r = problem_iteration(distances,force_vec,size)
    new_distances = distances
    
    print("This is the original Delta R: ",delta_r)
    for i in range(4):
        for i in range(1,len(new_distances)):
            new_distances[i] = new_distances[i] + delta_r[i-1,0]

        new_force_vec = force_vector_calc(new_distances,size)

#        if (new_force_vec[i]<=0.001 for i in range(len(new_force_vec))):
#            break
#
#        else:
        delta_r = problem_iteration(new_distances, new_force_vec,size)
#            print(new_distances)

    return new_distances



def main():
    a = [0,0.5,1,2]
    print ("FINAL ANSWER:",problem_loop(a,len(a)))


# This if-condition is True if this file was executed directly.
# It's False if this file was executed indirectly, e.g. as part
# of an import statement.
if __name__ == "__main__":
    main()

