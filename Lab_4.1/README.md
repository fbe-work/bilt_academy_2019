# Python basics

### Hello world

As any newcomer to a programming language or programming in general, we start with a common first little task: 
To write a little program called hello world, which does nothing else but showing/printing a “hello world!” text to the screen. 
For some people this even serves as a benchmark of how easy it is to learn the language. 
As we will see the Python version is both short and readable:

```python
print("hello world!")
```

As the focus of this class is RevitPythonShell and pyRevit, we will start Revit and fire up the RevitPythonShell, 
which should be located under the Add-Ins tab. When we type or paste our hello world program into it, it should run 
there without any troubles:

![revit_python_shell_01.png](https://github.com/hdm-dt-fb/bilt_academy_2019/raw/master/Lab_4.1/img/revit_python_shell_01.png "Our first Python program, run in the RevitPythonShell.")

Congratulations! If you were not already, now you are a Python programmer.
We will run all our following little code blocks - called snippets - the same way by pasting it straight into the Shell*. 
While printing a simple static text to the console might seem not very exiting at first, it is a key feature, 
which enables us to get visibility what is going on in our program, and to provide feedback to the users of our script.

*If you do this example not in our lab, but on your own: I would highly recommend typing the code instead of pasting! 
You will stumble over all the important little unavoidable mistakes and at the same time get a better understanding of 
your code.  For the BILT Academy lab we have to resort to pasting in interest of time.


### Variables

In almost every program we would want to store information. We can do this by using variables. 
You can think of them as container with a label on it. The name of the variable is the text on the label. 
A variable can hold all kinds of data. To assign a value to a variable, or in our picture creating a container labelling 
and filling it with content, we use the single equals operator. Here are some examples:

```python
empty_variable = None
some_text = "Python"
single_full_number = 42
single_fractional_number = 3.41
list_of_numbers = [1, 2, 3, 0, -5, single_full_number]
```

Any time we are interested what value(s) (if any) a variable contains, we can use the same print function from above, 
for even multiple items at a time:

```python
print(empty_variable)
print(some_text, list_of_numbers)
```

### Loops

Whenever we store multiple things in one variable (called iterable) – like the multiple characters of “Python” 
text (called string) in variable some_text or all the numbers stored in our list_of_numbers – we can process the 
individual elements one by one.
This concept is called loop. An easy way to think of it, is an assembly line:
All the numbers of list_of_numbers get placed at the beginning of the assembly line, then they get processed one by one. 
In Python, you would write:


```python
for number in list_of_numbers:
    incremented_number = number + 1
    print(number, incremented_number)
print("loop finished")
```

The “for • in •••:” signals that this is a loop, where all elements of list_of_numbers are placed at the beginning of the 
assembly line. One after another - as it is each elements turn - the current element of the list is placed in the variable 
called number. This overwrites its previous content. All the code that is indented is processed each time a new element 
from the list is put into the variable number, so the current number and its incremented twin will get printed for each 
element in list_of_numbers.  Once we end the indentation, we are out of the loop, so the “loop finished” message gets 
printed only once.

### Conditionals
As we process data, we often want our code to take predefined decisions. These are called conditionals and offer a very simple yet flexible way to process some elements differently than others. The most simple and common conditional is the keyword “if”. 
It will – as the word already suggests – only run a block of indented code if its condition is met:


```python
if some_text == "Python":
    print(some_text + " is easy to learn!")
```

This reads almost like English text: Only if the variable some_text contains the text/string that exactly matches the 
text/string “Python”, it will actually execute the indented code. 
Often we want to react on different inputs in different ways. For this scenario it is possible to put many if conditions 
in a row. Whenever the conditions are mutually exclusive, we would use an “elif” (short form for “else if”) as alternative 
check and an “else” as a catchall.
For our list_of_numbers example we could check the numbers one by one in a loop and have the program logic react on the 
numbers with different print statements:

```python
for number in list_of_numbers:
    if number > 1:
        print(number, " greater than 1")
    elif number < 1:
        print(number, " smaller than 1")
    else:
        print(number, " it is 1!!")
```

Note that if the number is greater than 1 the checks for “elif” and “else” are not even executed.

And these are already all the Python basics we need for our first useful script. Of course there are a lot more things 
to know in Python, but in the interest of time, our basics for the lab are condensed to the absolute minimum we need 
for this class. 
I highly recommend extending your Python knowledge, there are countless books and videos, even games to learn Python, 
so depending on your preferred way of learning I would like to encourage you to explore further with the help of those.
