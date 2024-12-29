import pandas as pd
import chromadb
import uuid

class Portfolio:
    def __init__(self, file_path="resources/my_portfolio.csv"):
        self.file_path = file_path
        self.data = pd.read_csv(file_path)
        self.chroma_client = chromadb.PersistentClient('vectorstore')
        self.collection = self.chroma_client.get_or_create_collection(name="portfolio")
        self.load_portfolio()

    def load_portfolio(self):
        if not self.collection.count():
            for _, row in self.data.iterrows():
                self.collection.add(documents=row["Techstack"],
                               metadatas={"links": row["Links"]},
                               ids=[str(uuid.uuid4())])

    def query_links(self, skills):
        return self.collection.query(query_texts=skills, n_results=2).get('metadatas', [])

    def get_data(self):
        return self.data

    def add_data(self, techstacks, link):
        new_entry = pd.DataFrame({"Techstack": [techstacks], "Links": [link]})
        self.data = pd.concat([self.data, new_entry], ignore_index=True)
        print(self.data)