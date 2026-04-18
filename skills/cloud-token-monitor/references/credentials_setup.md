# 凭证配置指南

本文档说明各云厂商的认证方式配置。

## 阿里云（百炼/灵积）

1. 登录阿里云控制台
2. 进入「百炼」或「灵积」服务
3. 获取 API Key
4. 环境变量：`ALIYUN_API_KEY`

## 腾讯云（TI-ONE）

1. 登录腾讯云控制台
2. 进入 TI-ONE 服务
3. 获取 SecretId 和 SecretKey
4. 环境变量：`TENCENT_SECRET_ID`, `TENCENT_SECRET_KEY`

## 华为云（ModelArts）

1. 登录华为云控制台
2. 进入 ModelArts 服务
3. 获取 AK/SK
4. 环境变量：`HUAWEI_ACCESS_KEY`, `HUAWEI_SECRET_KEY`

## 百度云（千帆）

1. 登录百度云控制台
2. 进入千帆大模型平台
3. 获取 API Key 和 Secret Key
4. 环境变量：`BAIDU_API_KEY`, `BAIDU_SECRET_KEY`

## 火山引擎（方舟）

1. 登录火山引擎控制台
2. 进入方舟平台
3. 获取 API Key
4. 环境变量：`VOLCENGINE_API_KEY`

## AWS（Bedrock）

1. 登录 AWS 控制台
2. 创建 IAM 用户并授予 Bedrock 权限
3. 获取 Access Key ID 和 Secret Access Key
4. 环境变量：`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_REGION`

## Azure（OpenAI Service）

1. 登录 Azure 门户
2. 创建 OpenAI 服务
3. 获取 Endpoint 和 API Key
4. 环境变量：`AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_API_KEY`

## Google Cloud（Vertex AI）

1. 创建 GCP 项目
2. 启用 Vertex AI API
3. 创建服务账号并下载 JSON 密钥
4. 环境变量：`GOOGLE_APPLICATION_CREDENTIALS`（指向 JSON 文件路径）

## Google AI（Gemini API）

1. 登录 Google AI Studio
2. 获取 API Key
3. 环境变量：`GOOGLE_AI_API_KEY`

## OpenAI

1. 登录 OpenAI 平台
2. 获取 API Key
3. 环境变量：`OPENAI_API_KEY`

## Anthropic

1. 登录 Anthropic Console
2. 获取 API Key
3. 环境变量：`ANTHROPIC_API_KEY`
