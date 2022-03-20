import re 
import pandas as pd 
import numpy as np 
import fuzzywuzzy


"""
DOCUMENTATION 

This script aims to automize repetitive text processing jobs that might be useful in Machine Learning processes.  
    
"""


class TestringtProcessor: 
    
    
    def getNumbersfromString(self, string, flag = False):
        
        """[Find all the number from string with regestring]

        Inputs : 
            string : [String] 
            flag : [Boolean] to select return all numbers in list or select first number as integer 
                    True : Returns all the integers in the string 
                    False : Returns first consecutive integer
            
        Returns:
            [List or Integer]: [According to flag]
            
        Usage: 
        a = t.getNumbersfromString("abc123d") --> 123 
        
        
            
        """
        if flag : 
            if type(string) == str : 
                number = re.findall('[0-9]+', string)
                return number 
            else :
                # This for deal with missing values None, NaN , etc
                return string 
        else : 
            if type(string) == str : 
                number = re.findall('[0-9]+', string)
                return int(number[0])

            else : 
                # This for deal with missing values None, NaN , etc
                return string 

    def replace_matches_in_column(self, df, column, string_to_match, min_ratio = 53):
        
        """[Helps to match the words looks similar]
        
        Inputs : 

            df : [pandas.DataFrame]
            column : Column that you want to work with 
            string_to_match : [String]
            min_ratio : [Integer] How much similarity is enough for you 
            
    
        Usage: 
        replace_matches_in_column(df = df , column = 'Country', string_to_match = 'australia')
        
         * australia
         * australie
         * australiEs 
         
         To match mispelled word in the dataframe
        
            
        """
    
        # get a list of unique strings 
        strings = df[column].unique()
        
        # get the top 10 closest matcher in our input string 
        matches = fuzzywuzzy.process.extract(string_to_match, strings , limit = 10 ,
                                             scorer = fuzzywuzzy.fuzz.token_sort_ratio)

        # only get matches with a ratio > min_ratio 
        close_matches = [matches[0] for matches in matches if matches[1] >= min_ratio]

        # get the rows of all the close matches in our dataframe 
        rows_with_matches = df[column].isin(close_matches)
        
        # replace all rows with close matches with the input matches 
        df.loc[rows_with_matches, column] = string_to_match


    





#### TEST #### 
# t = TestringtProcessor()
# a = t.getNumbersfromString("abc123d")
# print(a)
#### TEST ####








