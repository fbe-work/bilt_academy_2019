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
default_hinges_side = "Aufschlagrichtung_Family"
din = "Aufschlagrichtung_DIN"

# connect to Revit model elements via FilteredElementCollector
# collect all the doors (works the same way with other categories: e.g: walls: Bic.OST_Walls)
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
    hinges_default_param = door_type.LookupParameter(default_hinges_side)

    if hinges_default_param:
        door_type_default_side = hinges_default_param.AsString()
        print("door default side: ", door_type_default_side)

        # ask if door is mirrored or not
        is_mirrored = door.Mirrored

        # perform some logic to find the actual hinges side
        if not is_mirrored:
            door.LookupParameter(din).Set(door_type_default_side)
            print("door is not mirrored.")
            print("instance is:", door_type_default_side)

        elif is_mirrored:
            print("door is mirrored.")
            if door_type_default_side == "L":
                door.LookupParameter(din).Set("R")
                print("instance is: R")
            elif door_type_default_side == "R":
                door.LookupParameter(din).Set("L")
                print("instance is: L")
    else:
        print("parameter missing")

# commit the changes to the model database
# End transaction
tx.Commit()
print("successfully changed model")
