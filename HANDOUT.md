# BILT Academy 2019 Coding in Python

Being able to interact with programs you work with, not only via the graphical user interface and built-in tools, 
but also programmatically, is sometimes regarded as magic or having a superpower. With this lab I want to spread this 
"magic" and have you acquire some this "superpower" as well.

Regarding the programming language choice of this lab: 
C# for scripting in Revit does make sense - since most examples out there on RevitAPI are C#. However we will be using 
Python.  It is one of the easiest to learn, most taught, and wide spread languages in the world today, with connections 
to countless domains. Due to its super clean syntax, it is not only fast and easy to learn and prototype with, but also 
very readable, making it great for sharing and easily modifiable. Luckily this great programming language can also be 
used within Revit, making the jump into programming within Revit a smaller step.

So get started with Python scripting in Revit today! 
Expand your capabilities from being just a consumer of Revit and Plugins, to become a creator of your own functionality 
add-ons. While many would agree that scripting can 
drastically enhance your interactions with models, sadly only few dive into it. 
With this lab we explore how simple it can actually be, to get started to write your own 
custom functions with Python in Revit.
We will learn which tools can support us in this process, going from model exploration and snippet testing in 
RevitPythonShell, to a real script that helps us with a tedious task and finally making it conveniently available 
(for you and your team) in pyRevit as a regular Revit ribbon bar button.
We start with a short interactive intro into Python and gradually start coding our very simple yet useful script, 
inspired by a real world use case we have @HdM.

Disclaimer: This is by no means a complete introduction into programming or Python! 
It tries to light a spark of fascination and teach enough to whet the appetite. As a follow-up, further learning is 
highly recommended. We will only discuss the simple concepts of programming that we need for our use case, as they 
already enable a vast amount of possibilities.


### Motivation

When looking at Python Revit scripts at our office, they can mostly be categorized into:

* Optimize existing workflows
* Access hidden features regular users do not get
* More thorough model inspection
* Connections to external tools
* Better content tracking

Today we will look at a simple script we use in production. It accesses hidden properties and optimizes a away rather 
tedious "workflow": 
In big projects with thousands of door instances, we usually have consultants involved for the door planning. 
One of the first things they would want to know is to which side a door would open to. 

To my knowledge, there is no built-in tool in Revit to cover this topic/task. The naive approach to "solve" this issue 
would be to have someone dedicated to check in plans to which side the door instances open to and write this information 
into a parameter.
Clearly this approach is not very sustainable. Not only is it very time consuming and would need to be re-run while 
modifying the model or before each upload/submission, but it is also prone to human errors.
Luckily the information, whether a door instance is Mirrored, is already stored in the Revit model database. 
It is just not visible to the regular GUI (Graphical User Interface) user.

This is where scripting comes to the rescue:
As we can find out with the Revit Lookup tool, there is a "Mirrored" property on each door. Equipped with this knowledge 
we will prepare our doors with the information of their default orientation.
With this setup we will be able to write a script that runs blazingly fast through even an enormous number of doors in 
almost no time. The only errors to be expected from this script run are the errors unexpected settings from the setup.


# Python basics

### Hello world
As any newcomer to a programming language or programming in general, we start with a common first little task: 
To write a little program called hello world, which does nothing else but showing/printing a “hello world!” text to the 
screen. For some people this even serves as a benchmark of how easy it is to learn the language. 
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



# Python in Revit

### Connect to Revit model elements

The simplest way to connect to Revit model elements is via selections. 
For this purpose let us open an empty project, draw a few walls place a few doors (preferably of different types) in them, 
select the doors and start the RevitPythonShell.
The selected elements are now conveniently available via a list of elements in the pre-populated variable “selection”, 
the first selected element under “s0”.

This enables a path for quick exploration. As a preview for later, you could type “s0.” and get an autocomplete helper, 
which shows you an impressive amount of built-in functionality already available for the object:

![revit_python_shell_02.png](https://github.com/hdm-dt-fb/bilt_academy_2019/raw/master/Lab_4.2/img/revit_python_shell_02.png "Connect to model elements in RevitPythonShell.")

Usually we would not want to force the users of our scripts to select the elements to be processed, if we can avoid it. 
For that scenario there is a so-called FilteredElementCollector available which gives access to model elements by their 
category or class. A simple one to access all door instances in current model would be:

```python
doors = FilteredElementCollector(doc).\
        OfCategory(BuiltInCategory.OST_Doors).\
        WhereElementIsNotElementType().ToElements()
```

This will store all door instances - but not the door types - of the current model in the variable “doors”. 
If we were interested in the in the door types instead, we could use “WhereElementIsElementType()” in place of 
“WhereElementIsNotElementType()”. If this filter is omitted, we would get types and instances.

As you can see this is quite a long statement. I prefer to shorten it with the help of import aliases:

```python
from Autodesk.Revit.DB import FilteredElementCollector as Fec
from Autodesk.Revit.DB import BuiltInCategory as Bic

doors = Fec(doc).OfCategory(Bic.OST_Doors).\
        WhereElementIsNotElementType().ToElements()
```

This makes the statement way more compact but requires the aliasing imports at the top of your script.

### Print element Ids from loop

Now that we got all doors, we can access one of the most useful information of the elements: The object Id. This may not be the most exiting element property, but an extremely useful one when it comes to understand why something in our script did not go according to plan. 
So let us loop over the elements and get each Id:

```python
for door in doors:
    print(15*"-")
    print(door.Id)
```

As you can see I added another print statement for a separation line at the start of each element we loop over. 
This helps us to read the information we will add together with the door Id.

### Read element instance properties and parameters

Since we process the individual doors one by one in our loop, we can start to have a look at their element properties 
and parameters – which is one of the most common tasks.
Properties and Parameters are similar, retrieving their values is different though. Properties are accessible 
directly – one example is the “.Mirrored” property mentioned earlier. 
The updated version of our loop with the property “Mirrored”:

```python
for door in doors:
    print(15*"-")
    print(door.Id)
    print(door.Mirrored)
```


For parameters we would use the “LookupParameter(“parameter_name”)” method.
But this only gives us back the parameter itself, not the stored parameter value. 
To retrieve the parameter value we need one more method call, which is dependent on the datatype the parameter value is 
stored. As we will access the door mark, which is stored as text/string the method we need to get the parameter value is 
“AsString()”:

![revit_python_shell_03.png](https://github.com/hdm-dt-fb/bilt_academy_2019/raw/master/Lab_4.2/img/revit_python_shell_03.png "Connect to model elements in RevitPythonShell.")

Our doors loop extended with the door mark:

```python
for door in doors:
    print(15*"-")
    print(door.Id)
    print(door.Mirrored)
    print(door.LookupParameter("Mark").AsString())
```

But how do you get to know all (or most of) these properties and parameters?
There is a great tool for that: [RevitLookup](https://github.com/jeremytammik/RevitLookup)
Please jump to the Tools & resources section to learn more about it

### Read element type parameters

Once we are able to read Instance parameters, we will certainly want to get access to the type parameters, too. 
There is a just a minor thing to be aware of:
In the RevitAPI the type of a Family is accessed by the property “Symbol”. From there the parameter value access is the 
same way as for the instances via  “LookupParameter(“type_parameter_name”)”:

![revit_python_shell_04.png](https://github.com/hdm-dt-fb/bilt_academy_2019/raw/master/Lab_4.2/img/revit_python_shell_04.png "Access door type parameter.")

In our loop this would look like this:

```python
for door in doors:
    print(15*"-")
    print(door.Id)
    print(door.Mirrored)
    print(door.LookupParameter("Mark").AsString())
    print(door.Symbol.LookupParameter("Type Name").AsString())
```


# Door hinges side script

### Create a TODO list of small steps micro tasks

Now we have enough tools and knowledge to write our first useful script. In fact we even did some of the required work 
for it in the steps above.
For our script we open the provided "door_hinges_start.py" in notepad++.
Please make sure you follow the according setup steps from the tools & resources section for notepad++.
Let us also open the provided Revit project "python_beginners_tower.rvt".
When starting or adjusting a script, it is good practice to quickly write down in plain English what the steps are, 
to get the script to run its task. 
When starting a line with the "#" Symbol it is regarded as a comment and Python will ignore it and not try to execute it:


```python
# TODO micro step 1 to get the script to work
# TODO micro step 2 to get the script to work
```

In our case this could be the following steps:

```python
# TODO loop over all doors (loops)
# TODO ask each door for its type (access family type)
# TODO get preset default_hinges_side door side (how to read parameter)
# TODO ask if door is mirrored or not (how to read property)
# TODO perform some logic to find the actual hinges side (conditionals)
# TODO write result to door instance (how to write to parameter)
```

A good location for these general comments and TODO lists would be right after the imports.

### Script start version

Content of "door_hinges_start.py":

```python
import clr
clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import BuiltInCategory as Bic
from Autodesk.Revit.DB import FilteredElementCollector as Fec
from Autodesk.Revit.DB import Transaction

# TODO micro steps to get the script to work

# reference to the current open revit model to work with:
doc = __revit__.ActiveUIDocument.Document

# parameter names to work with:
# these are just the parameter names 
# not the actual parameters or their values
family_hinges_side = "hinges_side_family"
instance_hinges_side = "hinges_side_instance"

# connect to Revit model elements via FilteredElementCollector
# collect all the doors
doors = Fec(doc).OfCategory(Bic.OST_Doors).WhereElementIsNotElementType().ToElements()

# entering a transaction to the modify revit model database
# Start transaction
tx = Transaction(doc, 'set door hinges side')
tx.Start()

# create main logic here..:
for door in doors:
    print(15*"-")
    print(door.Id)
    print("door is mirrored:", door.Mirrored)

# commit the changes to the model database
# End transaction
tx.Commit()
```

### Comment out code lines you want to disable temporarily

The "#" is not only useful for comments, but also to temporarily disable a line of code. That way we can find out if 
the script runs without the line we commented out.

Get the type parameter door hinges side
The script start version provides with a skeleton of the components we already learned. It collects the doors, prints 
their Ids in the loop and indicates if they are mirrored.
Now it is time to retrieve the family type in order to get to the parameter value with the default hinges side of the family:

```python
for door in doors:
    print(15*"-")
    print(door.Id)
    print("door is mirrored: ", door.Mirrored)
    door_type = door.Symbol
```

### Debugging type parameter access

If we try to access the value of the parameter "default_hinges_side" for each door: 

```python
for door in doors:
    print(15*"-")
    print(door.Id)
    print("door is mirrored: ", door.Mirrored)
    door_type = door.Symbol
    print(door_type.LookupParameter(family_hinges_side).AsString())
```

![revit_python_shell_05.png](https://github.com/hdm-dt-fb/bilt_academy_2019/raw/master/Lab_4.3/img/revit_python_shell_05.png "Error when trying to access door type parameter.")

Luckily the first line of the exception already gives a hint:
"'NoneType' object has no attribute 'AsString()'"
This basically means we cannot use .AsString() to get a parameter text value, if that object does not exist. 
But since we print each door Id before any other action, we know, that the last door Id we see is the Id of the door 
that gives us the error.

Debugging errors is part of coding and often enough the part where we can learn the most, so let us inspect how that 
door type looks like:
After selecting the door with its Id (Revit > Manage > Inquiry > Select by Id) we can see that the door is a 
double leaf door. This is probably also the reason the creator did not provide with a default hinges side. 
With this information we have to take a decision now:
* Expect the parameter to always be there and have our script fail when users load incompatible families
* Expect the parameter to not always be there and only process conforming doors

For this workshop we will accept, that there might be doors that do not comply. 
So we will check with a simple conditional if the parameter exists:

```python
for door in doors:
    print(15*"-")
    print(door.Id)
    print("door is mirrored: ", door.Mirrored)
    door_type = door.Symbol
    hinges_default_param = door_type.LookupParameter(family_hinges_side)
    if hinges_default_param:
        print("parameter exists")
    else:
        print("parameter missing!!") 
```

![revit_python_shell_06.png](https://github.com/hdm-dt-fb/bilt_academy_2019/raw/master/Lab_4.3/img/revit_python_shell_06.png "Door types with missing parameter.")

With this check in place, we can now safely access the parameter value where it exists, and warn the user where it is missing:

```python
for door in doors:
    print(35 * "-")
    print(door.Id)
    door_type = door.Symbol
    hinges_default_param = door_type.LookupParameter(family_hinges_side)
    if hinges_default_param:
        hinges_type_side = hinges_default_param.AsString()
        print("door default side: ", hinges_type_side)
    else:
        print("parameter missing!!")
```

### Get instance property door mirrored

Whenever we get the default hinges side information, we want to know if the door is mirrored, in order to tell if the 
door is a "lefty" or "righty":

```python
for door in doors:
    print(15*"-")
    print(door.Id)

    door_type = door.Symbol
    hinges_default_param = door_type.LookupParameter(family_hinges_side)

    if hinges_default_param:
        hinges_type_side = hinges_default_param.AsString()
        print("door default side: ", hinges_type_side)
        is_mirrored = door.Mirrored
        print("door is mirrored : ", is_mirrored)
    else:
        print("parameter missing!!")
```

![revit_python_shell_07.png](https://github.com/hdm-dt-fb/bilt_academy_2019/raw/master/Lab_4.3/img/revit_python_shell_07.png "Access to mirrored property.")

This is basically all the information we need. Now we only need to make our script to take the right decisions based on the input.

### Final decisions

We can assume two cases : Mirrored / not mirrored. 
The simpler case is not mirrored, as we can just use the default hinges side given by the family type. 
For the mirrored version we look into the parameter value of hinges_type_side and choose the opposite:

```python
for door in doors:
    print(15*"-")
    print(door.Id)

    door_type = door.Symbol
    hinges_default_param = door_type.LookupParameter(family_hinges_side)

    if hinges_default_param:
        hinges_type_side = hinges_default_param.AsString()
        print("door default side: ", hinges_type_side)

        is_mirrored = door.Mirrored

        if not is_mirrored:
            print("door is not mirrored.")
            print("instance is:", hinges_type_side)

        elif is_mirrored:
            print("door is mirrored.")
            if hinges_type_side == "L":
                print("instance is: R")
            elif hinges_type_side == "R":
                print("instance is: L")
    else:
        print("parameter missing!!")
```

### Write parameter values within a transaction

So far we did not change the model at all. But after checking the output of our script is correct, we would want to 
write the result to a parameter. This works very similarly to reading a parameter value, but we specify, that we want 
to set the value via: Set("parameter_value").
Whenever we want to modify data of our Revit model we need to put it inside the context of a database transaction. 
Our modifications to the model have to happen between the start and the commit of the transaction.
Find the final version of our script below:

Script final version
Content of "door_hinges_complete.py":

```python
"""
checks all doors and sets door hinge side.
this is the pyRevit documentation help text.
"""
import clr

clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import BuiltInCategory as Bic
from Autodesk.Revit.DB import FilteredElementCollector as Fec
from Autodesk.Revit.DB import Transaction

# DONE loop over all doors (loops)
# DONE ask each door for its type (access family type)
# DONE get preset default_hinges_side door side (how to read parameter)
# DONE ask if door is mirrored or not (how to read property)
# DONE perform some logic to find the actual hinges side (conditionals)
# DONE write result to door instance (how to write to parameter)

# __window__.set_font_sizes(19)  # set bigger font in RPS
# reference the current open revit model to work with:
doc = __revit__.ActiveUIDocument.Document

# parameter names to work with:
# these are just the names not the actual parameters or their values
family_hinges_side = "hinges_side_family"
instance_hinges_side = "hinges_side_instance"

# connect to Revit model elements via FilteredElementCollector
# collect all the doors
doors = Fec(doc).OfCategory(Bic.OST_Doors).WhereElementIsNotElementType().ToElements()

# entering a transaction to the modify revit model database
# Start transaction
tx = Transaction(doc, 'set door hinges side')
tx.Start()

# create main logic here..:
for door in doors:
    print(15*"-")
    print(door.Id)

    # ask each door for its type
    door_type = door.Symbol
    # get preset default_hinges_side door side
    hinges_default_param = door_type.LookupParameter(family_hinges_side)

    if hinges_default_param:
        hinges_type_side = hinges_default_param.AsString()
        print("door default side: ", hinges_type_side)

        # ask if door is mirrored or not
        is_mirrored = door.Mirrored

        # perform some logic to find the actual hinges side
        if not is_mirrored:
            door.LookupParameter(instance_hinges_side).Set(hinges_type_side)
            print("door is not mirrored.")
            print("instance is:", hinges_type_side) 

        elif is_mirrored:
            print("door is mirrored.")
            if hinges_type_side == "L":
                door.LookupParameter(instance_hinges_side).Set("R")
                print("instance is: R")
            elif hinges_type_side == "R":
                door.LookupParameter(instance_hinges_side).Set("L")
                print("instance is: L")
    else:
        print("parameter missing!!")

# commit the changes to the model database
# End transaction
tx.Commit()
print("successfully changed model")
```

### Turn script into pyRevit native Revit button

script changes are reflected without reload
Now that we have a fully functional script that we can paste into RevitPythonShell, we would like to share its 
functionality with our colleagues. At HdM we use pyRevit for that purpose. We can basically store our script with the 
right name in the right directory and get a native Revit button in return! 
For this workshop the named script and directories are already prepared:
You can drop the provided "BILT.extension" directory into the extensions directory of pyRevit. 
After a Revit restart or just a pyRevit reload you should see the new button created in your Revit ribbon bar. 
To create more custom pyRevit scripts just follow the logic of the directory structure and refer to the excellent 
pyRevit documentation.

![revit_python_shell_08.png](https://github.com/hdm-dt-fb/bilt_academy_2019/raw/master/Lab_4.3/img/revit_python_shell_08.png "Directory structure for a new pyRevit extension.")

![revit_python_shell_09.png](https://github.com/hdm-dt-fb/bilt_academy_2019/raw/master/Lab_4.3/img/revit_python_shell_09.png "New pyRevit extension integrated into Revit ribbon bar.")

Once the button is in place, any saved changes to the code will have effect next time the button is pressed, 
without any reloads or refreshes!

### Potential extensions of the script

Host wall information
As you might imagine we barely scratched the surface of what is possible. Dependent on your project’s needs, our script 
has the potential to be extended with quite some useful extra functionality. 
If you have a look at the properties of our door in RevitLookup you will find the interesting “Host” property, 
which gives us access to the wall the door is hosted by. This could be the starting point for functionality that
* queries for the wall material and 
writes it into a door parameter, 
or just checks for compatibility 
* aligns the workset of the door to the workset of the wall 
or sets them to a predefined one
* check fire ratings of the doors align with the wall rating
* check sound insulation ratings of the doors align with the wall rating

and many more.


## Tools & resources

### RevitLookup

As the open-source RevitLookup repository does not provide installers, you could either compile it yourself or find a 
pre-compiled version here:
[RevitLookup](https://revitcoaster.blogspot.com/2017/04/revit-lookup-2018.html)
and follow the instruction provided in the zip file. 
Once the Add-In is loaded in Revit, you could either get a listing of everything (takes quite some time on large models) 
or inspect a selected element or current view. Everything in bold font works like a link in a website.

### Notepad++

A good text/code editor can make quite the difference. For small scripts or to start coding I usually recommend Notepad++, 
as it is an open source editor, that comes with tons of good tools built in, nice Python Syntax highlighting, and is 
also available as portable version which does not require an Installation. A few recommended settings:

Tab settings (Settings > Preferences > Tab Settings: TabSize:4, Check Replace by space)
Syntax highlighting (Language > P > Python)

For larger I prefer pyCharm as IDE which give nice auto completion when IronPython stubs are loaded.

### RevitPythonShell

RevitPythonShell provides installers under their repository release section. Unfortunately with some of their installers, 
there seem to be no option to install it for all users. So if you are able to install it, but do not see it getting 
loaded under Add-Ins tab is the workaround that worked on our machines:
After a successful install there should be the directory:

`C:\Program Files (x86)\RevitPythonShell2018`

Now we would just need to copy over the following two things from the installing user with the admin privileges to the 
regular user, who will use the shell in Revit: 
* First copy the directory from:
`C:\Users\your_admin_username\AppData\Roaming\RevitPythonShell201X`
to:
`C:\Users\your_username\AppData\Roaming\RevitPythonShell201X`
* Then copy the actual addin file from:
`C:\Users\f.beaupere\AppData\Roaming\Autodesk\Revit\Addins\201X\RevitPythonShell201X.addin`
to:
`C:\Users\your_username\AppData\Roaming\Autodesk\Revit\Addins\201X\RevitPythonShell201X.addin`

Make sure to adjust your username and Revit version you want to install the plugin for, in the paths above. The you 
should be good to go.

### Links

[RevitPythonShell](https://github.com/architecture-building-systems/revitpythonshell)

[RevitLookup](https://github.com/jeremytammik/RevitLookup)

[pyRevit](https://github.com/eirannejad/pyRevit)

[revitapidocs](http://www.revitapidocs.com/)

[Notepad++](https://notepad-plus-plus.org/)

