from fastapi import FastAPI
from routes import lists, contacts, tags

app = FastAPI()

app.include_router(lists.router)
app.include_router(contacts.router)
app.include_router(tags.router)