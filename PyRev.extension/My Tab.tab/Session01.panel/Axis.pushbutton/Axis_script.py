import Autodesk
import Autodesk.Revit.DB as DB
from Autodesk.Revit.DB import *


doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument
c = 0.3048
# declaring points
# Horizontal Axis
# Axe 1
p_1 = XYZ(0, 0, 0)
p_2 = XYZ(20/c, 0, 0)
line_1 = Line.CreateBound(p_1, p_2)

# Axe 2
p_3 = XYZ(0, -3.50/c, 0)
p_4 = XYZ(20/c, -3.50/c, 0)
line_2 = Line.CreateBound(p_3, p_4)

# Axe 3
p_5 = XYZ(0, -6.23/c, 0)
p_6 = XYZ(20/c, -6.23/c, 0)
line_3 = Line.CreateBound(p_5, p_6)

# Vertical Axis
# Axe A
p_7 = XYZ(2/c, 2/c, 0)
p_8 = XYZ(2/c, -10/c, 0)
line_A = Line.CreateBound(p_7, p_8)

# Axe B
p_9 = XYZ(5.18/c, 2/c, 0)
p_10 = XYZ(5.18/c, -10/c, 0)
line_B = Line.CreateBound(p_9, p_10)

# Axe C
p_11 = XYZ(8.43/c, 2/c, 0)
p_12 = XYZ(8.43/c, -10/c, 0)
line_C = Line.CreateBound(p_11, p_12)

# Axe D
p_13 = XYZ(10.93/c, 2/c, 0)
p_14 = XYZ(10.93/c, -10/c, 0)
line_D = Line.CreateBound(p_13, p_14)

# Axe E
p_15 = XYZ(12.93/c, 2/c, 0)
p_16 = XYZ(12.93/c, -10/c, 0)
line_E = Line.CreateBound(p_15, p_16)

# Axe F
p_17 = XYZ(16.28/c, 2/c, 0)
p_18 = XYZ(16.28/c, -10/c, 0)
line_F = Line.CreateBound(p_17, p_18)


t = Transaction(doc, 'grids')
t.Start()
# create grids
# Horizontal Axis
axe_1 = Grid.Create(doc, line_1)
axe_2 = Grid.Create(doc, line_2)
axe_3 = Grid.Create(doc, line_3)

# Vertical Axis
axe_A = Grid.Create(doc, line_A)
axe_B = Grid.Create(doc, line_B)
axe_C = Grid.Create(doc, line_C)
axe_D = Grid.Create(doc, line_D)
axe_E = Grid.Create(doc, line_E)
axe_F = Grid.Create(doc, line_F)

# Horizontal Axis
axe_1_name = axe_1.get_Parameter(BuiltInParameter.DATUM_TEXT)
axe_2_name = axe_2.get_Parameter(BuiltInParameter.DATUM_TEXT)
axe_3_name = axe_3.get_Parameter(BuiltInParameter.DATUM_TEXT)

# Vertical Axis
axe_A_name = axe_A.get_Parameter(BuiltInParameter.DATUM_TEXT)
axe_B_name = axe_B.get_Parameter(BuiltInParameter.DATUM_TEXT)
axe_C_name = axe_C.get_Parameter(BuiltInParameter.DATUM_TEXT)
axe_D_name = axe_D.get_Parameter(BuiltInParameter.DATUM_TEXT)
axe_E_name = axe_E.get_Parameter(BuiltInParameter.DATUM_TEXT)
axe_F_name = axe_F.get_Parameter(BuiltInParameter.DATUM_TEXT)

axe_1_name.Set('1')
axe_2_name.Set('2')
axe_3_name.Set('3')

# Vertical Axis
axe_A_name.Set('A')
axe_B_name.Set('B')
axe_C_name.Set('C')
axe_D_name.Set('D')
axe_E_name.Set('E')
axe_F_name.Set('F')

# try filteredelementcollector
# TODO: condition with Transaction (commit or RollBack) - if the axe is exist rollback
# if not create it

#axis_filter = DB.FilteredElementCollector(doc).OfCategory(DB.BuiltInCategory.OST_Grids)\
        #        .WhereElementIsNotElementType().ToElements()

#for axe in axis_filter:
    #print(axe.Name)

t.Commit()
