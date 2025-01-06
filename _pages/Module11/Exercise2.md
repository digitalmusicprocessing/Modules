---
layout: exercise
language: "pyodide"
permalink: "Module11/Exercise2"
title: "CS 372: Module 11: Blackman-Harris Window"
excerpt: "CS 372: Module 10: Blackman-Harris Window"
canvasasmtid: "219612"
canvaspoints: "2"
canvashalftries: 5

info:
  comments: "true"
  prev: "./Video2"
  next: "./Video3"
  points: 2
  instructions: "<p>The purpose of this exercise is to get you practice implementing window functions to use with the short-time Fourier Transform.  The three term Blackman-Harris Window is defined as \\[ w[n] = 0.42 - 0.5 \\cos(2 \\pi n / N) + 0.08 \\cos(4 \\pi n / N) \\] </p><p>And a plot is shown below:</p><img src = \" ../images/Module11/Blackman.svg\"><p> Sometimes this window is better to use than the Hann window for certain analyses.  Implement this window below</p>"
  packages: "numpy"
  goals:
      - To implement STFT window functions
    
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  correctcheck: |
    pyodide.globals.get("res") == "-0.0000000000,0.0000033885,0.0000135546,0.0000304999,0.0000542271,0.0000847403,0.0001220442,0.0001661451,0.0002170500,0.0002747673:-0.0000000000,0.0000135546,0.0000542271,0.0001220442,0.0002170500,0.0003393063,0.0004888925,0.0006659053,0.0008704591,0.0011026854"

files:
  - filename: "student.py"
    name: driver
    ismain: false
    isreadonly: false
    isvisible: true
    code: | 
        import numpy as np
        def get_blackman_harris(N):
            """
            Compute the Blackman-Harris Window for a window N samples long
            """
            w = np.zeros(N)
            ## TODO: Fill this in
            return w



  - filename: "main.py"
    ismain: true
    name: main
    isreadonly: true
    isvisible: true
    code: |
        w1 = get_blackman_harris(1024)[0:10]
        w2 = get_blackman_harris(512)[0:10]
        w1 = ",".join(["{:.10f}".format(f) for f in w1])
        w2 = ",".join(["{:.10f}".format(f) for f in w2])
        res = "{}:{}".format(w1, w2)
        
openFilesOnLoad: ["main.py", "student.py"]
---
