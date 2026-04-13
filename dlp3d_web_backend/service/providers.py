"""Provider requirements configuration for API key management.

This module defines the API key requirements for different service providers
used in the system, including Large Language Model (LLM), Automatic Speech
Recognition (ASR), and Text-to-Speech (TTS) services.

Official docs for touched interfaces:
- OpenAI:
  https://platform.openai.com/docs/overview
- SenseNova / SenseChat:
  https://platform.sensenova.cn/product/APIService/document
- DeepSeek:
  https://api-docs.deepseek.com/
- xAI:
  https://docs.x.ai/docs/overview
- Anthropic:
  https://docs.anthropic.com/en/api/overview
- Google Gemini:
  https://ai.google.dev/gemini-api/docs
- ElevenLabs:
  https://elevenlabs.io/docs/introduction
- SoftSugar:
  https://aigc.softsugar.com/html/help/en-US/9-%E8%AF%AD%E9%9F%B3%E5%A4%84%E7%90%86.html
- Volcengine realtime dialogue:
  https://www.volcengine.com/docs/6561/1594356?lang=zh
- Volcengine streaming ASR big model:
  https://www.volcengine.com/docs/6561/1354869?lang=zh
- Doubao speech:
  https://www.volcengine.com/docs/6561/120572
- Alibaba Bailian / DashScope Qwen:
  https://help.aliyun.com/zh/model-studio/use-qwen-by-calling-api
"""

LLM_REQUIREMENTS = dict(
    openai={'openai_api_key'},
    volcengine={'volcengine_app_id', 'volcengine_token'},
    volcengine_ark={'volcengine_api_key'},
    xai={'xai_api_key'},
    anthropic={'anthropic_api_key'},
    gemini={'gemini_api_key'},
    qwen={'qwen_api_key'},
    deepseek={'deepseek_api_key'},
    sensenova={'sensenova_ak', 'sensenova_sk'},
    sensechat={'sensechat_ak', 'sensechat_sk'},
    sensenovaomni={'sensenovaomni_ak', 'sensenovaomni_sk'},
)

ASR_REQUIREMENTS = dict(
    openai={'openai_api_key'},
    qwen={'qwen_api_key'},
    zoetrope=set(),
    softsugar={'softsugar_app_id', 'softsugar_app_key'},
    doubao={'huoshan_app_id', 'huoshan_token'},
    huoshan={'huoshan_app_id', 'huoshan_token'},
    volcengine={'volcengine_app_id', 'volcengine_token'},
)

TTS_REQUIREMENTS = dict(
    chatterbox=set(),
    zoetrope=set(),
    doubao={'huoshan_app_id', 'huoshan_token'},
    doubao_icl={'huoshan_app_id', 'huoshan_token'},
    huoshan={'huoshan_app_id', 'huoshan_token'},
    huoshan_icl={'huoshan_app_id', 'huoshan_token'},
    softsugar={'softsugar_app_id', 'softsugar_app_key'},
    sensenova={'nova_tts_api_key'},
    elevenlabs={'elevenlabs_api_key'}
)
