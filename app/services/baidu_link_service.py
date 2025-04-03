import re
import requests
from bs4 import BeautifulSoup
from typing import Optional

class BaiduLinkService:
    BAIDU_PAN_PATTERN = re.compile(r'^https?:\/\/pan\.baidu\.com\/s\/[a-zA-Z0-9_-]+(\?pwd=[a-zA-Z0-9]+)?(\&.*)?$')
    
    @staticmethod
    def is_valid_baidu_link(link: str) -> bool:
        """
        验证是否为有效的百度网盘链接格式
        """
        return bool(BaiduLinkService.BAIDU_PAN_PATTERN.match(link))
    
    @staticmethod
    def check_link_validity(link: str) -> Optional[bool]:
        """
        检测单个百度网盘链接有效性
        返回:
            True - 链接有效
            False - 链接无效
            None - 检测过程中出现错误
        """
            
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            
            response = requests.get(link, headers=headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.title.string if soup.title else ""
            
            if "百度网盘-链接不存在" in title:
                return False
            return True
            
        except Exception:
            return None
            
    @staticmethod
    def batch_check_links(links: list[str]) -> list[dict]:
        """
        批量检测百度网盘链接有效性
        返回:
            包含每个链接检测结果的列表
        """
        results = []
        for link in links:
            result = BaiduLinkService.check_link_validity(link)
            if result is None:
                results.append({"link": link, "valid": None, "message": "检测错误"})
            elif result is False:
                results.append({"link": link, "valid": False, "message": "链接无效"})
            else:
                results.append({"link": link, "valid": True, "message": "链接有效"})
        return results