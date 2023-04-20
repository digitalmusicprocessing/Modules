---
layout: exercise_pyodide
permalink: "Module22/Exercise1"
title: "CS 372: Module 22: Softmax"
excerpt: "CS 372: Module 22: Softmax"
canvasasmtid: "174031"
canvaspoints: "2"
canvashalftries: 5

info:
  comments: "true"
  prev: "./Video1"
  next: "./Video2"
  points: 2
  instructions: "<p>Implement the softmax method that turns multiple neuron outputs into probabilities</p>"
  packages: "numpy"
  goals:
    - Implement the softmax method in python
    
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    let ref = 0.18184;
    let tol = 0.001
  correctcheck: |
    Math.abs(pyodide.globals.res[0] - ref) < tol
  incorrectchecks:
    - incorrectcheck: |
        pyodide.globals.res == 0
      feedback: "Try again.  It looks like you're still returning 0, but you need to evaluate the neural network layers in a loop" 

files:

  - filename: "Student Code"
    name: driver
    ismain: false
    isreadonly: false
    isvisible: true
    height: 600
    code: | 
        import numpy as np

        def softmax(u):
            """
            Implement the softmax method

            Parameters
            ----------
            u: ndarray(N)
              Input to softmax
              
            Returns
            -------
            ndarray
                Result of softmax
            """
            ret = np.zeros(len(u))
            ## TODO: Fill this in
            return ret



  - filename: "Test Code Block"
    ismain: true
    name: main
    isreadonly: true
    isvisible: true
    code: |
        np.random.seed(0)
        u = np.random.randn(10)
        res = softmax(u)

        
        
---
