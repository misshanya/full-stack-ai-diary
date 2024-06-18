from gigachat import GigaChat

from core.config import settings
from .schemas import ChatMessage

TOKEN_SBER = settings.ai.token_sber


def send_message(user_prompt):
    with GigaChat(credentials=TOKEN_SBER, verify_ssl_certs=False) as giga:
        response = giga.chat(user_prompt)
        return ChatMessage(
            message=response.choices[0].message.content,
        )
