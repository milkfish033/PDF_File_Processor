from llama_index.core import (SimpleDirectoryReader, download_loader, VectorStoreIndex)
from llama_index.readers.file import PDFReader
import doubao
from multiprocessing import Process, freeze_support, set_start_method

def generate(filepaths, command) -> str:
  
    #otherwise it there will multi-processing issues
    freeze_support()
  
    reader = SimpleDirectoryReader(input_files=filepaths,required_exts=[".pdf"],num_files_limit=1)
  
    document = reader.load_data(num_workers = 1)
  
    #specify the number of files you want to load simultaneously
    #*:note it couldn't be bigger than the number of your CPU
  
    #generate relative answer 
    result = doubao.QA(document[0].get_text(), command)
  
    return result




