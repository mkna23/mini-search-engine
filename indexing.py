# -*- coding: utf-8 -*-

"""

Input:
   here the pathTodir that is argument of runIndexing and getNumberofDocuments comes as
   input for the program from main function
   
Computions:
    
    The function getNumberofDocument takes the path to dir with folder of files
    it return total number of text documents in folder
    
    
    The runindexing function also takes path to folders and open text file one by one and 
    apply other functions on the text in file to create index for file.
    
    readfile content function reads the content of file and takes opened file as argument
    
    preprocess function takes the text, removes puntuations, tokenize the text, then it stems the tokenized text
    and remove stopwords using stopwords library.
    
    appendTermDocFreq function takes the clean text returned by preprocess function 
    then in this function the cleantext is splitted and then the words are added to listofwords list
    and then using for loop we counted the frequency of words and appended the file with word, doc id and freq in doc
    by writing lines
    
    genIndex function reads the file termDocFreqFile and add the word as key of dic index and the docid:freq as value
    this function fills the index.
    
Output:
     index dic is filled with the words of text files as key and their docid: freq as value in dic
     index dic filling i output

"""

 

# global variable
index= {}

import os

def getNumberofDocument(pathToDir):
    """
    Description:
        This function takes the path to folders of files and retuens the no of text files in that folder
        
    Input:
        path to collection
    
    Algo:
        creating list of files in folder 
        and incrementing a number if it is text file
     output:
         total no of text files.
    """
    lyst = os.listdir(pathToDir)#list of files in folder
    noOf_document = 0
    #looping through list and incrementing noOf_documents if it is txt file
    for f in lyst:
       if ".txt" in f:
          noOf_document += 1
    return noOf_document-1 # as the file also contains termdocFreq file so returned one doc less than it
 
def runIndexing(pathToDir): 
    """ 
    Description: 
        This function takes the path to the folder of files to be indexed 
        considers only the files with .txt extension, read the content of the files
        one by one and generate an index from terms to documents for the whole collection. 
        call preprocess function to get a clean text. 
    
    Input: 
        path to the collection 
    output: 
        append the global variable index
    
    Algo: for each file in folder: 
        read the content of the file in text
        call preprocess(text)
        call appendTermDocFreq(cleanText, termDocFreqFile)
        call genIndex(termDocFreqFile)
        call genInvertedIndex(dictFileName, postingsFileName)
    """
   
    lyst = os.listdir(pathToDir)
    #looping through list of files in pathToDir and operating function only on txt file
    for f in lyst:
       if ".txt" in f:
          ftext = open(f,'r')#opened the text file
          #implementing all the functions on text of file
          text = readFileContent(ftext)#functions reads the text file
          docid = f.replace('.txt'," ")
          appendTermDocFreq(preprocess(text),docid,"termDocFreqFile")
          genIndex("termDocFreqFile")
          ftext.close()#closed the file
        
        
def readFileContent(fileName): 
    """ returns the content of the file as a string. 
    """
    text = fileName.read()
    return "".join(map(str,text))#returns the text in form of string
        
        
    
def preprocess(text):
    """
    Description: 
        This function takes text as argument, removes all punctuation and stop words
        then apply stemming 
    input: 
        text 
    output: 
        clean text
    """
    Text=[]
    newtext = " "
    tokenize_Text =[]
    from nltk.tokenize import word_tokenize
    #remove puntuations by importing punctuations list from string lib
    #after removing punc add the words to newtText string
    import string
    for word in text:
        if word not in string.punctuation:
           newtext = newtext + word
    #creating a list of tokenized text (tokenize_Text)
    tokenize_Text = word_tokenize(newtext)
    #stemming the words of tokenized list and appending them to Text list
    from nltk.stem import PorterStemmer
    ps = PorterStemmer()
    from nltk.corpus import stopwords
    #importing stopwords list and removing them from tokenized list by looping through list
    stop_words = set(stopwords.words('english'))
    for word in tokenize_Text:
        if word  not in stop_words:
           Text.append(ps.stem(word))
           
    return " ".join(map(str,Text))#returing string of cleanText(Text)
    

    
def appendTermDocFreq(cleanText,docid,termDocFreqFile): 
    """ 
    Description: 
        this functions takes a clean text as argument,  and appends TermDocFreqFile 
        with the list of term, the  document in which they appear and their frequencies. 
    Input: 
        cleanText
    output: 
        termDocFreqFile format: 3 columns, values seperated with space
            Term doc# freq
            recipe 1 5
            sweet 1 1
            sugar 1 2
            salt 1 2
            recipe 2 3
            salad 2 1
            salt 2 2
            tomato 2 2
    """ 
    listofwords=[]
    freq ={}
    #splitted the clean text that it got from preprocess function and assigned to newtext
    newText = cleanText.strip().split()
    #loop through the newText to add words into listofwords
    #appending the words only once into the list
    for word in newText:
       if word not in listofwords:
           listofwords.append(word)
    #appending the termdocfreqfile by opening it
    f = open('termDocFreqFile.txt','a')
    # looping through listofword
    for words in listofwords:
        freq[words]=cleanText.count(words)#in dic freq adding word along with its count in text
        #writing lines into file 
        f.writelines(words+" "+str(docid)+""+str(freq[words])+"\n")
    f.close()
    #closing file
    


def genIndex(termDocFreqFile): 
    """
    description: 
        this function reads termDocFreqFile line by line and append the global index  
        that go from terms as keys to list of documents that contain them with their frequencies as val. 
        Appending the index works as follows: 
            - for line in termDocFreqFile, 
                - if the term does not exist in index, 
                    add the term as key, the value will be a dictionary containg docid:freq as key:val in index
                - if the term already exists in index, append the val (which is a dictionary) with docid:freq 
                
    input: 
        termDocFreqFile
    output: 
        fill in the index structure global variable defined in top of the module.    
    """
    val={}
    # opening the file and reading line by line
    f = open("termDocFreqFile.txt",'r')
    for line in f:
        #splitting the terms in single line 
        line = line.strip().split(" ")
        #applying condition adding the value of index[word] into val dic if it already exist
        if line[0] in index.keys():
            val = index[line[0]]
            val[line[1]]=line[2]#then adding the docid and freq as key and value to val dic
            index[line[0]]=val#then val dic is value of index key that is term\ word in line (1st element of line)
        else:
            val2={}
            val2[line[1]]=line[2]#adding the docid(line[1]) and freq (line[2])as key and value to val2 dic
            index[line[0]]=val2#addimg val2 dic as value to index dic key word of line(line[0])
            
            # this fills the index dic
            
    


 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    