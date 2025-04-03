
## 正确的API使用方法

### 1. 单个链接检测API

**请求方式**: POST

**端点**: `/api/check-link`

**请求参数**:
```json
{
  "link": "百度网盘分享链接"
}
```

**示例**:
```json
{
  "link": "https://pan.baidu.com/s/1rB2-kURSHcMXo5EQDXZIbg"
}
```

**响应示例**:
```json
{
  "valid": false,
  "message": "链接无效"
}
```

### 2. 批量检测API

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

**示例**:
```json
{
  "links": [
    "https://pan.baidu.com/s/1rB2-kURSHcMXo5EQDXZIbg",
    "https://pan.baidu.com/share/init?surl=s_qH8y4iadl-nZa6sCuecA"
  ]
}
```

**响应示例**:
```json
{
  "results": [
    {
      "link": "https://pan.baidu.com/s/1rB2-kURSHcMXo5EQDXZIbg",
      "valid": false,
      "message": "链接无效"
    },
    {
      "link": "https://pan.baidu.com/share/init?surl=s_qH8y4iadl-nZa6sCuecA",
      "valid": true,
      "message": "链接有效"
    }
  ]
}
```

## 解决方案

根据您的需求，您应该使用批量检测API（`/api/batch-check`）而不是单个链接检测API（`/api/check-link`），因为您需要检测多个链接。

请确保您的请求发送到正确的端点，并使用正确的请求格式。