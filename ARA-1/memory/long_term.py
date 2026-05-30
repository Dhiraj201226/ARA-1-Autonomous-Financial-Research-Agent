import chromadb

class LongTermMemory:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="./chroma_db"
        )

        self.collection = (
            self.client.get_or_create_collection(
                "research_memory"
            )
        )

    def store(
        self,
        doc_id,
        text,
        embedding
    ):

        self.collection.add(
            ids=[doc_id],

            documents=[text],

            embeddings=[
                embedding.tolist()
            ]
        )

    def search(
        self,
        embedding,
        n_results= 1
    ):

        return self.collection.query(
            query_embeddings=[
                embedding.tolist()
            ],

            n_results=n_results
        )