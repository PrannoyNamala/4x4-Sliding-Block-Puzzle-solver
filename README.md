# 4x4-Sliding-Block-Puzzle-solver
The program takes the input state of a 4x4 Sliding Block Puzzle and returns the following:
  The list of all the states traversed
  Path to goal state
  
 All the returned parameters are in a text file
 
The input state is should be entered in the following order:
 01 02 03 04
 05 06 07 08
 09 10 11 12
 13 14 15 16
 
 * Here the numbers represent the order for input
 
 Messages will prompt if you have given a wrong or already entered input.
 For double digits numbers, input the following. 
 a = 10
 b = 11
 c = 12
 d = 13
 e = 14
 e = 15
 
 For the 
 
 No external libraries(like numpy) have been used in this code.
 
 The test cases used are:
 
Test Case 1: [[1, 2, 3, 4],[ 5, 6,0, 8], [9, 10, 7, 12] , [13, 14, 11, 15]]o/p file Test case 1.txt
Exmple to input this state : '123456089a7cdebf'

Test Case 2: [[1, 0, 3, 4],[ 5, 2, 7, 8], [9, 6, 10, 11] , [13, 14, 15, 12]]o/p file Test case 2txt

Test Case 3: [[0, 2, 3, 4],[ 1,5, 7, 8], [9, 6, 11, 12] , [13, 10, 14, 15]]o/p file Test case 3txt

Test Case 4: [[5, 1, 2, 3],[0,6, 7, 4], [9, 10, 11, 8] , [13, 14, 15, 12]]o/p file Test case 4txt

Test Case 5: [[1, 6, 2, 3], [9,5, 7, 4], [0, 10, 11, 8] , [13, 14, 15, 12]]o/p file Test case 5txt
