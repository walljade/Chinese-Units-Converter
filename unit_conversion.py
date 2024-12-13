import tkinter as tk
from tkinter import ttk

# 创建主窗口
root = tk.Tk()
root.title("中国古今单位转换器")
root.geometry("400x500")

# 定义转换因子
conversion_factors = {
    ("秦尺", "厘米"): 23.1,
    ("汉尺", "厘米"): 23.1,
    ("三国尺", "厘米"): 24.2,
    ("晋尺", "厘米"): 24.2,
    ("秦升", "毫升(今)"): 200,
    ("汉升", "毫升(今)"): 200,
    ("三国升", "毫升(今)"): 200,
    ("晋升", "毫升(今)"): 200,
    ("秦斤", "克"): 253,
    ("西汉斤", "克"): 250,
    ("新莽斤", "克"): 245,
    ("东汉斤", "克"): 222,
    ("曹魏斤", "克"): 220,
    ("晋斤", "克"): 220
}

# 定义通用转换函数
def convert_units(entry1, combo1, entry2, combo2):
    try:
        value = float(entry1.get())
        unit_from = combo1.get()
        unit_to = combo2.get()
        
        # 检查转换因子是否存在
        if (unit_from, unit_to) in conversion_factors:
            result = value * conversion_factors[(unit_from, unit_to)]
            entry2.config(state="normal")
            entry2.delete(0, tk.END)
            entry2.insert(0, f"{result:.2f}")
            entry2.config(state="readonly")
        else:
            entry2.config(state="normal")
            entry2.delete(0, tk.END)
            entry2.insert(0, "无法转换")
            entry2.config(state="readonly")
    except ValueError:
        entry2.config(state="normal")
        entry2.delete(0, tk.END)
        entry2.insert(0, "请输入有效的数字")
        entry2.config(state="readonly")

# 创建长度转换栏
length_frame = tk.LabelFrame(root, text="长度转换")
length_frame.grid(row=0, column=0, padx=10, pady=10, ipadx=10, ipady=10)

entry_length1 = tk.Entry(length_frame, width=10)
entry_length1.grid(row=0, column=0, padx=5, pady=10)

combo_length1 = ttk.Combobox(length_frame, values=["秦尺", "汉尺","三国尺", "晋尺"], width=5)
combo_length1.grid(row=0, column=1, padx=5, pady=10)
combo_length1.current(0)

label_equal1 = tk.Label(length_frame, text=" = ")
label_equal1.grid(row=0, column=2)

entry_length2 = tk.Entry(length_frame, width=10, state="readonly")
entry_length2.grid(row=0, column=3, padx=5, pady=10)

combo_length2 = ttk.Combobox(length_frame, values=["厘米"], width=5)
combo_length2.grid(row=0, column=4, padx=5, pady=10)
combo_length2.current(0)

button_length_convert = tk.Button(length_frame, text="转换", command=lambda: convert_units(entry_length1, combo_length1, entry_length2, combo_length2))
button_length_convert.grid(row=1, column=2, pady=10)

# 创建重量转换栏
weight_frame = tk.LabelFrame(root, text="重量转换")
weight_frame.grid(row=1, column=0, padx=10, pady=10, ipadx=10, ipady=10)

entry_weight1 = tk.Entry(weight_frame, width=10)
entry_weight1.grid(row=0, column=0, padx=5, pady=10)

combo_weight1 = ttk.Combobox(weight_frame, values=["秦斤", "西汉斤", "新莽斤", "东汉斤", "曹魏斤", "晋斤"], width=7)
combo_weight1.grid(row=0, column=1, padx=5, pady=10)
combo_weight1.current(0)

label_equal2 = tk.Label(weight_frame, text=" = ")
label_equal2.grid(row=0, column=2)

entry_weight2 = tk.Entry(weight_frame, width=10, state="readonly")
entry_weight2.grid(row=0, column=3, padx=5, pady=10)

combo_weight2 = ttk.Combobox(weight_frame, values=["克"], width=5)
combo_weight2.grid(row=0, column=4, padx=5, pady=10)
combo_weight2.current(0)

button_weight_convert = tk.Button(weight_frame, text="转换", command=lambda: convert_units(entry_weight1, combo_weight1, entry_weight2, combo_weight2))
button_weight_convert.grid(row=1, column=2, pady=10)

# 创建容量转换栏
volume_frame = tk.LabelFrame(root, text="容量转换")
volume_frame.grid(row=2, column=0, padx=10, pady=10, ipadx=10, ipady=10)

entry_volume1 = tk.Entry(volume_frame, width=10)
entry_volume1.grid(row=0, column=0, padx=5, pady=10)

combo_volume1 = ttk.Combobox(volume_frame, values=["秦升", "汉升", "三国升", "晋升"], width=5)
combo_volume1.grid(row=0, column=1, padx=5, pady=10)
combo_volume1.current(0)

label_equal3 = tk.Label(volume_frame, text=" = ")
label_equal3.grid(row=0, column=2)

entry_volume2 = tk.Entry(volume_frame, width=10, state="readonly")
entry_volume2.grid(row=0, column=3, padx=5, pady=10)

combo_volume2 = ttk.Combobox(volume_frame, values=["毫升(今)"], width=7)
combo_volume2.grid(row=0, column=4, padx=5, pady=10)
combo_volume2.current(0)

button_volume_convert = tk.Button(volume_frame, text="转换", command=lambda: convert_units(entry_weight1, combo_weight1, entry_weight2, combo_weight2))
button_volume_convert.grid(row=1, column=2, pady=10)

# 运行主循环
root.mainloop()