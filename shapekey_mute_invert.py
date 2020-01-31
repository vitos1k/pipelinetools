import bpy


def main(context):
    for block in context.active_object.data.shape_keys.key_blocks:
        block.mute = not (block.mute)


class Object_OT_MuteShapeKeys(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.muteshapekeys"
    bl_label = "Mute Shapekeys for Object -  Operator"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        main(context)
        return {'FINISHED'}


def register():
    bpy.utils.register_class(Object_OT_MuteShapeKeys)


def unregister():
    bpy.utils.unregister_class(Object_OT_MuteShapeKeys)


if __name__ == "__main__":
    register()
