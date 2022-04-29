import arcpy
import os

#Definicje
def print_message(is_ARCGIS=True, message='Wiadomosc'):
    if is_ARCGIS:
        arcpy.AddMessage(message)
    else:
        print(message)


def get_parameters(is_ARCGIS=True):
    if is_ARCGIS:
        p1 = int(arcpy.GetParameterAsText(0))
    else:
        p1 = 10
    return p1

#Static
arcpy.env.workspace= r'C:\GIK2\Semestr1\PPG\first_arcpy\Polska.gdb'
#Dynamic
#layerString = arcpy.GetParameterAsText(0)
desc = arcpy.Describe(arcpy.env.workspace)

#Printuje imie i nazwisko
def imie_nazwisko (name, last_name):
    print(name + " " + last_name)

name = 'Patrycja'
last_name = 'Bibro'

imie_nazwisko(name, last_name)

# Print selected layer and describe object properties
print("Name: {}".format(desc.name))
if hasattr(desc, "layer"):
    print("Layer name: {}".format(desc.layer.name))
    print("Layer data source: {}".format(desc.layer.catalogPath))
else:
    print("Layer name: {}".format(desc.name))
    print("Layer data source: {}".format(desc.catalogPath))

# Print workspace properties
print "%-24s %s" % ("Connection String:", desc.connectionString)
print "%-24s %s" % ("WorkspaceFactoryProgID:", desc.workspaceFactoryProgID)
print "%-24s %s" % ("Workspace Type:", desc.workspaceType)

# Print Connection properties
cp = desc.connectionProperties
print "\nDatabase Connection Properties:"
print "%-12s %s" % ("Database:", cp.database)

#Get top-level feature classes
featureclasses = arcpy.ListFeatureClasses()
rasters = arcpy.ListRasters()

print(" ")
print("Feature classes: ")

for fc in featureclasses:
    print(fc)

for r in rasters:
    print(r)

print(" ")
print('Feature classes shape type:')

for fc in featureclasses:
    descfc = arcpy.Describe(fc)
    print(fc + " - " + descfc.shapeType)
    print("Dataset Type: {0}".format(descfc.datasetType))
    print("Extent:\n  XMin: {0}, XMax: {1}, YMin: {2}, YMax: {3}".format(
        descfc.extent.XMin, descfc.extent.XMax, descfc.extent.YMin, descfc.extent.YMax))

print(" ")

for r in rasters:
    descr = arcpy.Describe(r)
    print(r + " " + descr.dataType)
    print(r + "Compression type: " + descr.compressionType)
    print("Dataset Type: {0}".format(descr.datasetType))
    print("Extent:\n  XMin: {0}, XMax: {1}, YMin: {2}, YMax: {3}".format(
        descr.extent.XMin, descr.extent.XMax, descr.extent.YMin, descr.extent.YMax))



