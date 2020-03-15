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
# • select_gpu.py
    Script to use with blender commandline arguments, to select proper GPU's to render with
    usually usage would be something like blender -b filename.blend -p select_gpu.py
    But before that, you should edit  highlighte line in the script, where you can choose which gpu's to enable:
    dev_list = [0,1,2]
# • restart_blen_on_crash.bat
    This windows batch file will restart blender every time blender shuts off. 
    Be ready to kill your batch file via task manager. 
    Also note: you should specify in blend file not to overwrite render results, so after
    restart your blender would continue render from last frame. And wouldn't redo all the
    stuff from the begining
# • invert_seams.py
    This script is for blender2.8x , inverts Seams/OR/Sharp tag for selected edges. Type InvertPopup into Search,
    to call an operator. After that you can add to qucik favs individual operators from
    popup menu Just by rightclicking on them
