# -*- coding: utf-8 -*-
"""


imported:
    indexing program,math lib, operator
Input:
   here input is query that is taken from main function
        
Computions:
     This functions preprocess the query text and splits it into individual terms. 
    Then find the documents containing the terms and rank them by relevance score. 
    
    define  a dictionary docScores of doc:score to return 
    cleanQuery= preprocess(query) 
    for each query term: 
        find its entry in index, 
        get the dictionary docFreq containing doc:freq as key:val from the index
        calculate the Number of documents nbdocs containing the term, (len of dict) 
        for each doc in dic: 
            calculate the weight wtdoc as freq*log(N/n) 
            where N is the total number of documents in the coll 
            n is the number of documents containing the term  
            if doc does not exist as key in docScores: 
                add it as key with its wtdoc as value 
            else:
                increment the score with wtdoc 
    
    sort docScores by values, then show the doc id and the score. 
     
    output: 
        dictionary of doc: score 
    
    

"""


    
import indexing
import math 
import operator
    

"""
 
   
"""
 
def search(query,num_doc):   
    docScores = {}
    docScores2 = {}
    listofdocscores=[]
    score = 0
    queryTerms=[]
    cleanQuery= indexing.preprocess(query)#cleaned the query and assigned it to cleanQuery
    queryTerms = cleanQuery.split(" ")#splitted the cleanQuery and made list(queryTerms) of terms
    N = num_doc# getting the no of text doc using function of indexing
    #loop through the list queryTerms 
    for qterm in queryTerms:
        dictDocFreq = indexing.index[qterm]#add the value of query term into dic dictDocFreq
        n = len(dictDocFreq)#len of dic 
        for doc, freq in dictDocFreq.items():#loop through items of dic dicDocFreq
            #calculated relevant score for query in doc wrt freq of q term in doc
            score = float(int(freq) * math.log(N/n))
            if doc not in docScores.keys():
                docScores[doc]=score#add the docid of query as key and relevant score of qterm as value
            else:
                docScores[doc] += score
            # incremented the score if doc in keys already
    docScores2 = dict(sorted(docScores.items(),key = operator.itemgetter(1),reverse = True))
    listofdocscores.append(docScores2)
    
    return listofdocscores
# returns the list of dic of query term as key and docid:score as value














