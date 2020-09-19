import yaml 
class Summarizer_doc:
    """
    Module for summarization

    """
    def __init__(self):
        with open('../config/config.yaml','r') as fl:
            self.configs = yaml.load(fl) 
            
    def load_docs(self):
        """
        Read articles from path
        """
        pass

    def load_config(self):
        pass

    def sent_splitter(self):
        pass

    def first_sent_extractor(self):
        pass

    def first_num_words(self):
        pass

    def find_top3_sent(self):
        pass

    def sent_combinator(self):
        pass

summarize_obj = Summarizer_doc()
summarize_obj.load_config()