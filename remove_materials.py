import bpy
obj = bpy.context.active_object
if obj.type == 'MESH':
    slots = len(obj.material_slots)
    bpy.context.active_object.pass_index = 0
    if slots>0:
        for i in range(slots):
            bpy.ops.object.material_slot_remove()
