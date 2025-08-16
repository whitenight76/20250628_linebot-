## Block架構

import gradio as gr
# 這個範例展示了如何使用Gradio的Block架構來建立一個簡單的互動介面
def greet(name):
    return f"Hello {name}!"# 這個函數會在使用者輸入名字後被呼叫，並返回
# 一個問候語。這裡的name參數會自動從使用

with gr.Blocks() as demo:
    name_textbox =gr.Textbox(label="your name",placeholder="請輸入在這裡")
    output_textbox = gr.Textbox(label="輸出位置",placeholder="結果顯示在這裡")
    greet_button = gr.Button("請點擊")
    greet_button.click(
        fn=greet,
        inputs=[name_textbox],
        outputs=[output_textbox]
    )   
    
    demo.launch()