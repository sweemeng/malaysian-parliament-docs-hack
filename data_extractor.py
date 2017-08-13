import os.path
import PyPDF2


def document_walker(path=""):
    for item in os.listdir(path):
        doc_path = os.path.join(path, item)
        if os.path.isdir(doc_path):
            for doc in os.listdir(doc_path):
                if "pdf" in doc:
                    yield os.path.join(doc_path, doc)

def extract_text(path=""):
    for item in document_walker(path=path):
        f = open(item, "rb")
        reader = PyPDF2.PdfFileReader(f)
        text_list = []
        for n in range(reader.numPages):
            page = reader.getPage(n)
            text_list.append(page.extractText())
        yield " ".join(text_list)
            
def extract_text_single(file_name):
    f = open(file_name, "rb")
    reader = PyPDF2.PdfFileReader(f)
    text_list = []
    for n in range(reader.numPages):
        page = reader.getPage(n)
        text_list.append(page.extractText())
    return " ".join(text_list)

def stop_words(stopword_file="indonesian_stopword.txt"):
    stopword_file = open(stopword_file)
    stopwords = stopword_file.readlines()
    stopwords = [stopword[:-1] for stopword in stopwords]
    return stopwords
