import requests
from typing import Optional

def make_request(url: str, headers: Optional[dict] = None, timeout: int = 10) -> Optional[str]:
    """
    发送HTTP请求并返回响应内容
    
    参数:
        url: 请求URL
        headers: 请求头
        timeout: 超时时间(秒)
    
    返回:
        响应文本内容，如果请求失败则返回None
    """
    try:
        response = requests.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()
        return response.text
    except Exception:
        return None