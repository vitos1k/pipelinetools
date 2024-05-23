import bpy

def convert_to_quaternion(obj, scn):
        quats = []        
        for fr in range(scn.frame_start,scn.frame_end,scn.frame_step):
            scn.frame_set(fr)
            quat = obj.matrix_world.to_quaternion()
            quats.append(quat)
        for i,fr in enumerate(range(scn.frame_start,scn.frame_end,scn.frame_step)):
            obj.rotation_quaternion = quats[i]
            obj.keyframe_insert('rotation_quaternion',frame = fr)
        obj.rotation_mode = 'QUATERNION'

#
#

scn = bpy.context.scene
obj = bpy.context.active_object
convert_to_quaternion(obj,scn)
