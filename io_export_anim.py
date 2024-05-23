bl_info = {
    "name": "Export Camera Animation",
    "author": "ottle",
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

def write_anim(context, filepath, frame_start, frame_end):
    fw = open(filepath, 'w').write
    fw("object,frame,posx,posy,posz,scalex,scaley,scalez,roll,pitch,yaw\n")
    frame_range = range(frame_start, frame_end + 1)
    for obj in bpy.context.selected_objects:
        for f in frame_range:
            bpy.context.scene.frame_set(f)
            matrix = obj.matrix_world.copy()
            posx, posy, posz = matrix.to_translation()[:]
            scalex, scaley, scalez = matrix.to_scale()[:]
            roll, pitch, yaw = matrix.to_euler()[:]
            fw("%s, %d, %r, %r, %r, %r, %r, %r, %r, %r, %r\n"
                % (obj.name, f, posx,posy,posz, scalex,scaley,scalez, roll,pitch,yaw))

from bpy.props import StringProperty, IntProperty, BoolProperty
from bpy_extras.io_utils import ExportHelper


class AnimationExporter(bpy.types.Operator, ExportHelper):
    """Save selected object animations as a csv file."""
    bl_idname = "export_animation.objects"
    bl_label = "Animation"

    filename_ext = ".csv"
    filter_glob: StringProperty(default="*.csv", options={'HIDDEN'})

    frame_start: IntProperty(name="Start Frame",
            description="Start frame for export",
            default=1, min=1, max=300000)
    frame_end: IntProperty(name="End Frame",
            description="End frame for export",
            default=250, min=1, max=300000)

    def execute(self, context):
        write_anim(context, self.filepath, self.frame_start, self.frame_end)
        return {'FINISHED'}

    def invoke(self, context, event):
        self.frame_start = context.scene.frame_start
        self.frame_end = context.scene.frame_end

        wm = context.window_manager
        wm.fileselect_add(self)
        return {'RUNNING_MODAL'}


def menu_export(self, context):
    default_path = os.path.splitext(bpy.data.filepath)[0] + ".csv"
    self.layout.operator(AnimationExporter.bl_idname, text="Animation (.csv)")


def register():
    bpy.utils.register_class(AnimationExporter)
    bpy.types.TOPBAR_MT_file_export.append(menu_export)


def unregister():
    bpy.utils.unregister_class(AnimationExporter)
    bpy.types.TOPBAR_MT_file_export.remove(menu_export)


if __name__ == "__main__":
    register()
