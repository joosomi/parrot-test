import os

from openai import OpenAI

from app.utils.env_loader import load_env  # 유틸리티 함수 임포트

# OpenAI 클라이언트 초기화
client = OpenAI(api_key=load_env())  # 환경 변수 로드를 유틸리티 함수로 처리


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
