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
