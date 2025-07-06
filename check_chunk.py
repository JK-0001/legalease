# check_chunks_for_assessee.py
from utils import get_chroma_client, get_or_create_collection
from langchain_openai import OpenAIEmbeddings
import dotenv

dotenv.load_dotenv()

client = get_chroma_client("./chroma_db")
embedding_model = OpenAIEmbeddings()
collection = get_or_create_collection(client, "docs", embedding_function=embedding_model)

results = collection.get(include=["documents", "metadatas"])
docs = results["documents"]
metas = results["metadatas"]


for i, doc in enumerate(docs):
    if "assessee" in doc.lower():
        print(f"\n--- Found in Chunk {i} ---")
        print(doc[:1000])
        print(metas[i])