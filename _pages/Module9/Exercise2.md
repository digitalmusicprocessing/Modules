---
layout: exercise
language: "python"
permalink: "Module9/Exercise2"
title: "CS 372: Module 9: Exercise 2"
excerpt: "CS 372: Module 9: Exercise 2"
canvasasmtid: "219643"
canvaspoints: "1.5"
canvashalftries: 5

info:
  comments: "true"
  prev: "./Video2"
  points: 1.5
  instructions: "<p>So far we've been talking about the frequencies in terms of integer number of cycles over a particular interval, but if we know how many samples are in that interval and what the sample rate is, we can devise a formula to determine what the frequency actually is in hz.  This will move us towards being able to detect notes in real audio using the DFT.  In this exercise, given a particular frequency index in either the cosine or sine array of DFT dot products, as well as the number of samples in the signal and the sample rate of the signal, return the frequency associated to the sine or cosine at a particular index $k$ in hz.</p><p><b>Hint:</b> The equation is in terms of k, N, and sr only.  You want to end up with hz, which is cycles per second.  k is the number of cycles / interval.  N is the number of samples / interval.  sr is the number of samples / second.  So you have to arrange them into an equation that ends up in cycles / second.</p>"
  packages: "numpy"
  goals:
    - To translate from indices of the DFT to frequencies of the DFT
    
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    var pos = feedbackString.trim();
  correctcheck: |
    pos.includes("441.2205.11025")
  incorrectchecks:
    - incorrectcheck: |
        pos.includes("0.0.0")
      feedback: "Try again.  You need to return the frequency in hz, not 0"
files:
  - filename: "student.py"
    name: driver
    ismain: false
    isreadonly: false
    isvisible: true
    height: 400
    code: | 
          def index_to_freq(k, N, sr):
              """
              Given a particular frequency index in either the
              cosine or sine array of DFT dot products, as well
              as the number of samples in the signal and the sample
              rate of the signal, return the frequency associated
              to the sine or cosine at a particular index $k$ in hz

              Parameters
              ----------
              k: int
                  Frequency index
              N: int
                  Number of samples
              sr: int
                  Sample rate
              Returns
              -------
              Frequency, in hz, associated to k
              """
              return 0 ## TODO: This is a dummy value


  - filename: "main.py"
    ismain: true
    name: main
    isreadonly: true
    isvisible: true
    code: |
        res = "%i"%index_to_freq(1, 100, 44100)
        res += ".%i"%index_to_freq(10, 200, 44100)
        res += ".%i"%index_to_freq(11025, 44100, 44100)
        print(res)
        
        
openFilesOnLoad: ["main.py", "student.py"]
---