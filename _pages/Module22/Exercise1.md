---
layout: exercise
language: "pyodide"
permalink: "Module22/Exercise1"
title: "CS 372: Module 22: Softmax"
excerpt: "CS 372: Module 22: Softmax"
canvasasmtid: "219629"
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
    Math.abs(pyodide.globals.get("res") - ref) < tol
  incorrectchecks:
    - incorrectcheck: |
        pyodide.globals.get("res") == 0
      feedback: "Try again.  It looks like you're still returning 0, but you need to evaluate the softmax function" 

files:

  - filename: "student.py"
    ismain: false
    isreadonly: false
    isvisible: true
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



  - filename: "main.py"
    ismain: true
    isreadonly: true
    isvisible: true
    code: |
        np.random.seed(0)
        u = np.random.randn(10)
        res = softmax(u)[0]

        
openFilesOnLoad: ["main.py", "student.py"]
---
