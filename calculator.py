from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename='superhero')
root.title('Calculator')
root.geometry('410x520')
root.iconbitmap('calculator_logo.ico')

#  function for add strings[number, symbol] to display
calculation = ''
def add_to_text_field(x) :
   global calculation
   calculation += str(x)
   text_box.delete(1.0, 'end')
   text_box.insert(1.0, calculation) 

#  function to evaluate the strings
def evaluate() :
   global calculation
   try:
      result = str(eval(calculation))
      text_box.delete(1.0, 'end')
      text_box.insert(1.0, result)
   except ZeroDivisionError:
      clear_field()
      add_to_text_field('Cannot divide by zero')
   except Exception as e:
      clear_field()
      add_to_text_field('Error: ' + str(e))

#  function to clear the display
def clear_field() :
   global calculation
   calculation = ''
   print(calculation)
   text_box.delete(1.0, 'end')

#  function to delete strings one by one
def delete() :
   global calculation
   calculation = calculation[ :-1]
   text_box.delete(1.0, 'end')
   text_box.insert(1.0, calculation)

#  creating display
text_box = tb.Text(root, font=('Helvetica', 24), height=2)
text_box.pack(padx=10, pady=20)

#  creating button container to hold the all buttons
button_container = tb.Frame(root, bootstyle='dark')
button_container.pack(padx=10, pady=10,)

# creating style to resize the button
my_style = tb.Style()
my_style.configure('light.Outline.TButton', font=("Helvetica", 20), width=3)

#  creating button
button_open = tb.Button(button_container, text='(', style="light.Outline.TButton", command=lambda:add_to_text_field('('))
button_open.grid(padx=10, pady= 10, row=2, column=1)
button_close = tb.Button(button_container, text=')', style="light.Outline.TButton,", command=lambda:add_to_text_field(')'))
button_close.grid(padx=10, pady= 10, row=2, column=2)
button_del = tb.Button(button_container, text='Del', style="light.Outline.TButton,", command=delete)
button_del.grid(padx=10, pady= 10, row=2, column=3)
button_AC = tb.Button(button_container, text='AC', style="light.Outline.TButton,", command=clear_field)
button_AC.grid(padx=10, pady= 10, row=2, column=4)

button_7 = tb.Button(button_container, text='7', style="light.Outline.TButton,", command=lambda:add_to_text_field('7'))
button_7.grid(padx=10, pady= 10, row=3, column=1)
button_8 = tb.Button(button_container, text='8', style="light.Outline.TButton,", command=lambda:add_to_text_field('8'))
button_8.grid(padx=10, pady= 10, row=3, column=2)
button_9 = tb.Button(button_container, text='9', style="light.Outline.TButton,", command=lambda:add_to_text_field('9'))
button_9.grid(padx=10, pady= 10, row=3, column=3)
button_div = tb.Button(button_container, text='÷', style="light.Outline.TButton,", command=lambda:add_to_text_field('/'))
button_div.grid(padx=10, pady= 10, row=3, column=4)

button_4 = tb.Button(button_container, text='4', style="light.Outline.TButton,", command=lambda:add_to_text_field('4'))
button_4.grid(padx=10, pady= 10, row=4, column=1)
button_5 = tb.Button(button_container, text='5', style="light.Outline.TButton,", command=lambda:add_to_text_field('5'))
button_5.grid(padx=10, pady= 10, row=4, column=2)
button_6 = tb.Button(button_container, text='6', style="light.Outline.TButton,", command=lambda:add_to_text_field('6'))
button_6.grid(padx=10, pady= 10, row=4, column=3)
button_mul = tb.Button(button_container, text='x', style="light.Outline.TButton,", command=lambda:add_to_text_field('*'))
button_mul.grid(padx=10, pady= 10, row=4, column=4)

button_1 = tb.Button(button_container, text='1', style="light.Outline.TButton,", command=lambda:add_to_text_field('1'))
button_1.grid(padx=10, pady= 10, row=5, column=1)
button_2 = tb.Button(button_container, text='2', style="light.Outline.TButton,", command=lambda:add_to_text_field('2'))
button_2.grid(padx=10, pady= 10, row=5, column=2)
button_3 = tb.Button(button_container, text='3', style="light.Outline.TButton,", command=lambda:add_to_text_field('3'))
button_3.grid(padx=10, pady= 10, row=5, column=3)
button_min = tb.Button(button_container, text='-', style="light.Outline.TButton,", command=lambda:add_to_text_field('-'))
button_min.grid(padx=10, pady= 10, row=5, column=4)

button_0 = tb.Button(button_container, text='0', style="light.Outline.TButton,", command=lambda:add_to_text_field('0'))
button_0.grid(padx=10, pady= 10, row=6, column=1)
button_dot = tb.Button(button_container, text='.', style="light.Outline.TButton,", command=lambda:add_to_text_field('.'))
button_dot.grid(padx=10, pady= 10, row=6, column=2)
button_equal = tb.Button(button_container, text='=', style="light.Outline.TButton,", command=evaluate)
button_equal.grid(padx=10, pady= 10, row=6, column=3)
button_add = tb.Button(button_container, text='+', style="light.Outline.TButton,", command=lambda:add_to_text_field('+'))
button_add.grid(padx=10, pady= 10, row=6, column=4)

root.mainloop()