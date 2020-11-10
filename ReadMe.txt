____________________________________________________________________________________________

  CE 5290: Bi-directional Dijkstra Algorithm
____________________________________________________________________________________________

  
  ReadMe.txt

  This ReadMe contains instructions to run the Bi-directional Dijkstra's Algoritm
  code and generate the output to get the Shortest path distance between the input 
  pair of nodes.

____________________________________________________________________________________________

 CONTENTS
__________

	1) SYSTEM REQUIREMENTS
	2) GENERAL INFORMATION
	3) EXECUTION STEPS (In brief)
	4) INPUT
	5) OUTPUT
	6) SAVING THE RESULTS
	7) KNOWN ISSUES

____________________________________________________________________________________________

 1) SYSTEM REQUIREMENTS
________________________

Bi-directional Dijkstra's Algorithm code was written with Python 3.7.

The Python Intterpreter/ Libraries required to be installed to run the program are:

	Networkx (Designed by Aric Hagberg)
	Pandas
	Matplotlib
	Pylab
	Math

Use the package manager pip to install the above Libraries.


_____________________________________________________________________________________________
 
 2) GENERAL INFORMATION
________________________

The ZIP folder contains the following 2 important files. Make sure that both the files 
are stored in the same folder/directory before running the program.

i)  Bi-directional Dijkstra.py:
    This is the Python file with the code written for the algorithm.

ii) Input_CSV.csv:
    This is the Comma Separated Value (CSV) file through which the program will take
    the Graph input in the form of an Adjacency Cost matrix. 


Apart from this, the ZIP folder has following documents:

i)  Project Report consisting of Algorithm description and Pseudocode (PDF):
    Refer this document to know more about the algorithm and the basic structure of the code.

ii) Sample Output (PDF), Sample Output fig 1 (PNG), Sample Output fig 2 (PNG)


________________________________________________________________________________________________

 3) EXECUTION STEPS
____________________

The following steps are to be done:

i)	Place the Input_CSV file and the Python file in the same folder.
ii)	Open the Input_CSV file. Enter the required data and Save the file.
iii)	Run the Python file.
iv)	Enter the Number of nodes in the network. 
v)  	Choose the Source node and the Sink node.
vi)  	Save the generated figures if required.

__________________________________________________________________________________________________

 4) INPUT
___________

The code uses Pandas library to read and import data from the 'Input_CSV.csv' file.
This file can be run using MS Excel. Following are important points and guidelines
to be noted:

i) 	The file format contains the Column labels in the first row of the sheet and the 
	Row labels in the first column of the sheet, which are strictly integers from 1 to n. 
	This should not be changed.

ii)	The first cell in the sheet strictly contains the string 'Nodes'. This should not 
	be changed.

iii)	The Adjacency matrix stores the cost/weight of an arc (i, j) in the cell where the
	i th Row and the j th column intersect. Only the costs/weights of the existent arcs 
	in the network need to be filled in. Other cells will be automatically filled in as 0.

iv)	Upon running the program, enter the number 'n' of nodes in the network. The code
	will read and import the data to the graph from the first (n x n) matrix.

v) 	Choose the Source node and the Sink node.

__________________________________________________________________________________________________

 5) OUTPUT
___________

The following information is received as the output of the program:

i)	Upon entering the number of nodes, the plotted figure of the Network will be 
	generated. It can be saved for later purposes otherwise close the figure to proceed.

ii)	The iterations in both the Forward Dijkstra's from the Source node and the 
	Reverse Dijkstra's from the Sink node are detailed.

iii)  	The Program will terminate by showing the list of the nodes & arcs contained in the 
	Shortest path from the Source to the Sink. A figure will be generated with the Shortest
	path arcs highlighted in Red color.

__________________________________________________________________________________________________

 6) SAVING THE RESULTS
_______________________

i)	All the plots generated can be saved in PNG format.

ii)	The iterations details can be saved in the PDF format. 

__________________________________________________________________________________________________

 7) KNOWN ISSUES
_________________

i)	The Algorithm will not work if the network contains a negative cycle.

ii)	The Code will show error if points (i) & (ii) from 'INPUT' are not followed.

iii)	The result will be erroneous if the correct value is not provided in Execution step (iv)

iv)	In order to give another file as an input, replace the file name 'Input_CSV.csv' with the
	name of the enew file. Also, make sure that the new file format adheres to the 
	points (i) & (ii) from 'INPUT'.


___________________________________________________________________________________________________

By-
Hrishikesh Gadekar
___________________________________________________________________________________________________