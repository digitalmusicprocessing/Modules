---
layout: exercise
language: "pyodide"
permalink: "Module21/Exercise1"
title: "CS 372: Module 21: Evaluating Feedforward Neural Nets"
excerpt: "CS 372: Module 21: Evaluating Feedforward Neural Nets"
canvasasmtid: "219628"
canvaspoints: "2.5"
canvashalftries: 5

info:
  comments: "true"
  prev: "./Video1"
  next: "./Video2"
  points: 2.5
  instructions: "<p>Given a list of perceptron weight matrices <code>Ws</code> and a corresponding list of bias columns <b>bs</b>, implement the algorithm to evaluate a neural network on a particular input <code>x</code>, using the provided <code>logistic</code> function as the nonlinearity.  You will have to do this layer by layer in a loop.  As a reminder, the first layer is <code>logistic(Ws[0]*x+bs[0])</code>, where <code>*</code> means matrix multiplication.  Then the output of this is fed to <code>Ws[1]</code> and <code>bs[1]</code>, etc.</p>"
  packages: "numpy"
  goals:
    - Use a sequence of matrix multiplications to evaluate neural nets in numpy
    
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    let ref = 0.18348;
    let tol = 0.05
  correctcheck: |
    Math.abs(pyodide.globals.get("res") - ref) < tol
  incorrectchecks:
    - incorrectcheck: |
        pyodide.globals.get("res") == 0
      feedback: "Try again.  It looks like you're still returning the dummy value, but you need to evaluate the neural network layers in a loop" 

files:

  - filename: "student.py"
    ismain: false
    isreadonly: false
    isvisible: true
    code: | 
        import numpy as np

        logistic = lambda u: 1/(1+np.exp(-u))

        def nn_forward(Ws, bs, x):
            """
            Evaluate a feedforward neural network

            Parameters
            ----------
            Ws: list of ndarray(N_{i+1}, Ni)
                Weight matrices for each layer
            bs: list of ndarray(N_{i+1})
                Bias vectors for each layer
            x: ndarray(N_0)
                Input
              
            Returns
            -------
            ndarray
                Result of neural network evaluation
            """
            ## TODO: Evaluate the neural network on an input x

            return np.array([0]) # TODO: This is a dummy



  - filename: "main.py"
    ismain: true
    isreadonly: true
    isvisible: true
    code: |
        np.random.seed(0)
        As = [np.random.randn(4, 3), np.random.randn(5, 4), np.random.randn(1, 5)]
        bs = [np.random.randn(4), np.random.randn(5), np.random.randn(1)]
        x = np.random.randn(3)
        res = nn_forward(As, bs, x)[0]

        
openFilesOnLoad: ["main.py", "student.py"]
---
