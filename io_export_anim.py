bl_info = {
    "name": "Export Camera Animation to CSV [IFSRenderer]",
    "author": "ottle,vitos1k",
    "version": (0, 1),
    "blender": (2, 80, 0),
    "location": "File > Export > Animation (.csv)",
    "description": "Export Animation (.csv)",
    "warning": "",
    "wiki_url": "",
    "support": 'COMMUNITY',
    "category": "Import-Export",
}

import os
import bpy
from mathutils import Matrix
def write_anim(context, filepath, frame_start, frame_end,loc,rot,scale,inc_name):
    fw = open(filepath, 'w').write
    word = ""
    if inc_name:
        word += "name"
    if loc:
        if word!="":
            word +=",locx,locy,locz"
        else:
            word +="locx,locy,locz"
    if rot:
        if word!="":
            word +=",rotx,roty,rotz"
        else:
            word +="rotx,roty,rotz"        
    if scale:
        if word!="":
            word +=",scalex,scaley,scalez"
        else:
            word +="scalex,scaley,scalez"
    fw(word)
    fw("\n")

    frame_range = range(frame_start, frame_end + 1)
    mToggle_YZ = Matrix(((1.0, 0.0, 0.0, 0.0),(0.0, 0.0, 1.0, 0.0),(0.0, 1.0, 0.0, 0.0),(0.0, 0.0, 0.0, 1.0)))
    for obj in bpy.context.selected_objects:
        for f in frame_range:
            word = ""
            bpy.context.scene.frame_set(f)
            matrix = obj.matrix_world.copy()            
            matrix2 = mToggle_YZ @ matrix @ mToggle_YZ.inverted()
            posx, posy, posz = matrix2.to_translation()[:]
            scalex, scaley, scalez = matrix2.to_scale()[:]
            rotw, rotx, roty, rotz  = matrix2.to_quaternion()[:]
            if inc_name:
                word += "%s" % obj.name
            if loc:
                if word!="":
                    word +=","
                word +="%r,%r,%r" % (posx,posy,posz)
            if rot:
                if word!="":
                    word +=","
                word +="%r,%r,%r,%r" % (rotw,rotx,roty,rotz)
            if scale:
                if word!="":
                    word +=","
                word +="%r,%r,%r" % (scalex, scaley, scalez)
            fw(word)
            fw("\n")

from bpy.props import StringProperty, IntProperty, BoolProperty
from bpy_extras.io_utils import ExportHelper


class AnimationExporter(bpy.types.Operator, ExportHelper):
    """Save selected object animations as a csv file."""
    bl_idname = "export_animation.objects"
    bl_label = "Animation IFS"

    filename_ext = ".csv"
    filter_glob: StringProperty(default="*.csv", options={'HIDDEN'})

    frame_start: IntProperty(name="Start Frame",
            description="Start frame for export",
            default=1, min=1, max=300000)
    frame_end: IntProperty(name="End Frame",
            description="End frame for export",
            default=250, min=1, max=300000)
    loc: BoolProperty(name="Include Location",default = True)
    rot: BoolProperty(name="Include Rotation",default = True)
    scale: BoolProperty(name="Include Scale",default = True)
    inc_name: BoolProperty(name="Include Name",default = True)
    def execute(self, context):
        write_anim(context, self.filepath, self.frame_start, self.frame_end, self.loc, self.rot, self.scale, self.inc_name)
        return {'FINISHED'}

    def invoke(self, context, event):
        self.frame_start = context.scene.frame_start
        self.frame_end = context.scene.frame_end

        wm = context.window_manager
        wm.fileselect_add(self)
        return {'RUNNING_MODAL'}


def menu_export(self, context):
    default_path = os.path.splitext(bpy.data.filepath)[0] + ".csv"
    self.layout.operator(AnimationExporter.bl_idname, text="Animation IFS (.csv)")


def register():
    bpy.utils.register_class(AnimationExporter)
    bpy.types.TOPBAR_MT_file_export.append(menu_export)


def unregister():
    bpy.utils.unregister_class(AnimationExporter)
    bpy.types.TOPBAR_MT_file_export.remove(menu_export)


if __name__ == "__main__":
    register()
