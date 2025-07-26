from qdrant_client import QdrantClient, models
import numpy as np

# 1) Connect
client = QdrantClient("localhost", port=6333)

# 2) (Re)create collection with 4‑D vectors
client.recreate_collection(
    collection_name="crispcore",
    vectors_config=models.VectorParams(size=4, distance=models.Distance.COSINE),
)

# 3) Upsert one point
vec = np.array([0.1, 0.2, 0.3, 0.4]).tolist()
client.upsert(
    "crispcore",
    models.Batch(
        ids=[1],
        vectors=[vec],
        payloads=[{"text": "hello world"}],
    ),
)

# 4) Search the same vector
hits = client.search("crispcore", query_vector=vec, limit=1)
print("Top hit:", hits[0].payload["text"], "score", hits[0].score)