import gradio as gr

with gr.Blocks() as demo:
    a = gr.Number(label="輸入數字", value=0, precision=2, step=0.1)
    b = gr.Number(label="輸入數字", value=0, precision=2, step=0.1)
    gr.Markdown("## 數字計算器")
    gr.Markdown("### 選擇計算方式")
    gr.Markdown("請輸入兩個數字，然後選擇計算方式。")
    gr.Markdown("### 結果將顯示在下方")
    with gr.Row():
        add_button = gr.Button("加法")
        subtract_button = gr.Button("減法")
        multiply_button = gr.Button("乘法")
        divide_button = gr.Button("除法")
    with gr.Row():
        reset_button = gr.Button("重置")
    c=gr.Number(label="結果", value=0, precision=2, step=0.1)
    @add_button.click(inputs=[a, b], outputs=c)
    def add(a, b):
        return a + b
    @subtract_button.click(inputs=[a, b], outputs=c)
    def subtract(a, b):
        return a - b
    @multiply_button.click(inputs=[a, b], outputs=c)
    def multiply(a, b):
        return a * b
    @divide_button.click(inputs=[a, b], outputs=c)
    def divide(a, b):   
        if b == 0:
            return "除數不能為零"
        return a / b
    @reset_button.click(inputs=[], outputs=[a, b, c])
    def reset():
        return 0, 0, 0
demo.launch()
# 這個範例展示了如何使用Gradio的Block架構來建立一個簡單的數字計算器介面。
# 使用者可以輸入兩個數字，然後選擇加法、減法、乘法或除法
# 進行計算，結果將顯示在下方的結果框中
# 使用者也可以點擊重置按鈕來清除所有輸入和結果。
# 每個按鈕都會觸發相應的計算函數
# 並將輸入的數字作為參數傳遞給它們
# 最後，重置按鈕會清除所有輸入和結果框的值。
# 注意：除法按鈕會檢查除數是否為零，
# 如果是，則返回錯誤信息。