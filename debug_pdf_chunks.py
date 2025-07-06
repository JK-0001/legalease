# debug_query.py
from langchain_openai import OpenAIEmbeddings
from utils import get_chroma_client, get_or_create_collection, format_results_as_context, query_collection
import dotenv

dotenv.load_dotenv()

embedding_model = OpenAIEmbeddings()
client = get_chroma_client("./chroma_db")
collection = get_or_create_collection(client, "docs", embedding_function=embedding_model)

query_results = query_collection(collection, "assessee definition under income tax act", n_results=10)
print(format_results_as_context(query_results))
