---
layout: exercise
language: "pyodide"
permalink: "Module11/Exercise1"
title: "CS 372: Module 11: STFT Window Extraction"
excerpt: "CS 372: Module 11: STFT Window Extraction"
canvasasmtid: "219611"
canvaspoints: "1.5"
canvashalftries: 5

info:
  comments: "true"
  prev: "./Video1"
  next: "./Video2"
  points: 1.5
  instructions: "<p>The purpose of this exercise is to get you to hone in on the key step of extracting a window from a signal given a window length and a hop length.  This was part of the <code>specgram</code> method on the previous page, but I can't emphasize it enough, so let's try it again (see if you can do it without looking).</p>"
  packages: "numpy"
  goals:
      - To implement STFT window functions
    
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false

  correctcheck: |
    pyodide.globals.get("res") == "50,51,52,53,54,55,56,57,58,59:160,161,162,163,164,165,166,167,168,169"
  incorrectchecks:
    - incorrectcheck: |
        false
      feedback: "Try again.  It looks like you haven't filled in the audio yet." 

files:
  - filename: "student.py"
    name: driver
    ismain: false
    isreadonly: false
    isvisible: true
    code: | 
        import numpy as np
        def get_window(x, win, hop, j):
            """
            Return the audio in the jth window
            Ex) First window (j = 0) x[0:win]
            Ex) Second window (j = 1) x[hop:hop+win]
            Ex) Third window (j = 2) x[2hop:2hop+win]
            
            Parameters
            ----------
            x: ndarray(N)
              Audio samples
            win: int
              Window length
            hop: int
              Hop length
            j: int 
              Window index
            """
            return x # TODO: This is a dummy value



  - filename: "main.py"
    ismain: true
    name: main
    isreadonly: true
    isvisible: true
    code: |
        x = np.arange(1024)
        win = 10
        hop = 5
        x1 = get_window(x, win, hop, 10)
        x1 = ",".join([str(f) for f in x1])
        x2 = get_window(x, win, hop, 32)
        x2 = ",".join([str(f) for f in x2])
        res = "{}:{}".format(x1, x2)
        
openFilesOnLoad: ["main.py", "student.py"]
---