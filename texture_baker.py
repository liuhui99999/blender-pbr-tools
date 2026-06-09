import bpy
def bake_diffuse(obj_name,output,res=2048):
 obj=bpy.data.objects.get(obj_name)
 if not obj: return
 img=bpy.data.images.new("bake",res,res)
 bpy.context.view_layer.objects.active=obj
 bpy.ops.object.mode_set(mode="EDIT")
 bpy.ops.mesh.select_all(action="SELECT")
 bpy.ops.object.mode_set(mode="OBJECT")
 bpy.ops.object.bake(type="DIFFUSE")
 img.save_render(output)
 print("Baked: "+output)
print("Loaded")
