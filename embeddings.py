from dotenv import load_dotenv
load_dotenv()

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_postgres.vectorstores import PGVector
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# Load and split
raw_documents = TextLoader('./test.txt').load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
documents = text_splitter.split_documents(raw_documents)

print(f"✅ Number of chunks: {len(documents)}")
for i, doc in enumerate(documents):
    print(f"Chunk {i+1}: {doc.page_content[:60]}...")

# Initialize embeddings
embeddings_model = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")

connection = 'postgresql+psycopg://langchain:langchain@localhost:6024/langchain'
COLLECTION_NAME = "my_docs"  # Define once, use everywhere

# Clear existing data in the target collection
db = PGVector(
    embeddings=embeddings_model,
    collection_name=COLLECTION_NAME,
    connection=connection,
    use_jsonb=True,
)
db.delete_collection()
print("✅ Cleared collection")

# Insert fresh into the SAME collection
db = PGVector.from_documents(
    documents,
    embeddings_model,
    connection=connection,
    collection_name=COLLECTION_NAME,  # 👈 MUST match above
)


print(f"✅ Inserted {len(documents)} documents")

# Search
response = db.similarity_search("query", k=4)
print(f"\n🔍 Found {len(response)} results:")
for i, doc in enumerate(response):
    print(f"\nResult {i+1} (ID: {doc.id}):")
    print(doc.page_content)