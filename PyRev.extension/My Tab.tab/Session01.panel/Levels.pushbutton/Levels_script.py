import Autodesk
from Autodesk.Revit.DB import *

doc = __revit__.ActiveUIDocument.Document
c = 0.3048

t = Transaction(doc, 'grids')
t.Start()
# PC Level
pc_level = Level.Create(doc, -3.65/c)
# RC Level
rc_level = Level.Create(doc, -3.45/c)
# SOG Level
sog_level = Level.Create(doc, -2.05/c)
# First Level
first_level = Level.Create(doc, 0.750/c)

pc_level_name = pc_level.get_Parameter(BuiltInParameter.DATUM_TEXT)
rc_level_name = rc_level.get_Parameter(BuiltInParameter.DATUM_TEXT)
sog_level_name = sog_level.get_Parameter(BuiltInParameter.DATUM_TEXT)
first_level_name = first_level.get_Parameter(BuiltInParameter.DATUM_TEXT)

pc_level_name.Set('PC Level')
rc_level_name.Set('RC Level')
sog_level_name.Set('SOG Level')
first_level_name.Set('First Level')

t.Commit()
