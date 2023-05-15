# mini-search-engine
A python code was computed for indexing articles and searching queries in the given articles, the search task was performed by computing the relevance score for that query in the articles. 
The text was preprocessed by eliminating stop words, punctuations and then lemmatization and stemming techniques were performed for better understanding of text and increasing the efficiency of search engine while searching.


# Python scripts and their results:

- assign2Main.py : This script act as user interface and calls indexing and searching python files to get the text articles with their relevance score for the search word entered by user.
- indexing.py: This script takes the folder of files and open only text filed one by one. For each text file it preprocess the text and then using the frequenct of each searhed word with the words in text, it gives the index to the document.  
- searching.py: This script preprocess the query text and splits it into individual terms. Then it finds the documents containing the terms and rank them by relevance score. 
