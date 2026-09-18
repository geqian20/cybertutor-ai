import os
from dotenv import load_dotenv
import anthropic

load_dotenv()

api_key=os.getenv("AI_API_KEY")
base_url=os.getenv("AI_BASE_URL")
model_name=os.getenv("AI_MODEL_NAME")

client=anthropic.Anthropic(api_key=api_key,base_url=base_url)

def chat_with_ai(user_input):
    print("正在思考中...")
    
    try:
        response=client.messages.create(
            model=model_name,
            max_tokens=1024,
            system="你是一个网络安全助教，非常乐于助人，讲解清晰易懂",
            messages=[
                {"role":"user","content":user_input}
                ]
        )
        
        for block in response.content:
            if block.type=="text":
                return block.text
            
        return "没有获取到有效回复"
    
    except Exception as e:
        return f"发生错误：{e}"
    

if __name__=="__main__":
    print("=== Claude Agent v0.1 (基础对话版) ===")
    print("输入 'exit' 退出程序")
    
    while True:
        question=input("\n你: ")
        
        if question.strip().lower()=="exit":
            print("再见！")
            break
    
        answer=chat_with_ai(question)
        print(f"AI:{answer}")
