---
layout: exercise
language: "python"
permalink: "Module1/Exercise3"
title: "CS 372: Module 1: Python Methods And Conditionals"
excerpt: "CS 372: Module 1: Python Methods And Conditionals"
canvasasmtid: "219624"
canvaspoints: "1.5"
canvashalftries: 5

info:
  comments: "true"
  prev: "./Video3"
  points: 1.5
  instructions: "<p>Just one more exercise in this module!  At a pressure of 1 atmospheres, water exists in a liquid state between 32 and 212 degrees Fahrenheit.  Write a method called <code>is_liquid</code> that takes two parameters.  The first is the temperature in degrees Fahrenheit.  The second is the pressure in atmospheres.  If the pressure is 1, return <code>True</code> if water is a liquid or <code>False</code> otherwise.  If the pressure is not 1, return <code>None</code> to indicate that this is unknown (for the purposes of this exercise)."
  goals:
    - To define methods in python
    - To implement boolean expressions and if statements in python
    
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    var pos = feedbackString.trim();
  correctcheck: |
    pos.includes("False.True.False.None.None.")
  incorrectchecks:
    - incorrectcheck: |
        pos.includes("True.False.True.None.None.")
      feedback: "Try again.  Somehow you got the opposite logic here!" 
    - incorrectcheck: |
        pos.includes("False.True.False.True.True.")
      feedback: "Try again.  Don't forget to return <code>None</code> if the pressure is not 1" 
 
files:
  - filename: "student.py"
    name: driver
    ismain: false
    isreadonly: false
    isvisible: true
    code: | 
         ## TODO: Define the is_liquid method here


  - filename: "main.py"
    ismain: true
    name: main
    isreadonly: true
    isvisible: true
    code: |
        # Run some tests on the method
        print(is_liquid(18, 1), end='.')
        print(is_liquid(100, 1), end='.')
        print(is_liquid(300, 1), end='.')
        print(is_liquid(100, 2), end='.')
        print(is_liquid(90, 3), end='.')
        
openFilesOnLoad: ["main.py", "student.py"]
---
