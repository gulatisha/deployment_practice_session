import re

class Preprocessor_doc:
    """ 
    Module for preprocessing
    """
    def remove_special_char(self,text):
        """ 
        Remove special characters
        Input 
            text: string
        Output 
            modified_text : string
        """
        modified_text = re.sub(',|;|#,$','',text)
        return modified_text

    def convert_to_lower(self,text):
        return text.lower()

        
