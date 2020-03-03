import bpy


def enable_gpus(device_type,device_list):
    preferences = bpy.context.preferences
    cycles_preferences = preferences.addons["cycles"].preferences
    cuda_devices, opencl_devices = cycles_preferences.get_devices()

    if device_type == "CUDA":
        devices = cuda_devices
    elif device_type == "OPENCL":
        devices = opencl_devices
    else:
        raise RuntimeError("Unsupported device type")

    activated_gpus = []

    for i,device in enumerate(devices):
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
dev_list = [0,1,2]
#########################

gpus = enable_gpus("CUDA",dev_list)
print("Activated gpu's: ")
print(gpus)
