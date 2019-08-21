from Autodesk.Revit.DB import FilteredElementCollector as Fec
from Autodesk.Revit.DB import BuiltInCategory as Bic

# show all elements in current selection
print(selection)

# show first element in current selection
print(s0)

# retrieve all door instances
doors = FilteredElementCollector(doc).\
        OfCategory(BuiltInCategory.OST_Doors).\
        WhereElementIsNotElementType().ToElements()

# retrieve all door instances via aliased collector
doors = Fec(doc).OfCategory(Bic.OST_Doors).\
        WhereElementIsNotElementType().ToElements()

# show door ids
for door in doors:
    print(15*"-")
    print(door.Id)

# access door instance properties
for door in doors:
    print(15*"-")
    print(door.Id)
    print(door.Mirrored)

# access door instance parameters
for door in doors:
    print(15*"-")
    print(door.Id)
    print(door.Mirrored)
    print(door.LookupParameter("Mark").AsString())

# access door type parameters
for door in doors:
    print(15*"-")
    print(door.Id)
    print(door.Mirrored)
    print(door.LookupParameter("Mark").AsString())
    print(door.Symbol.LookupParameter("Type Name").AsString())

