# pipelinetools
My tools i use in a production pipeline in a softwares such as blender/houdini/after effects

# • io_aftereffects_export_with_curves.py
    Addon for blender 2.8+  It exports cameras/empties/curves and lamps from blender  to after effects. 3d curves from blender
    are exported as 2d masks on 2d layers in camera space. Currently works only with regular cameras, panoramic support to be
    added later 

# • shapekey_mute_invert.py
    This script creates an Operator that inverts all the 'Mute' parameters of all shapekeys of the active object.
    To call that operator type "Mute Shapekeys for Object -  Operator" in a search menu. 
    Note: This operator would dissapear after you close blender instance. So make sure to launch script again
    
# • surface_follow_28.py
    This script is a port to 2.80 from this repository
    https://github.com/the3dadvantage/BlenderSurfaceFollow/blob/master/Surface%20Follow
    Before binding to surface you have to apply all transfroms
