In order to run my tests, you will need python3 installed and accessible from the BASH terminal as well as networkx and matplotlib installed for graph outputs.

	networkx can be installed by running `pip install networkx`
	matplotlib can be installed by running `python -m pip install -U matplotlib`

To test, run the script while rooted in the directory of the shell script.
The script runs all files in the associated test_cases/inputs directory and outputs in the associated test_cases/outputs directory.

WARNING: For the exact tests, the 95-vertex test case which runs for ~20 minutes is included in inputs. To not overwrite its output I recommend moving it from the test running folder when running the script so that the runner only take ~5 minutes rather than ~20.

Argument possibilities:
	<none> 	= runs exact solution on exact test cases
	a	= runs approximate solution on approximate test cases
	approx	= runs approximate solution on approximate test cases
	e	= runs exact solution on exact test cases
	exact	= runs exact solution on exact test cases
	<other>	= fails to run

This shell script is identical to the one within the approximate_solution directory, but defaults to running the exact solution if none is specified.

Test cases must be formatted as follows:
	1. First line is a number N which states the number of edges in the graph
	2. The next N lines are the edge pairs formatted as `x y` (x <space> y)
	3. The final line states the name of the test so that the graph output may be associated properly

Outputs are formatted as follows:
	1. First line is a number N which states the number of vertices in the minimum vertex cover of the passed graph
	2. The next N lines are the vertices in the cover
	3. The final line states the runtime of the algorithm in seconds

Output graphs have the input graph on the left and covered graph on the right