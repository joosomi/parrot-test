from pydantic import BaseModel


class PromptRequest(BaseModel):
    prompt: str  # 사용자 입력 프롬프트
