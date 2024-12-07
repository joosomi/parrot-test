import os

from dotenv import load_dotenv


def load_env():
    """
    환경 변수를 로드합니다.
    """
    load_dotenv()
    return os.getenv("OPENAI_API_KEY")
