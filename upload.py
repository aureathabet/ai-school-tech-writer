from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_pinecone import PineconeVectorStore
from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain_community.document_loaders import DirectoryLoader
from tqdm import tqdm
from constants import *
from dotenv import load_dotenv

load_dotenv()

loader = DirectoryLoader('./standards', glob="**/*.pdf", loader_cls=PyPDFLoader, show_progress=True, use_multithreading=True)
raw_docs = loader.load()

# Split documents into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=3072, chunk_overlap=100)
documents = text_splitter.split_documents(raw_docs)
total_documents = len(documents)
print(f"Going to add {total_documents} to Pinecone")

# Choose the embedding model and vector store
embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)
vector_store = PineconeVectorStore(index_name=PINECONE_INDEX, embedding=embeddings)
for i in tqdm(range(len(documents)), desc="Uploading documents"):
    vector_store.add_documents([documents[i]])
print("Loading to vectorstore done")