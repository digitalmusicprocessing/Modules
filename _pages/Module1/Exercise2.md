---
layout: exercise_python
permalink: "Module1/Exercise2"
title: "CS 372: Module 1: Python Slicing"
excerpt: "CS 372: Module 1: Python Slicing"
canvasasmtid: "168271"
canvaspoints: "1.5"
canvashalftries: 5

info:
  comments: "true"
  prev: "./Video2"
  next: "./Video3"
  points: 1.5
  instructions: "<p>One thing I find myself doing all the time is converting formats of multimedia data with python scripts.  Part of this is just getting the file paths correct.  Let's say I wanted to convert an audio file with a .wav format to a .mp3 format.  Write the code comes up with the correct .mp3 target filename using string slices and string concatenation.  <b>Hint:</b> You can use a negative index as the end of a slice.</p>"
  goals:
    - To use slicing notation in python
    - To apply string concatenation in python
    
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    var pos = feedbackString.trim();
  correctcheck: |
    pos.includes("drake.mp3_justinbieber.mp3_drscoville.mp3")
  incorrectchecks:
    - incorrectcheck: |
        pos.includes("drake.wav_justinbieber.wav_drscoville.wav")
      feedback: "Try again.  Looks like the filenames are still in wav format." 
 
files:
  - filename: "Student Code"
    name: driver
    ismain: false
    isreadonly: false
    isvisible: true
    code: | 
         def convert_format(filename):
             """
             Convert the format of a string
             Parameters
             ----------
             filename: string
              Name of some file that ends in .wav
             """
             ## TODO: Change result so that it ends with .mp3
             result = filename
             return result


  - filename: "Test Code Block"
    ismain: true
    name: main
    isreadonly: true
    isvisible: true
    code: |
        # Run some tests on the method
        print(convert_format("drake.wav"), end='_')
        print(convert_format("justinbieber.wav"), end='_')
        print(convert_format("drscoville.wav"))
        
---
