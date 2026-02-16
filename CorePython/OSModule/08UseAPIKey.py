#pip install python-dotenv
import os
from dotenv import load_dotenv

load_dotenv()
#collect sensitive information from .env file
apikey=os.getenv("API_KEY")
uid=os.getenv("UserID")
ps=os.getenv("Password")

# not to be displayed
print(apikey)
print(uid)
print(ps)