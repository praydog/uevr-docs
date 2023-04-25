# UnrealVR: Blueprint API

UnrealVR implements some functions within the Unreal Engine's existing VR Blueprint API. These functions would usually do nothing because the VR plugins are not present. UnrealVR implements these functions so modders can easily access HMD and controller data without having to write a C++ plugin.

This should be more familiar to modders, and easier to use than the C++ API. Normal game developers should feel right at home as well.

At the moment, only confirmed to work perfectly on 4.27. More testing and development is needed to support other versions.

## Implemented functions

For more information on these functions, visit the [Unreal Engine documentation](https://docs.unrealengine.com/4.27/en-US/BlueprintAPI/Input/HeadMountedDisplay/)

### Head Mounted Display: Get Device Pose

This one only works for the HMD for now. Bit of a hacky implementation, but it works.

### Head Mounted Display: Get Motion Controller Data

Only works for left and right controller. 

`Valid`, `Aim Position`, `Aim Rotation`, `Grip Position`, `Grip Rotation` are implemented.

### Head Mounted Display: Get XRSystem Flags

Metadata used to inform blueprint about certain things.

```cpp
enum ECustomSystemFlags : int32_t {
    SYSTEMFLAG_NONE = 0,
    SYSTEMFLAG_HMD_ACTIVE = 1 << 0,
    SYSTEMFLAG_DECOUPLED_PITCH = 1 << 1,
    SYSTEMFLAG_OPENXR = 1 << 2,
    SYSTEMFLAG_OPENVR = 1 << 3,
    SYSTEMFLAG_MOTION_CONTROLLERS_ACTIVE = 1 << 4,
    SYSTEMFLAG_LEFT_THUMBREST_ACTIVE = 1 << 5,
    SYSTEMFLAG_RIGHT_THUMBREST_ACTIVE = 1 << 6,
};
```
