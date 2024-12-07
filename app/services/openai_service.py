import os

from dotenv import load_dotenv
from openai import OpenAI

# 환경 변수 로드
load_dotenv()

# OpenAI 클라이언트 초기화
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_response(prompt: str) -> dict:
    """
    OpenAI GPT 모델 호출하여 응답 생성.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}]
        )
        message_content = response.choices[0].message.content.strip()
        return {"prompt": prompt, "response": message_content}
    except Exception as e:
        return {"error": str(e)}
