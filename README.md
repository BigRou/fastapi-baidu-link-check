# 百度网盘链接检测API

## 项目简介
这是一个基于FastAPI的百度网盘链接有效性检测服务，可以快速判断百度网盘分享链接是否有效。

## 功能特性
- 检测百度网盘链接有效性
- 返回明确的检测结果（有效/无效/错误）
- 简单的RESTful API接口

## API使用说明

### 检测链接有效性

**请求方式**: POST

**端点**: `/api/check-link`

**请求参数**:
```json
{
  "link": "百度网盘分享链接"
}
```

**响应示例**:
```json
{
  "valid": true,
  "message": "链接有效"
}
```

### 批量检测链接有效性

**请求方式**: POST

**端点**: `/api/batch-check`

**请求参数**:
```json
{
  "links": [
    "百度网盘分享链接1",
    "百度网盘分享链接2"
  ]
}
```

**响应示例**:
```json
{
  "results": [
    {
      "link": "https://pan.baidu.com/share/init?surl=s_qH8y4iadl-nZa6sCuecA",
      "valid": true,
      "message": "链接有效"
    },
    {
      "link": "https://pan.baidu.com/s/1rB2-kURSHcMXo5EQDXZIbg",
      "valid": false,
      "message": "链接无效"
    }
  ]
}
```

## 安装指南

1. 克隆项目
```bash
git clone https://github.com/BigRou/fastapi-baidu-link-check.git
cd fastapi-baidu-link-check
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 启动服务
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8488
```



## 依赖项
- FastAPI
- requests
- beautifulsoup4

## 常见问题

**Q**: 服务启动后如何访问API?
**A**: 默认地址是 `http://localhost:8488/api/check-link`

**Q**: 返回结果中valid为null是什么意思?
**A**: 表示检测过程中出现错误，可能是网络问题或链接格式不正确。