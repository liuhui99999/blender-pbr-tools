import bpy
def rename_objs(prefix="",suffix=""):
 for o in bpy.data.objects: o.name=prefix+o.name+suffix
 print("Done")
def rename_mats(prefix=""):
 for m in bpy.data.materials:
  if m.users>0: m.name=prefix+m.name
 print("Done")
print("Loaded")
