---
layout: exercise_pyodide
permalink: "Module17Old/Exercise1"
title: "CS 472: Module 17: Warping Path Costs"
excerpt: "CS 472: Module 17: Warping Path Costs"
canvasasmtid: "115612"
canvaspoints: "1.5"
canvashalftries: 5

info:
  comments: "true"
  prev: "./Video1"
  next: "./Video2" 
  points: 1.5
  instructions: "Fill in the code below to sum up the distances in a cross-similarity matrix that a warping path passes through.  Programmatically, a warping path is actually a 2D array of [i, j].  For example, <p><code>[[0, 0], [0, 1], [1, 2], [2, 3]]</code></p> is a warping path.  It is possible to loop through this like <p><code>for idx in range(len(path)):<BR>&nbsp&nbsp&nbsp&nbspi = path[idx, 0]<BR>&nbsp&nbsp&nbsp&nbspj = path[idx, 1]</code></p>But, thanks to the wonders of python, you can unpack the inner arrays with a simpler loop<p><code>for i, j in path:</code></p>This is the starting point in the code below."
  packages: "numpy"
  goals:
    - To compute the cost of warping paths by referencing cross-similarity matrices
    
processor:  
  correctfeedback: "Correct!!" 
  incorrectfeedback: "Try again"
  submitformlink: false
  feedbackprocess: | 
    feedback.setValue("cost1 = " + pyodide.globals.cost1 + ", cost2 = " + pyodide.globals.cost2);
  correctcheck: |
    Math.floor(pyodide.globals.cost1) == 144 && Math.floor(pyodide.globals.cost2) == 279
  incorrectchecks:
    - incorrectcheck: |
        pyodide.globals.cost1 == 0 && pyodide.globals.cost2 == 0
      feedback: "Try again.  It looks like you're returning a cost of 0 for all warping paths." 


files:
  - filename: "CSM Computation"
    name: specgram
    ismain: false
    isreadonly: true
    isvisible: true
    height: 200
    code: | 
          import numpy as np

          def get_csm_fast(Y1, Y2):
              Y1Sqr = np.sum(Y1**2, 1)
              Y2Sqr = np.sum(Y2**2, 1)
              D = Y1Sqr[:, None] + Y2Sqr[None, :] - 2*Y1.dot(Y2.T)
              D[D < 0] = 0
              D = np.sqrt(D)
              return D



  - filename: "Student Code"
    name: driver
    ismain: false
    isreadonly: false
    isvisible: true
    height: 500
    code: | 
        def get_warppath_cost(C, path):
            """
            Compute the cost of a particular warping path by summing up
            the distances between the pairs that it traverses through
            a cross-similarity matrix

            Parameters
            ----------
            C: ndarray(M, N)
                An M x N cross-similarity matrix
            path: list of [i, j]
                The warping path
            
            Returns
            -------
            ndarray((N-win)/h+1)
                The audio offset function
            """
            cost = 0
            for i, j in path:
                ## TODO: Fill this in
                pass
            return cost



  - filename: "Test Code Block"
    ismain: true
    name: main
    isreadonly: true
    isvisible: true
    height: 500
    code: |
          N = 100
          t = np.linspace(0, 1, N)
          Y1 = np.zeros((N, 2))
          Y1[:, 0] = np.cos(2*np.pi*t)
          Y1[:, 1] = np.sin(4*np.pi*t)
          Y2 = np.zeros((N, 2))
          Y2[:, 0] = 1.3*np.cos(2*np.pi*(t**2))
          Y2[:, 1] = 1.3*np.sin(4*np.pi*(t**2))+0.1 
          C = get_csm_fast(Y1, Y2)
          path1 = [[i, i] for i in range(N)]
          path2 = [[i, 0] for i in range(N)] + [[N-1, j] for j in range(1, N)]
          cost1 = get_warppath_cost(C, path1)
          cost2 = get_warppath_cost(C, path2)

        
        
---
