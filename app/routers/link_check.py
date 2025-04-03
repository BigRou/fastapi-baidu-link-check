from fastapi import APIRouter, HTTPException
from typing import Optional, List
from pydantic import BaseModel

router = APIRouter(
    prefix="/api",
    tags=["link_check"]
)

class LinkRequest(BaseModel):
    link: str

class BatchLinkRequest(BaseModel):
    links: List[str]

@router.post("/check-link")
async def check_link(link_request: LinkRequest):
    """
    检测单个百度网盘链接有效性
    """
    from app.services.baidu_link_service import BaiduLinkService
    
    result = BaiduLinkService.check_link_validity(link_request.link)
    
    if result is None:
        raise HTTPException(status_code=400, detail="无效的链接格式")
    elif result is False:
        return {"valid": False, "message": "链接无效"}
    return {"valid": True, "message": "链接有效", "link": link_request.link}

@router.post("/batch-check")
async def batch_check_links(batch_request: BatchLinkRequest):
    """
    批量检测百度网盘链接有效性
    """
    from app.services.baidu_link_service import BaiduLinkService
    
    results = []
    for link in batch_request.links:
        result = BaiduLinkService.check_link_validity(link)
        if result is None:
            results.append({"link": link, "valid": None, "message": "检测错误"})
        elif result is False:
            results.append({"link": link, "valid": False, "message": "链接无效"})
        else:
            results.append({"link": link, "valid": True, "message": "链接有效"})
    
    return {"results": results}