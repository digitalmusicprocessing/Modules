---
layout: exercise_pyodide
permalink: "Module11/Exercise2"
title: "CS 372: Module 11: Blackman-Harris Window"
excerpt: "CS 372: Module 10: Blackman-Harris Window"
canvasasmtid: "171269"
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
  feedbackprocess: | 
    function compareArrays(x, y) {
      let res = true;
      if (x.length != y.length) {
        res = false;
      }
      for (let i = 0; i < x.length && i < y.length; i++) {
        if (x[i] != y[i]) {
          res = false;
        }
      }
      return res;
    }
    let w1ref = [ -1.3877787807814457e-17, 0.0000033885058309951477, 0.000013554576124077955, 0.000030499869156250248, 0.000054227148311658535, 0.00008474028146535084, 0.00012204424012042525, 0.0001661450982995416, 0.00021705003118953348, 0.0002747673135410772 ];
    let w2ref = [-1.3877787807814457e-17, 0.000013554576124077955, 0.000054227148311658535, 0.00012204424012042525, 0.00021705003118953348, 0.00033930631782219667, 0.0004888924578373699, 0.0006659052997262799, 0.000870459096159959, 0.0011026854019042381];
  correctcheck: |
    compareArrays(pyodide.globals.w1, w1ref) && compareArrays(pyodide.globals.w2, w2ref)

files:
  - filename: "Student Code"
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



  - filename: "Test Code Block"
    ismain: true
    name: main
    isreadonly: true
    isvisible: true
    code: |
        w1 = get_blackman_harris(1024)[0:10]
        w2 = get_blackman_harris(512)[0:10]
        
---
