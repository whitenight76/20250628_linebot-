import gradio as gr

with gr.Blocks() as demo:
    gr.Markdown("## 歡迎使用Gradio互動介面")
    input_textbox = gr.Textbox(label="輸入框", placeholder="請輸入在這裡")
    output_textbox = gr.Textbox(label="輸出框", placeholder="結果顯示在這裡")

    @input_textbox.change(inputs=input_textbox, outputs=output_textbox)
    def update_output(text):
        return text
    
demo.launch()