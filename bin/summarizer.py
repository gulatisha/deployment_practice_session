import yaml 
class Summarizer_doc:
    """
    Module for summarization

    """
    def __init__(self):
        with open('../config/config.yaml','r') as fl:
            self.configs = yaml.load(fl) 

    def load_docs(self,file_path):
        """
        Read articles from path
        """
        with open(file_path,'r') as fl:
            text = fl.read()
        return text

    def sent_splitter(self,text):
        """
        Split text into array of sentences
        Input
            text: string
        Output
            sentences : list of strings
        """

        sentences = text.split('.')
        return sentences

    def group_sentences(self,sentences):
        """

        """
        first_sent , rest_sent = sentences[0], sentences[1:]
        return first_sent,rest_sent

    def find_sent_length(self,text):
        return text.split()

    def find_sent_length_array(self,sentences):
        return [self.find_sent_length(sent) for sent in sentences]
        pass

    def find_top_sentence(self,sent_lengths,sentences):
        sorted_idx = np.argsort(sent_lengths)
        top3_idx = sortedIdx[-3:]
        top_3_sentences = [sentences[i] for i in top3_idx]
        return top_3_sentences
    
    def find_summary(self):
        file_path = self.config['data_path']['train_data']
        text = self.load_docs(file_path)
        sentences = self.sent_splitter(text)
        first_sent,rest_sent = self.group_sentences(sentences)
        sent_lengths = self.find_sent_length_array(rest_sent)
        top_3_sentences = self.find_top_sentence(sent_lengths,rest_sent)
        all_sentences = [first_sent] + [top_3_sentences]
        summary = ''.join(all_sentences)
        

summarize_obj = Summarizer_doc()
summarize_obj.load_config()