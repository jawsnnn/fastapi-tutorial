'''
Application file
'''

from fastapi import FastAPI

application = FastAPI()

@application.get("/")
def get_root(message):
    return {
        "message": f"This is a goddamn message: {message}"
    }