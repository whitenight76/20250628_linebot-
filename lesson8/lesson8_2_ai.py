#建立一個gradio的Block架構
#功能
#1.使用者輸入名字
#2.建立輸出框
#3.建立按鈕

import gradio as gr
#的文字框中獲取。
def greet(name):
    return f"Hello {name}!"  # 返回一個問候語 
# 使用Gradio的Block架構來建立一個簡單的互動介面
# 使用with語句來定義Block架構
with gr.Blocks() as demo:
    name_textbox = gr.Textbox(label="your name", placeholder="請輸入在這裡")  # 用戶輸入名字的文字框
    output_textbox = gr.Textbox(label="輸出位置", placeholder="結果顯示在這裡")  # 顯示結果的文字框
    greet_button = gr.Button("請點擊")  # 按鈕，點擊後觸發問候函數

    # 當按鈕被點擊時，呼叫greet函數，並將name_textbox的輸入作為參數傳遞給它
    greet_button.click(
        fn=greet,
        inputs=[name_textbox],
        outputs=[output_textbox]
    )