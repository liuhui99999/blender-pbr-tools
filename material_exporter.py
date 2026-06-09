import bpy,os,shutil
def export_mat(name,out_dir):
 mat=bpy.data.materials.get(name)
 if not mat: return
 os.makedirs(out_dir,exist_ok=True)
 if mat.use_nodes:
  for n in mat.node_tree.nodes:
   if n.type=="TEX_IMAGE" and n.image:
    src=bpy.path.abspath(n.image.filepath)
    if os.path.exists(src): shutil.copy2(src,os.path.join(out_dir,os.path.basename(src)))
 print("Exported")
print("Loaded")
