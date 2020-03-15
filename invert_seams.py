bl_info = {
    "name": "Invert Popup Seams/Sharp",
    "author": "vitos1k https://github.com/vitos1k/pipelinetools",
    "version": (1, 1),
    "blender": (2, 80, 0),
    "location": "Search menu -> Invert Popup",
    "description": "Shows popup menu in edit mode to invert selected seam and sharp edges",    
    "wiki_url": "",
    "category": 'MESH'}

import bpy,bmesh

def draw_popup(self, context):
    col = self.layout.column()
    row = col.row()
    if bpy.context.mode == 'EDIT_MESH':
        row.label(text = "Be good")
        row = col.row()
        row.operator("mesh.invert_seam_selected",text = "Invert Seams")
        row = col.row()
        row.operator("mesh.invert_sharp_selected",text = "Invert Sharp")
    else:
        row.label(text = "Works only in EDIT mode")
    

class MESH_OT_invertpopup(bpy.types.Operator):
    bl_idname = "mesh.invert_seam_sharp_menu"
    bl_label = "InvertPopup"

    def invoke(self, context, event):
        context.window_manager.popup_menu(draw_popup, title='Invert Menu', icon='INFO')
        return {'FINISHED'}

class MESH_OT_InvertSeam(bpy.types.Operator):
    '''Bind To Surface'''
    bl_idname = "mesh.invert_seam_selected"
    bl_label = "Invert selected seams"
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        if bpy.context.mode != 'EDIT_MESH':
            return {'CANCELLED'}
        obj = context.active_object
        me = obj.data
        bm = bmesh.from_edit_mesh(me)
        selected = [edge for edge in bm.edges if edge.select]
        for edge in selected:
            edge.seam = not edge.seam
        bmesh.update_edit_mesh(me)
        return {'FINISHED'}

class MESH_OT_InvertSharp(bpy.types.Operator):
    '''Bind To Surface'''
    bl_idname = "mesh.invert_sharp_selected"
    bl_label = "Invert selected sharp edges"
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        if bpy.context.mode != 'EDIT_MESH':
            return {'CANCELLED'}
        obj = context.active_object
        me = obj.data
        bm = bmesh.from_edit_mesh(me)
        selected = [edge for edge in bm.edges if edge.select]
        for edge in selected:
            edge.smooth = not edge.smooth
        bmesh.update_edit_mesh(me)
        return {'FINISHED'}


classes = (MESH_OT_invertpopup,MESH_OT_InvertSeam,MESH_OT_InvertSharp,)

def register():    
    for cls in classes:
        bpy.utils.register_class(cls)    

def unregister():    
    for cls in classes:
        bpy.utils.unregister_class(cls)    

if __name__ == "__main__":
    register()