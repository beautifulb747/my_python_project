import random
import tkinter as tk
from tkinter import messagebox
import os
X = 114154
folder_path = 'D:\\24-point game'

if os.path.exists(folder_path):
    i = 1 + 1
else:
    os.mkdir(folder_path)

class Game24:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("欢乐24点")
        self.root.geometry("320x300")
        label = tk.Label(self.root, text="欢迎来玩欢乐24点！", font=("Arial", 18))
        label.pack(pady=10)

        start_btn = tk.Button(self.root, text="开始", font=("Arial", 24), bg="#4CAF50", fg="white", command=self.start_game)
        start_btn.pack(pady=5)

        exit_btn = tk.Button(self.root, text="退出", font=("Arial", 12), bg="#D32F2F", fg="white", command=self.root.quit)
        exit_btn.pack(pady=5)

        def on_btn_click():
            window = tk.Tk()
            window.geometry("400x300")
            window.title("关于")
            text_widget = tk.Text(window, height=20, width=50)
            text_widget.insert("end", "by beautifulb747@163.com \n欢乐24点 v:1.2.0 py\n主程序编写：beautifulb747@163.com\n注：【帮助】程序算法可能存在缺陷，如程序算不出24可以在网上查询\n反馈想法、意见或错误，请联系beautifulb747@163.com")
            text_widget.configure(state="disabled")
            text_widget.pack()

        start_btn = tk.Button(self.root, text="关于", font=("Arial", 12), bg="#2196F3", fg="white", command=on_btn_click)
        start_btn.pack(pady=5)

        def on_btn_click1():
            window = tk.Tk()
            window.geometry("400x300")
            window.title("规则")
            text_widget = tk.Text(window, height=20, width=50)
            text_widget.insert("end", "点击【开始】按钮以开始游戏\n输入算式时注意：\n1.乘和除用*和/表示\n2.输入的算式不要加等于号，否则会报错。\n3.算式中的括号必须是英文的，否则会报错。\n反馈想法、意见或错误，请联系beautifulb747@163.com")
            text_widget.configure(state="disabled")
            text_widget.pack()

        start_btn = tk.Button(self.root, text="规则", font=("Arial", 12), bg="#2196F3", fg="white", command=on_btn_click1)
        start_btn.pack(pady=5)
        self.score = 0
        self.load_score()
        self.score_label = tk.Label(self.root, text=f"累计积分：{self.score}", font=("Arial", 16))
        self.score_label.pack(pady=10)

    def start_game(self):
        nums = self.generate_nums()
        self.show_nums(nums)

    def generate_nums(self):
        group1 = [(1, 3, 4, 6),  (2, 3, 3, 8), (2, 5, 7, 1), (2, 3, 3, 7),
                  (2, 3, 6, 9), (2, 4, 7, 7),  (3, 3, 8, 8), (1, 3, 6, 5),
                  (3, 4, 6, 6), (3, 5, 5, 7), (4, 4, 5, 9),  (1, 3, 5, 10),
                  (1, 3, 7, 11), (1, 4, 5, 7), (1, 4, 7, 7), (1, 5, 6, 9),
                  (2, 5, 7, 10), (2, 5, 8, 9), (2, 6, 7, 8), (2, 6, 8, 10),
                  (2, 7, 9, 10), (2, 8, 8, 10), (3, 6, 7, 10), (3, 6, 8, 8),
                  (3, 7, 7, 7), (3, 7, 9, 9), (3, 8, 9, 10), (1, 1, 6, 8),
                  (4, 5, 9, 10), (4, 6, 6, 10), (4, 7, 8, 10), (4, 8, 9, 9),
                  (5, 5, 8, 10), (5, 6, 8, 8), (5, 6, 9, 9), (5, 7, 7, 10),
                  (5, 7, 9, 10), (6, 6, 7, 9), (6, 7, 8, 9), (6, 7, 9, 10),
                  (1, 3, 5, 10), (1, 3, 7, 11), (1, 4, 5, 7), (1, 4, 7, 7),
                  (1, 5, 6, 9), (1, 5, 7, 8), (1, 6, 6, 9), (2, 5, 7, 10),
                  (2, 5, 8, 9), (2, 6, 7, 8), (2, 6, 8, 10), (2, 7, 9, 10),
                  (2, 8, 8, 10), (3, 6, 7, 10), (3, 6, 8, 8), (3, 7, 7, 7),
                  (3, 7, 8, 10), (3, 7, 9, 9), (3, 8, 9, 10), (4, 5, 9, 10),
                  (4, 6, 6, 10), (4, 7, 8, 10), (4, 8, 9, 9), (1, 4, 5, 5),
                  (5, 6, 9, 9), (5, 7, 7, 10), (5, 7, 9, 10), (1, 2, 7, 5),
                  (6, 6, 7, 9), (6, 7, 8, 9), (6, 7, 9, 10), (1, 1, 4, 5),
                  (1, 2, 3, 9), (1, 2, 4, 8), (1, 2, 5, 7), (1, 2, 6, 6),
                  (1, 2, 8, 4), (1, 2, 9, 3), (1, 3, 4, 7), (1, 3, 5, 6),
                  (1, 3, 7, 4), (1, 3, 8, 3), (1, 3, 9, 2), (1, 4, 4, 8),
                  (1, 4, 7, 3), (1, 4, 8, 2), (1, 4, 9, 1), (1, 5, 5, 4),
                  (1, 5, 6, 3), (1, 5, 7, 2), (1, 5, 8, 1), (1, 6, 6, 2),
                  (1, 1, 4, 5), (2, 2, 3, 8), (2, 2, 4, 7), (2, 2, 5, 6),
                  (2, 2, 6, 5), (2, 2, 7, 4), (2, 2, 8, 3), (2, 2, 9, 2),
                  (2, 3, 4, 6), (2, 3, 5, 5), (2, 3, 6, 4), (2, 3, 7, 3),
                  (2, 3, 9, 1), (2, 4, 4, 6), (2, 4, 5, 5), (2, 4, 6, 4),
                  (2, 4, 8, 2), (2, 4, 9, 1), (2, 5, 5, 3), (2, 5, 6, 2),
                  (2, 6, 6, 1), (1, 5, 7, 8), (1, 6, 6, 9), (1, 6, 7, 1),
                  (2, 3, 8, 2), (2, 3, 8, 2),  (2, 4, 7, 3), (1, 2, 6, 6)]

        nums = random.choice(group1)
        return nums

    def show_nums(self, nums):
        nums_str = [str(num) for num in nums]
        expression_str = "  ".join(nums_str)

        self.window = tk.Toplevel(self.root)
        self.window.title("欢乐24点    开始答题")
        self.window.geometry("320x240")

        label = tk.Label(self.window, text=f"请使用这四个数算出24：{expression_str}", font=("Arial", 12))
        label.pack(pady=10)

        entry = tk.Entry(self.window, width=20, font=("Arial", 12))
        entry.bind("<Return>", lambda event: self.handle_expression(nums, entry.get()))
        entry.pack(pady=10)

        button = tk.Button(self.window, text="确定", font=("Arial", 12), bg="#4CAF50", fg="white",
                           command=lambda: self.handle_expression(nums, entry.get()))
        button.pack(pady=10)

        def on_btn_click3():
            import collections
            import tkinter as tk
            from tkinter import messagebox
            def evaluate_rpn(rpn):
                stack = []
                operators = ['+', '-', '*', '/']
                for token in rpn:
                    if token in operators:
                        b = stack.pop()
                        a = stack.pop()
                        if token == '+':
                            result = a + b
                        elif token == '-':
                            result = a - b
                        elif token == '*':
                            result = a * b
                        else:
                            result = a / b
                        stack.append(result)
                    else:
                        stack.append(token)
                return stack[0]

            def infix_to_rpn(infix):
                precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
                output = []
                operator_stack = []
                for token in infix:
                    if token.isdigit():
                        output.append(int(token))
                    elif token in precedence:
                        while operator_stack and operator_stack[-1] in precedence \
                                and precedence[token] <= precedence[operator_stack[-1]]:
                            output.append(operator_stack.pop())
                        operator_stack.append(token)
                    elif token == '(':
                        operator_stack.append(token)
                    elif token == ')':
                        while operator_stack[-1] != '(':
                            output.append(operator_stack.pop())
                        operator_stack.pop()
                while operator_stack:
                    output.append(operator_stack.pop())
                return output

            def expand(current, nums):
                result = []
                for i in range(len(current)):
                    for j in range(i + 1, len(current)):
                        for op in ['+', '-', '*', '/']:
                            new = list(current)
                            exp = f"({current[i]}{op}{current[j]})"
                            rpn = infix_to_rpn(exp)
                            try:
                                value = evaluate_rpn(rpn)
                                if value < 0 or value > 100:
                                    continue
                                new.pop(j)
                                new.pop(i)
                                new.append(value)
                                result.append((new, exp))
                            except ZeroDivisionError:
                                continue
                return result

            def bfs(nums):
                queue = collections.deque([(nums, '')])
                visited = set()
                visited.add(tuple(nums))
                while queue:
                    current, exp = queue.popleft()
                    if len(current) == 1 and current[0] == 24:
                        return exp
                    for next_state, next_exp in expand(current, nums):
                        if tuple(next_state) not in visited:
                            visited.add(tuple(next_state))
                            queue.append((next_state, f"{exp} {next_exp}"))
                return None

            def calculate():
                num1 = int(entry1.get())
                num2 = int(entry2.get())
                num3 = int(entry3.get())
                num4 = int(entry4.get())
                result = bfs([num1, num2, num3, num4])

                if result:
                    messagebox.showinfo(message=f"您输入的数字可以组成24点！{result}", title="提示")
                else:
                    messagebox.showinfo(
                        message="您输入的数字程序计算无解。\n如果在网上（建议百度）查询未果，请反馈beautifulb747@163.com 谢谢。", title="提示")
            window = tk.Tk()
            window.title("24点计算器")
            window.geometry("300x150")

            instruction_label = tk.Label(window, text="请输入四个数字，点击计算按钮计算以获取结果。")
            instruction_label.pack(side=tk.TOP, pady=10)

            entry1 = tk.Entry(window, width=4)
            entry1.pack(side=tk.LEFT, padx=5)
            entry2 = tk.Entry(window, width=4)
            entry2.pack(side=tk.LEFT, padx=5)
            entry3 = tk.Entry(window, width=4)
            entry3.pack(side=tk.LEFT, padx=5)
            entry4 = tk.Entry(window, width=4)
            entry4.pack(side=tk.LEFT, padx=5)
            calculate_button = tk.Button(window, text="计算", command=calculate)
            calculate_button.pack(side=tk.BOTTOM, pady=10)

            result_label = tk.Label(window, text="")
            result_label.pack(side=tk.TOP)

            window.mainloop()

        button = tk.Button(self.window, text="帮助", bg="#2196F3", fg="white", command=on_btn_click3)
        button.pack(pady=10)

        start_button = tk.Button(self.window, text="跳过", bg="#D32F2F", fg="white",
                                 command=lambda: (self.window.destroy(), self.start_game()))
        start_button.pack(side=tk.BOTTOM, pady=10)

        self.window.mainloop()

    def handle_expression(self, nums, expression):
        used_nums = [num for num in nums if str(num) in expression]
        if len(used_nums) != 4:
            messagebox.showinfo("错误", "算式必须使用给出的四个数字。")
            return
        try:
            result = eval(expression)
        except:
            messagebox.showinfo("错误", "算式无效，请重新输入。")
            return
        if result == 24:
            self.score += 1
            self.score_label.config(text=f"得分：{self.score}")
            messagebox.showinfo("恭喜", f"你算对了！\n当前得分：{self.score}")
            self.save_score()
            self.show_result()
        else:
            messagebox.showinfo("错误", "计算结果不是24，请重试。")

    def show_result(self):
        result = messagebox.askquestion("结果", "是否继续游戏？")
        if result == "no":
            self.root.quit()
        else:
            self.window.destroy()
            self.start_game()

    def run(self):
        self.root.mainloop()

    def load_score(self):
        if os.path.exists("D:\\score.txt"):
            with open("D:\\score.txt", "r") as f:
                self.score = int(f.read())

    def save_score(self):
        with open("D:\\score.txt", "w") as f:
            f.write(str(self.score))


if __name__ == "__main__":
    game = Game24()
    game.run()
