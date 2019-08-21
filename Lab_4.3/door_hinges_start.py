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
    print("door is mirrored: ", door.Mirrored)

# commit the changes to the model database
# End transaction
tx.Commit()
