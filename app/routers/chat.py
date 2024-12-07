from fastapi import APIRouter

from app.models.request_models import PromptRequest
from app.services.openai_service import generate_response

router = APIRouter(prefix="/generate", tags=["Chat Generation"])


@router.post("/", summary="프롬프트 기반 응답 생성")
def generate_prompt(request: PromptRequest):
    """
    사용자의 프롬프트를 OpenAI 모델에 전달하여 응답 생성.
    """
    return generate_response(request.prompt)
