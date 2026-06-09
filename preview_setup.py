import bpy
def preview_setup(name,out="preview.png"):
 for o in list(bpy.data.objects):
  if o.type in ("LIGHT","CAMERA"): bpy.data.objects.remove(o)
 bpy.ops.object.light_add(type="AREA",location=(2,-2,3))
 bpy.context.object.data.energy=200
 bpy.ops.mesh.primitive_plane_add(size=2)
 bpy.ops.object.camera_add(location=(1.5,-1.5,1.2))
 bpy.context.scene.camera=bpy.context.object
 bpy.context.scene.render.filepath=out
 bpy.ops.render.render(write_still=True)
 print("Rendered: "+out)
print("Loaded")
