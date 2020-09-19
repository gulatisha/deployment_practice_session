import re
import yaml

class Preprocessor_doc:
    """ 
    Module for preprocessing
    """
    def __init__(self):
        self.x = 2

    def remove_special_char(self):
        """ 
        Remove special characters
        Input 
            text: string
        Output 
            modified_text : string
        """
        pass

    def tokenize_article(self):
        """
        Split sentences into tokens
        Input
            modified_text : string
        Output 
            tokenized_text : string
        """
        pass

    def stopowords_removal(self):
        """
        Remove stopwords 
        Input 
            tokenized_text : string
        Output
            cleaned_text : string
        """
        pass
