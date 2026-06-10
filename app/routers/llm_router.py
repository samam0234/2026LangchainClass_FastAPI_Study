# fastapi_basic/app/router/llm_router.py
# 역할 : HTTP 요청(클라이언트가 보낸 request(클라이언트가 보낸 모든 요청정보(데이터 포함)))을 받아, Service단을 호출하고,
#        Client에게 응답을 반환한다.

from fastapi import APIRouter       # Router를 분리할 때 필요
import json

# 요청/응답시 처리되는 데이터 검증용
from app.schemas.llm import SummarizeRequest, SummarizResponse, SentimentReviewRequest, SentimentReviewResponse

# 호출할 서비스단
from app.services.llm_service import summarize

# prefix : 모든 경로 앞에 /llm이 붙는다
# 예 : /summarize =>    /llm/summarize
llm_router = APIRouter(prefix="/llm", tags=["llm"])    # router를 분리 할 때 사용하는 객체

@llm_router.post("/summarize", response_model=SummarizResponse, status_code=201, summary="텍스트 요약(LLM)")
async def summarize_text(request:SummarizeRequest) : 
    """
        텍스트를 GPT-4o로 요약합니다.
    """
    result = await summarize(request.text, request.max_length, request.language)
    return SummarizResponse(
        original_length=len(request.text),
        summary=result
    )