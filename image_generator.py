from openai import OpenAI
from datetime import datetime

# APIキーの設定方法:
# 1. 環境変数: export OPENAI_API_KEY="your-api-key-here"
# 2. 直接指定: client = OpenAI(api_key="your-api-key-here")
client = OpenAI()  # 環境変数 OPENAI_API_KEY を使用

def generate_image(prompt_text, filename=None):
    """画像を生成して保存する関数"""
    try:
        result = client.images.generate(
            model="dall-e-2",
            prompt=prompt_text,
            size="1024x1024",
            n=1
        )
        
        image_url = result.data[0].url
        
        # ファイル名が指定されていない場合、タイムスタンプを使用
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"generated_image_{timestamp}.png"
        
        # URLから画像をダウンロード
        import requests
        response = requests.get(image_url)
        
        with open(filename, "wb") as f:
            f.write(response.content)
            
        print(f"画像が正常に生成されました: {filename}")
        return filename
        
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        return None

# 使用例
if __name__ == "__main__":
    prompt = """
    A delightful cartoon turtle character running with determination and joy, 
    perfect for a timer app mascot. The turtle has vibrant emerald green shell 
    with golden patterns, wearing bright orange running sneakers and a cute 
    red headband. Its expression shows focused concentration mixed with happiness, 
    with sparkling eyes full of energy. The turtle is captured mid-stride in 
    a dynamic running pose against a clean white background, suitable for web use. 
    The art style is modern, clean, and friendly - perfect for a productivity app.
    """
    
    generate_image(prompt, "timer_turtle_mascot.png")