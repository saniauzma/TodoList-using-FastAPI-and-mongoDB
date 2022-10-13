from model import Todo

#mongodb driver
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
database = client.TodoList
collection = database.todo


async def fetch_one_todo(title):
    doc = await collection.find_one({"title":title})
    return doc


async def fetch_all_todos():
    todos = []
    cursor = collection.find({})
    async for doc in cursor:
        todos.append(Todo(**doc))
    return todos

async def create_todo(todo):
    doc = todo
    result = await collection.insert_one(doc)
    return doc

async def update_todo(title, desc):
    await collection.update_one({"title":title}, {"$set":{"description":desc}})
    doc = await collection.find_one({"title":title})
    return doc

async def remove_todo(title):
    await collection.delete_one({"title":title})
    return True 