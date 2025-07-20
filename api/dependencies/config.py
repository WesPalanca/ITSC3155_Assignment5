from dotenv import load_dotenv
import os
load_dotenv()

class conf:
    host = "localhost"
    database = "sandwich_maker_api"
    port = 3306
    user = "root"
    password = os.getenv("SQL_PASSWORD")