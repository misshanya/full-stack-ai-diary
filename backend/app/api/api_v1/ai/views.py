from fastapi import APIRouter

from gigachat import GigaChat

from .schemas import ChatMessage
from .helpers import send_message

router = APIRouter(
    tags=['AI'],
    prefix='/chat'
)


@router.post('/')
async def chat_msg(msg: ChatMessage):
    return send_message(
        user_prompt=msg.message,
    )
