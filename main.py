import os

from dotenv import load_dotenv
from fastapi import FastAPI
from openai import OpenAI

# 환경 변수 로드
load_dotenv()

# OpenAI 클라이언트 설정
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")  # 환경 변수에서 API 키 가져오기
)

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to OpenAI Prompt Tester"}


# 프롬프트 생성 엔드포인트
@app.post(
    "/generate/",
    summary="프롬프트 기반 응답 생성",
    description="사용자가 입력한 프롬프트를 바탕으로 OpenAI GPT 모델에서 응답을 생성합니다.",
    tags=["Chat Generation"]
)
def generate_prompt(prompt: str):
    """
    이 함수는 프롬프트를 받아 GPT 모델을 호출하여 응답을 생성합니다.

    Args:
        prompt (str): 사용자가 입력한 텍스트

    Returns:
        dict: 생성된 응답과 입력된 프롬프트
    """
    try:
        # OpenAI API 호출
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # 사용할 모델 설정
            messages=[{"role": "user", "content": prompt}],  # 사용자 메시지 전달
        )
        # GPT 모델이 생성한 메시지 내용 가져오기
        message_content = response.choices[0].message.content
        return {"prompt": prompt, "response": message_content.strip()}
    except Exception as e:
        # 예외 처리
        return {"error": str(e)}
