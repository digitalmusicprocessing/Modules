---
layout: exercise
language: "pyodide"
permalink: "Module14/Exercise4"
title: "CS 372: Module 14: FFTConvolve Implementation Exercise"
excerpt: "CS 372: Module 14: FFTConvolve Implementation Exercise"
canvasasmtid: "219615"
canvaspoints: "2"
canvashalftries: 5

info:
  comments: "true"
  prev: "./Video4.html"
  points: 2
  instructions: "<p>Fill in the <code>myfftconvolve</code> method to implement a DFT-based convolution similar to what we just talked about, but where the length of the zeropadded array is rounded up to the nearest power of two above M+N-1, so that the Fast-Fourier Transform (FFT) algorithm can run.  Since you've rounded the length up, at the end, you'll need to cut down and return the slice 0:M+N-1.</p>"
  packages: "numpy"
  goals:
    - To leverage the convolution/multiplication property to implement convolution efficiently with an FFT
    - To use slices in numpy arrays
    
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    
  correctcheck: |
    pyodide.globals.get("correct")
  incorrectchecks:
    - incorrectcheck: |
        pyodide.globals.get("lenconv1") == 512
      feedback: "Try again.  It looks like you may have forgotten to slice the return array down to the first M+N-1 samples." 

files:
  - filename: "student.py"
    name: driver
    ismain: false
    isreadonly: false
    isvisible: true
    height: 550
    code: | 
        import numpy as np
        def myfftconvolve(x, y):
            """
            Parameters
            ----------
            x: ndarray(N)
                Samples in the first array
            y: ndarray(M)
                Samples in the second array
            
            
            Returns
            -------
            ndarray(M+N-1)
                The result of the convolution
            """
            M = len(x)
            N = len(y)
            # Round M+N-1 up to the nearest power of 2
            K = int(2**np.ceil(np.log2(M+N-1)))
            xz = np.zeros(K)
            yz = np.zeros(K)
            ## TODO: Put x at the beginning of xz and y at the beginning of yz
            ## Then, take the DFT of xz and yz with np.fft.fft
            ## Then, multiply the DFTs and invert them with np.fft.ifft
            ## Finally, return the first M+N-1 samples of the result
            



  - filename: "main.py"
    ismain: true
    name: main
    isreadonly: true
    isvisible: true
    code: |
        np.random.seed(0)
        x = np.random.randn(100)
        y = np.random.randn(200)
        conv1 = myfftconvolve(x, y)
        conv2 = np.convolve(x, y)
        correct = False
        lenconv1 = len(conv1)
        if len(conv1) == len(conv2): 
            correct = np.allclose(conv1, conv2)
        

openFilesOnLoad: ["main.py", "student.py"]
---

