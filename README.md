python-challenge (WK3 Assignment): Python coding

Approach

The 4 python-challenge assignments were solved by using building blocks, i.e. several subroutines, from the class material as well as googling some of the solutions needed.

PyBank

PyBank was relatively straightforward although how to approach some of the tasks, e.g. the average of the changes in “Profit/Losses” was not immediately obvious. Fortunately, the data file was small and could be opened in Excel and different hypotheses could be tested. One challenge overcome (and useful in future applications) was that initially the csvwriter wrote to every other line in the output text file. This was researched and solved by using the argument newline = ‘\n’

with open(output_path, 'w', newline="\n") as csvfile:

PyPoll

PyPoll was much more challenging with more than 3.5M lines of data. The solution hinged around finding a way to create a unique list of candidates and then build the rest of the data on that. Several solutions were found but the most readable was:

		if row[2] not in candidate_list:
                candidate_list.append(row[2])

This code cycles through each line in the data at the candidate position (row[2]) and compares it with the list of candidates that the code is building. If it’s not in the list it adds that candidate and creates a new entry in the votes tally list by appending a zero. 

       votes_tally.append(0)

Conveniently, the votes could be tallied within the same loop with:

		for i, candidate in enumerate(candidate_list):
                if candidate == row[2]:
                    a = int(votes_tally[i])
                    votes_tally[i] = a + 1
                else:
                    pass 

This code is the engine of the solution for PyPoll.  One other call out was identifying the winner by finding the index of the maximum of the votes tally and using it for the candidate game.

       Winner = candidate_list[votes_tally.index(max(votes_tally))



PyBoss








       
       
       
       
       
       
       
       
       
