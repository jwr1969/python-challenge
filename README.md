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

PyBoss, reading, converting and then rewriting employee date to a new file was also relatively straight forward. My solution read the data by column converted it and appended the results to a new list which was then zipped and written to an output txt file. The date conversion was the trickiest piece, and for that I defined a function using split to separate the old date into year, month and day and then rebuild it in the new format.

		def new_date(date):
    			year = date.split("-")[0]
    			month = date.split("-")[1]
    			day = date.split("-")[2]
    			new_date_string = str(month + "/" + day  + "/" + year)
    			return new_date_string

The function was called with:

		date_reformat.append(new_date(row[2]))

This made the code much more readable and easier to work with.  The suggested state abbreviation list was copied directly into the code and created as a list.

PyParagraph

PyParagrah read in a paragraph and then analysed it for approximate word count, approximate sentence count, approximate letter count (per word, average sentence length (in words). This was a tougher assignment and using Jupyter Notebook to experiment with different options I chose to read the file as “.” delimited file to obtain sentences as items in my list removing the last entry which was “ “. Using the re module with method split I then ran through and counted words by sentence and characters by sentence and appended them to lists.

	for x in range(len(sentences)):
        # Count the number of words per sentence and add to new list
        sentence_words.append(len(re.split(" ",sentences[x])))
        # Count the number of characters per sentence and add to new list
        sentences_characters.append(len(sentences[x]))

My results

Paragraph Analysis  Resources\paragraph_3.txt
---------------------------------------------
Approximate Word Count: 124
Approximate Sentence Count: 5
Average Letter Count: 5.4
Average Sentence Length: 24.8

When run with the “Bruce Wayne” paragraph which I called paragraph_3 I get slightly different results because my code adds an extra word after a full stop (+ 4 words) presumable as the result of a double space and more characters per word (5.4 versus 4.6) presumably as a result of counting spaces between words. I did not use the suggested re.split("(?<=[.!?]) +", paragraph)- as I did not fully understand it, although I did look it up. I’m sure my solution could be refined with different arguments in re.split.

John Russell
10th April, 2021







       
       
       
       
       
       
       
       
       
