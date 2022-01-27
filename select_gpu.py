import bpy

def printout(devices):
    if (devices and len(devices)>0):
        print ("###################################################")
        print ("there are %i devices in %s" % (len(devices),devices[0].type))
        for i,dev in enumerate(devices):
            print("%i. %s" % (i,dev.name))
        print ("###################################################")

def enable_gpus(device_type,device_list):

    preferences = bpy.context.preferences
    cycles_preferences = preferences.addons["cycles"].preferences
    device_types = [dev[0] for dev in  cycles_preferences.get_device_types(bpy.context.scene)]
    current_type = cycles_preferences.compute_device_type
    if ((device_type == None) or (device_type not in device_types)):
          #IF OPTIX SELECTED THEN SEARCH ALL OPTIX DEVICES    
        all_devices = cycles_preferences.get_devices_for_type(current_type)
    else:
        all_devices = cycles_preferences.get_devices_for_type(device_type)
    printout(all_devices)
    activated_gpus = []
    for i,device in enumerate(all_devices):
        if (i in device_list):
            device.use = True
            activated_gpus.append(device.name)
        else:
            device.use = False

    cycles_preferences.compute_device_type = device_type
    for scene in bpy.data.scenes:
        scene.cycles.device = "GPU"

    return activated_gpus


#########################                        
dev_list = [0]
#########################

gpus = enable_gpus('OPTIX',dev_list)
print("Activated gpu's: ")
print(gpus)
