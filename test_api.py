import requests
import json

# 测试批量检测API
def test_batch_check():
    url = 'http://127.0.0.1:8000/api/batch-check'
    payload = {
        "links": [
            "https://pan.baidu.com/s/1rB2-kURSHcMXo5EQDXZIbg",
            "https://pan.baidu.com/share/init?surl=s_qH8y4iadl-nZa6sCuecA"
        ]
    }
    
    response = requests.post(url, json=payload)
    print(f"状态码: {response.status_code}")
    print(json.dumps(response.json(), ensure_ascii=False, indent=2))

# 测试单个链接检测API
def test_check_link():
    url = 'http://127.0.0.1:8000/api/check-link'
    payload = {
        "link": "https://pan.baidu.com/s/1rB2-kURSHcMXo5EQDXZIbg"
    }
    
    response = requests.post(url, json=payload)
    print(f"状态码: {response.status_code}")
    print(json.dumps(response.json(), ensure_ascii=False, indent=2))

# 测试错误的请求格式 - 这是用户遇到的问题
def test_wrong_format():
    url = 'http://127.0.0.1:8000/api/check-link'
    # 错误的请求格式 - 使用了links而不是link
    payload = {
        "links": [
            "https://pan.baidu.com/s/1rB2-kURSHcMXo5EQDXZIbg",
            "https://pan.baidu.com/share/init?surl=s_qH8y4iadl-nZa6sCuecA"
        ]
    }
    
    response = requests.post(url, json=payload)
    print(f"状态码: {response.status_code}")
    print(json.dumps(response.json(), ensure_ascii=False, indent=2))

if __name__ == "__main__":
    print("\n1. 测试批量检测API:")
    test_batch_check()
    
    print("\n2. 测试单个链接检测API:")
    test_check_link()
    
    print("\n3. 测试错误的请求格式:")
    test_wrong_format()