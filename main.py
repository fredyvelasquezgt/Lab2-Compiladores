
import sys
import os
from antlr4 import *
from build.yaplLexer import yaplLexer
from build.yaplParser import yaplParser
from yaplWalker import yaplWalker
from yaplErrorListener import yaplErrorListener

import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
from prettytable import PrettyTable

# Paleta de colores
PALETTE = {
    "background": "#343a40",
    "text": "white",
    "code_background": "#2c3e50",
    "symbolT_background": "#1e1e1e",
    "highlight": "#e0a800",
    "button_background": "#3498db",  # Nuevo color de fondo para botones
    "button_text": "white"  # Nuevo color de texto para botones
}

def on_enter(e):
    tooltip_label["text"] = "Click to parse the code"

def on_leave(e):
    tooltip_label["text"] = ""

def create_text_area(parent, **kwargs):
        frame = Frame(parent)
        scrollbar = Scrollbar(frame)
        text_widget = tk.Text(frame, **kwargs, yscrollcommand=scrollbar.set)
        scrollbar.config(command=text_widget.yview)
        
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        return frame, text_widget    

input = ""
# Class that writes line number in text widget
class LineNumbers(tk.Text):
    def __init__(self, master, text_widget, **kwargs):
        super().__init__(master, **kwargs)

        self.text_widget = text_widget
        self.text_widget.bind('<KeyPress>', self.on_key_press)

        self.insert(1.0, '1')
        self.configure(state='disabled')

    def on_key_press(self, event=None):
        final_index = str(self.text_widget.index(tk.END))
        num_of_lines = final_index.split('.')[0]
        line_numbers_string = "\n".join(str(no + 1) for no in range(int(num_of_lines)))
        width = len(str(num_of_lines))

        self.configure(state='normal', width=width+1 if int(num_of_lines) < 10 else width)
        self.delete(1.0, tk.END)
        self.insert(1.0, line_numbers_string)
        self.configure(state='disabled')

    


def open_file():
    file_path = askopenfile(initialdir = "./input", mode='r', filetypes=[('YAPL Files', '*yapl'), ("all files", "*.*")])
    if file_path is not None:
        # pass
        filename_splited = file_path.name.split("/")
        filename_splited = filename_splited[len(filename_splited)-1]
        hola = filename_splited[len(filename_splited)-2]
        archivo1_ = "input/" + filename_splited

        content = file_path.read()
        text_area_code.insert(tk.INSERT, content, "\n")
        runbtn.config(state="normal")

def run():
    with open('input/temp.yapl', 'w') as f:
        fetched_content = text_area_code.get('1.0', 'end-1c')
        f.write(fetched_content)
    run_main.set(True)

def clear():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def main():
    # input = FileStream(argv[1])
    input = FileStream('input/temp.yapl')

    lexer = yaplLexer(input)
    lexer.removeErrorListeners()
    lexer.addErrorListener(yaplErrorListener())

    stream = CommonTokenStream(lexer)
    stream.fill()

    print("Tokens:")
    for token in stream.tokens:
        print(token)

    parser = yaplParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(yaplErrorListener())

    tree = parser.prog()
    print("\nParse Tree:")
    print(tree.toStringTree(parser.ruleNames))

    walker = yaplWalker()
    walker.initSymbolTable()
    walker.visit(tree)

    cont = 0
    print("\nSymbol Table:")
    myTable = PrettyTable()
    for record in walker.symbolTable.records:
        cont = cont + 1
        # print("Symbol", record.toString())
        myTable.field_names = record.keys()
        myTable.add_row(record.values())
    print(myTable)
    text_area_symbolT.insert(tk.INSERT, myTable)



    if len(walker.errors) >= 1:
        print("\n" + yaplErrorListener.ANSI_RED)
        print("----------------------------- ERROR -----------------------------")
        for error in walker.errors:
            if "payload" in error:
                print("Error: position " + str(error["payload"].line) + ":" + str(error["payload"].column) + " " + error["msg"])
                
            else:
                print("Error: " + error["msg"])
            

        print("-----------------------------------------------------------------")
        print("\n" + yaplErrorListener.ANSI_RESET)


    

    



if __name__ == '__main__':
    window = tk.Tk()
    window.title('Analizador Semántico')
    window.state('zoomed')
    window.configure(bg=PALETTE["background"])

    run_main = BooleanVar()

    # Styling UI elements
    style = Style()
    style.configure("TButton", background=PALETTE["button_background"], foreground=PALETTE["button_text"], font=("Arial", 12, "bold"))

    # Definition of UI elements
    adharbtn = Button(window, text='Choose File', command=lambda: open_file())
    runbtn = Button(window, text='Run', command=run)
    clearbtn = Button(window, text='Clear', command=clear)
    tooltip_label = Label(window, text="", background=PALETTE["background"], foreground="gray")
    label_file_explorer = tk.Label(window, text=" ", width=20, height=2, fg=PALETTE["text"], bg=PALETTE["background"])

    frame_code, text_area_code = create_text_area(window, font=("Consolas", 12), fg=PALETTE["text"], bg=PALETTE["code_background"], highlightthickness=0)
    frame_symbolT, text_area_symbolT = create_text_area(window, font=("Consolas", 10), fg="skyblue", bg=PALETTE["symbolT_background"], highlightthickness=0)
    l = LineNumbers(window, text_area_code, font=("Consolas", 12), fg="gray", bg="#2e2e2e", highlightthickness=0)

    # Add elements to UI
    adharbtn.grid(row=0, column=0, padx=(10, 10), pady=(10, 0), sticky="news")
    runbtn.grid(row=0, column=1, padx=(10, 10), pady=(10, 0), sticky="news")
    clearbtn.grid(row=0, column=2, padx=(10, 10), pady=(10, 0), sticky="news")
    tooltip_label.grid(row=0, column=3, padx=(10, 10), pady=(10, 0), sticky="news")
    label_file_explorer.grid(row=0, column=4, padx=(10, 10), pady=(10, 0), sticky="news")

    l.grid(row=1, column=0, sticky="ns", padx=(10, 0))
    frame_code.grid(row=1, column=1, columnspan=4, pady=(10, 10), padx=(10, 10), sticky="news")
    frame_symbolT.grid(row=2, column=0, columnspan=5, pady=(10, 10), padx=(10, 10), sticky="news")

    # Stretch configurations
    for i in range(5):
        window.grid_columnconfigure(i, weight=1)
    window.grid_rowconfigure(1, weight=1)

    runbtn.wait_variable(run_main)
    main()
    window.mainloop()