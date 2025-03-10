import tkinter as tk

def find_set_bits(hex_number):
    try:
        # 将16进制字符串转换为整数
        num = int(hex_number, 16)
        # 获取该数的二进制表示，去掉前面的'0b'
        binary_representation = bin(num)[2:]
        # 找出所有设置为1的位的位置
        set_bits = [len(binary_representation) - i for i, bit in enumerate(binary_representation, start=1) if bit == '1']
        return set_bits
    except ValueError:
        return "无效的16进制输入"

def on_submit():
    hex_input = entry.get()
    result = find_set_bits(hex_input)
    result_label.config(text="设置为1的位的位置为: " + str(result))

# 创建主窗口
root = tk.Tk()
root.title("16进制数位检查器")

# 创建输入框
entry = tk.Entry(root, width=30)
entry.pack(pady=20)

# 创建提交按钮
submit_button = tk.Button(root, text="提交", command=on_submit)
submit_button.pack(pady=10)

# 创建结果显示标签
result_label = tk.Label(root, text="")
result_label.pack(pady=20)

# 运行主循环
root.mainloop()
