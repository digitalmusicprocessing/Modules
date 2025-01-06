---
layout: exercise
language: "pyodide"
permalink: "Module9/Exercise1"
title: "CS 372: Module 9: Exercise 1"
excerpt: "CS 372: Module 9: Exercise 1"
canvasasmtid: "219642"
canvaspoints: "1.5"
canvashalftries: 5

info:
  comments: "true"
  prev: "./Video1"
  next: "./Video2"
  points: 1.5
  instructions: "Fill in the <code>has_freq</code> method that determines whether a sinusoid of a particular frequency exists in a signal, using Fourier dot products."
  packages: "numpy"
  goals:
    - To use numpy element-wise operations with trig functions
    - To apply Fourier projection to check for the existence of a sinusoid
    
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
      
  correctcheck: |
    pyodide.globals.get("res") == "1,1,0,0,1"
  incorrectchecks:
    - incorrectcheck: |
        pyodide.globals.get("res") == "0,0,0,0,0"
      feedback: "Try again.  It looks like you aren't returning True for things that are actually there."
    - incorrectcheck: |
        pyodide.globals.get("res") == "0,0,0,0,1"
      feedback: "Try again.  It's OK if either a sine OR a cosine is there." 

files:
  - filename: "student.py"
    name: driver
    ismain: false
    isreadonly: false
    isvisible: true
    height: 600
    code: | 
        import numpy as np
        def has_freq(x, f, thresh):
            """
            Determine whether a frequency is contained in a signal
            
            Parameters
            ----------
            x: ndarray(N)
                The signal of interest
            f: int
                The frequency to check
            thresh: float
                If either the sine component or the cosine
                component are above this threshold, then consider
                the frequency f to exist
            
            Returns
            -------
            True if the frequency is in x, and False otherwise
            """
            N = len(x)
            n = np.arange(N)/N
            c = np.sum(x*np.cos(2*np.pi*f*n))
            ## TODO: Fill in sine part, and if either is > thresh, 
            ## then say it has the frequency
            
            return False


  - filename: "main.py"
    ismain: true
    name: main
    isreadonly: true
    isvisible: true
    code: |
        N = 100
        t = np.arange(N)/N
        y = np.cos(2*np.pi*2*t) + np.sin(2*np.pi*1*t) + np.cos(2*np.pi*5*t - np.pi/3)
        resarr = np.array([has_freq(y, f, 0.1) for f in np.arange(1, 6)], dtype=int)
        res = ""
        for i, r in enumerate(resarr):
            res += "%i"%r
            if i < len(resarr)-1:
                res += ","
        
openFilesOnLoad: ["main.py", "student.py"]
---