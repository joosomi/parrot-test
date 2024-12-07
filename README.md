# 🦜 Parrot OpenAI Prompt Tester

OpenAI GPT 모델을 활용하여 사용자 프롬프트를 처리하고 응답을 생성하는 FastAPI 기반 프로젝트

## 📌 프로젝트 개요

- **현재 상태**: 개발 초기 단계 (2024.12.07 ~ 진행 중)  
- **목적**: 
  - OpenAI API를 활용하여 프롬프트 기반 응답 생성 기능을 테스트
  - 다양한 프롬프트 엔지니어링 실험
  - 여러 GPT 모델(`gpt-3.5-turbo`, `gpt-4` 등)의 응답 비교


## 📚 설치 및 실행
1. [Poetry 공식 문서](https://python-poetry.org/docs/#installing-with-the-official-installer)를 참고하여 Poetry를 설치합니다.
  
2. Poetry를 사용하여 프로젝트의 의존성을 설치
  ```
  poetry install
  ```

3. 환경 변수 설정
샘플 파일 .env.sample을 참고하여 OPEN_API_KEY를 입력해주세요.
  ```
  OPENAI_API_KEY=your_openai_api_key
  ```

4. Poetry의 가상환경을 활성화한 후 FastAPI 서버를 실행합니다:
  ```
  poetry shell
  uvicorn main:app --reload
  ```

5. Swagger 문서 확인
FastAPI가 제공하는 Swagger UI를 통해 API 문서를 확인하고 테스트할 수 있습니다. <br>
[[Swagger UI](http://127.0.0.1:8000/docs)]: http://127.0.0.1:8000/docs


## 🚀 주요 기능

### 1. 현재 구현된 기능
#### 프롬프트 기반 응답 생성 
**`POST /generate`** : 사용자가 입력한 텍스트를 OpenAI GPT 모델에 전달하여 응답을 생성합니다.
  <br>
  - Request Body (JSON)
  ```json
  {
    "prompt": "안녕!"
  }
  ```
  - Response Body (JSON)
  ```
  {
    "prompt": "안녕!",
    "response": "안녕하세요! 도와드릴게 있나요? 😊"
  }
  ```

![image](https://github.com/user-attachments/assets/8080f654-38c2-4784-9d48-888642c43526)



## 🛠️ 개발 계획
- 다양한 모델 테스트
- 프롬프트 엔지니어링 테스트: 역할 설정, 컨텍스트 추가 등
