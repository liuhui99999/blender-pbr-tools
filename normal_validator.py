import bpy
def check(mat_name):
 mat=bpy.data.materials.get(mat_name)
 if not mat: return
 for n in mat.node_tree.nodes:
  if n.type=="NORMAL_MAP":
   for i in n.inputs:
    if i.is_linked:
     tex=i.links[0].from_node
     if tex.type=="TEX_IMAGE" and tex.image:
      cs=tex.image.colorspace_settings.name
      if cs!="Non-Color": print("Issue: should be Non-Color")
 print("Checked")
print("Loaded")
