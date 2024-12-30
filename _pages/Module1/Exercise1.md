---
layout: exercise
language: "python"
permalink: "Module1/Exercise1"
title: "CS 372: Module 1: Python Arithmetic Operations"
excerpt: "CS 372: Module 1: Python Arithmetic Operations"
canvasasmtid: "219623"
canvaspoints: "1.5"
canvashalftries: 5

info:
  comments: "true"
  prev: "./Video1"
  next: "./Video2"
  points: 1.5
  instructions: "<p>You're a cashier, but you only have quarters and nickels.  Your boss told you to use the following algorithm: use as many quarters as you can to get under the amount, then add nickels until you go over the amount.  For example, to make 73 cents, we'd use two quarters to get to 50, and then we'd add 5 nickels until we got to 75.</p><p>Fill in the code below to follow your boss's algorithm.  The code has imported the <code>math</code> library, and you can use <code>math.ceil(number)</code> to round a number up and <code>math.floor(number)</code> to round a number down.  Your solution should only be a few lines and it should only have arithmetic operations; you won't need any loops, if statements, or anything like that (we will talk about those momentarily)</p>"
  goals:
    - To manipulate variables and types in python
    - To apply arithmetic expressions in python
    
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    var pos = feedbackString.trim();
  correctcheck: |
    pos.includes("2 Quarters, 5 Nickels.2 Quarters, 4 Nickels.1 Quarters, 0 Nickels.")
  incorrectchecks:
    - incorrectcheck: |
        pos.includes("2.92 Quarters, 0 Nickels.2.64 Quarters, 0 Nickels.1.0 Quarters, 0 Nickels.")
      feedback: "Try again.  It looks like you're doing a regular divide by 25 instead of a floor divide.  Try <code>change//25</code>." 
    - incorrectcheck: |
        pos.includes("0 Quarters, 0 Nickels.0 Quarters, 0 Nickels.0 Quarters, 0 Nickels.")
      feedback: "Try again.  It looks like you haven't updated num_quarters or num_nickels" 
 
files:
  - filename: "student.py"
    name: driver
    ismain: false
    isreadonly: false
    isvisible: true
    code: | 
         import math
         def make_change(change):
             """
             Make change according to the above specifications
             Parameters
             ----------
             change: int
                Amount of change to make
             """
             ## TODO: Change these two variables to reflect the actual
             ## change that's made
             num_quarters = 0
             num_nickels = 0
             print("{} Quarters, {} Nickels".format(num_quarters, num_nickels), end='.')


  - filename: "main.py"
    ismain: true
    name: main
    isreadonly: true
    isvisible: true
    code: |
        # Run some tests on the method
        make_change(73)
        make_change(66)
        make_change(25)
        
openFilesOnLoad: ["main.py", "student.py"]
---
