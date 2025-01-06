---
layout: exercise
language: "pyodide"
permalink: "Module12/Exercise1"
title: "CS 372: Module 12: Exercise 1"
excerpt: "CS 372: Module 12: Exercise 1"
canvasasmtid: "219613"
canvaspoints: "1.5"
canvashalftries: 5

info:
  comments: "true"
  prev: "./Video1"
  next: "./Video2"
  points: 1.5
  instructions: "Fill in the <code>max_freq</code> method to compute the index of the maximum amplitude frequency from a set of complex DFT coefficients.  You can use <code>np.argmax</code> to find the index of the maximum element in an array.  You can also use <code>np.abs</code> to find the absolute value (complex modulus) of complex numbers."
  packages: "numpy"
  goals:
    - To use properties of complex numbers to compute amplitudes
    
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
      
  correctcheck: |
    pyodide.globals.get("idx") == "3"
  incorrectchecks:
    - incorrectcheck: |
        pyodide.globals.get("idx") == "4"
      feedback: "Be careful!  Make sure you're taking the absolute value / magnitude (np.abs) and not just the real component"

files:
  - filename: "student.py"
    name: driver
    ismain: false
    isreadonly: false
    isvisible: true
    height: 600
    code: | 
        import numpy as np
        def max_freq(F):
            """
            Compute the index of the maximum amplitude frequency
            in complex DFT coefficients
            
            Parameters
            ----------
            F: ndarray(K, dtype=np.complex)
                The first K coefficients of the complex DFT
            
            Returns
            -------
            int: Index of the maximum amplitude frequency
            """
            
            
            return 0 ## TODO: This is a dummy value


  - filename: "main.py"
    ismain: true
    name: main
    isreadonly: true
    isvisible: true
    code: |
        N = 100
        n = np.arange(N)/N
        y = np.cos(2*np.pi*3*n + np.pi/4) + 0.8*np.cos(2*np.pi*4*n)
        idx = max_freq(np.fft.fft(y)[0:10])
        
openFilesOnLoad: ["main.py", "student.py"]
---
