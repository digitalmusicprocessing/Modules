---
layout: exercise_pyodide
permalink: "Module16/Exercise3"
title: "CS 372: Module 16: Matrix Exercise"
excerpt: "CS 372: Module 16: Matrix Exercise"
canvasasmtid: "172213"
canvaspoints: "2"
canvashalftries: 5

info:
  comments: "true"
  prev: "./Video3"
  next: "./Video4"
  points: 2
  instructions: "Modify the <code>average_columns</code> code to compute the average of every column with a matrix multiplication.  The easiest way to do this is to create a row matrix of 1s that you multiply on the left.  This matrix multiplication will perform the sum of all elements in each column.  Then, you should element-wise divide the result by the number of rows to finalize the average.  Use the command <code>np.ones((1, num))</code> to create a row matrix with <code>num</code> elements, then use <code>np.dot(A, B)</code> to multiply two matrices."
  packages: "numpy"
  goals:
    - Setup matrices with the proper dimensions
    - Perform matrix multiplication in numpy
    
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    feedback.setValue("" + pyodide.globals.avg + "");
  correctcheck: |
    "" + pyodide.globals.avg == "5,4,6,6,4"
  incorrectchecks:
    - incorrectcheck: |
        "" + pyodide.globals.avg == "0,0,0,0,0"
      feedback: "Try again. It looks like you're still returning the dummy values." 

    - incorrectcheck: |
        "" + pyodide.globals.avg == "56,46,62,64,40"
      feedback: "Try again.  You're very close!  Be sure to divided the averages by M." 


files:
  - filename: "Student Code"
    name: driver
    ismain: false
    isreadonly: false
    isvisible: true
    height: 450
    code: | 
          import numpy as np

          def average_columns(A):
            """
            Compute the average of each column of a matrix using only
            matrix multiplication and no loops

            Parameters
            ----------
            A: ndarray(M, N)
                A matrix
            
            Returns
            -------
            ndarray(N)
                An average across all columns
            """
            M = A.shape[0]
            N = A.shape[1]
            avg = np.zeros(N) # This is a dummy value
            ## TODO: Fill this in
            
            return avg
              



  - filename: "Test Code Block"
    ismain: true
    name: main
    isreadonly: true
    isvisible: true
    code: |
        np.random.seed(0)
        A = 10*np.random.rand(10, 5)
        avg = average_columns(A)
        avg = np.array(avg, dtype=int)
        
---
