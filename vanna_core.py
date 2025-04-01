import os

from vanna.chromadb import ChromaDB_VectorStore
from vanna.google import GoogleGeminiChat
import base64
import pandas as pd
from dotenv import load_dotenv
load_dotenv()

class MyVanna(ChromaDB_VectorStore, GoogleGeminiChat):
    def __init__(self, config=None):
        ChromaDB_VectorStore.__init__(self, config=config)
        GoogleGeminiChat.__init__(self, config={'api_key': os.getenv("API_KEY"), 'model': os.getenv("model")})

    def setup_database(self, host, dbname, user, password, port=3306):
        self.connect_to_mysql(host=host, dbname=dbname, user=user, password=password, port=port)
        df_information_schema = self.run_sql("SELECT * FROM INFORMATION_SCHEMA.COLUMNS")

        plan = self.get_training_plan_generic(df_information_schema)
        self.train(plan=plan)

    def ask_question(self, question):
        try:
            result = self.ask(question=question)
            if hasattr(result, 'figure'):
                if result.figure is not None:
                    img_bytes = result.figure.to_image(format="png", scale=2)
                    img_base64 = base64.b64encode(img_bytes).decode("utf-8")
                    return type('obj', (object,), {'llm_response': result.llm_response, 'image': img_base64})
            return type('obj', (object,), {'llm_response': result.llm_response, 'image': None})
        except Exception as e:
            return type('obj', (object,), {'llm_response': f"Error: {e}", 'image': None})

def initialize_vanna(host, dbname, user, password, port=3306):
    vn = MyVanna()
    vn.setup_database(host, dbname, user, password, port)
    return vn