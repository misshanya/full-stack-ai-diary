from fastapi import APIRouter

from gigachat import GigaChat
from pydantic import BaseModel

from core.config import settings

TOKEN_SBER = settings.ai.token_sber


router = APIRouter(
    tags=['AI'],
    prefix='/chat'
)


class ChatMessage(BaseModel):
    message: str


def send_message(user_prompt):
    with GigaChat(credentials=TOKEN_SBER, verify_ssl_certs=False) as giga:
        response = giga.chat(user_prompt)
        return ChatMessage(
            message=response.choices[0].message.content,
        )


@router.post('/')
async def chat_msg(msg: ChatMessage):
    return send_message(
        user_prompt=msg.message,
    )
