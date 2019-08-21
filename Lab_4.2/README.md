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
