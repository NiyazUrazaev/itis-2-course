from typing import Optional

from fastapi import FastAPI
from fastapi import Body
import uvicorn


app = FastAPI()


@app.get('/')
async def hello(name: str, age: int):
    """Hello world method.

    :param name: Name of user.
    :param age: Age of user.
    :return: Hello world message.
    """
    return {'message': f'Hello {name}! U are {age} years old.'}


@app.post('/')
async def post_message(name: str = Body()):
    return {'message': f'Hello {name}!'}


if __name__ == '__main__':
    uvicorn.run(app)

