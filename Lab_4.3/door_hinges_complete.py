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
# DONE get preset family_hinges_side door side (how to read parameter)
# DONE ask if door is mirrored or not (how to read property)
# DONE perform some logic to find the actual hinges side (conditionals)
# DONE write result to door instance (how to write to parameter)

# reference the current open revit model to work with:
doc = __revit__.ActiveUIDocument.Document

# parameter names to work with:
# these are just the names not the actual parameters or their values
family_hinges_side = "hinges_side_family"
instance_hinges_side = "hinges_side_instance"

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
    # get preset family_hinges_side door side
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
        print("parameter missing")

# commit the changes to the model database
# End transaction
tx.Commit()
print("successfully changed model")
