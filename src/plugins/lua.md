# UnrealVR: Lua API

UnrealVR provides a Lua API that can be used to create plugins. This API is a wrapper around the C++ API, and is intended to be used by plugins written in Lua.

It is intended to be used within UE4SS, but can technically be used in any Lua environment.

This API is in its infancy, and is subject to change.

## Example

```lua
local LuaVR = require("LuaVR")

local function vr_print(text)
    print("[LuaVR Script] " .. text .. "\n")
end

local params = LuaVR.params
local callbacks = params.sdk.callbacks

local total_t = 0.0

-- Example usage of callbacks
callbacks.on_pre_engine_tick(function(engine, delta)
    total_t = total_t + delta
end)

-- Modifies the camera position
callbacks.on_post_calculate_stereo_view_offset(function(device, view_index, world_to_meters, position, rotation, is_double)
    position.z = position.z + 100.0
    position.y = position.y - 100.0
end)



-- UEVR_PluginInitializeParam

-- UEVR_PluginVersion
vr_print("Major: " .. tostring(params.version.major))
vr_print("Minor: " .. tostring(params.version.minor))
vr_print("Patch: " .. tostring(params.version.patch))

-- UEVR_PluginFunctions
vr_print("Is drawing ui: " .. tostring(params.functions.is_drawing_ui()))
params.functions.log_info("Hello from LuaVR!")
params.functions.log_warn("Hello from LuaVR!")
params.functions.log_error("Hello from LuaVR!")

-- UEVR_VRData
vr_print("Runtime ready state: " .. tostring(params.vr.is_runtime_ready()))
vr_print("Is OpenVR: " .. tostring(params.vr.is_openvr()))
vr_print("Is OpenXR: " .. tostring(params.vr.is_openxr()))
vr_print("Is HMD Active: " .. tostring(params.vr.is_hmd_active()))

local standing_origin = UEVR_Vector3f.new()
params.vr.get_standing_origin(standing_origin)
vr_print("Standing Origin: " .. tostring(standing_origin.x) .. ", " .. tostring(standing_origin.y) .. ", " .. tostring(standing_origin.z))

local rotation_offset = UEVR_Vector3f.new()
params.vr.get_rotation_offset(rotation_offset)
vr_print("Rotation Offset: " .. tostring(rotation_offset.x) .. ", " .. tostring(rotation_offset.y) .. ", " .. tostring(rotation_offset.z))

local hmd_index = params.vr.get_hmd_index()
vr_print("HMD Index: " .. tostring(hmd_index))

local left_controller_index = params.vr.get_left_controller_index()
vr_print("Left Controller Index: " .. tostring(left_controller_index))

local right_controller_index = params.vr.get_right_controller_index()
vr_print("Right Controller Index: " .. tostring(right_controller_index))

local hmd_position = UEVR_Vector3f.new()
local hmd_rotation = UEVR_Quaternionf.new()
params.vr.get_pose(hmd_index, hmd_position, hmd_rotation)

vr_print("HMD Position: " .. tostring(hmd_position.x) .. ", " .. tostring(hmd_position.y) .. ", " .. tostring(hmd_position.z))
vr_print("HMD Rotation: " .. tostring(hmd_rotation.x) .. ", " .. tostring(hmd_rotation.y) .. ", " .. tostring(hmd_rotation.z) .. ", " .. tostring(hmd_rotation.w))

if left_controller_index ~= -1 then
    local left_controller_position = UEVR_Vector3f.new()
    local left_controller_rotation = UEVR_Quaternionf.new()
    params.vr.get_pose(left_controller_index, left_controller_position, left_controller_rotation)

    vr_print("Left Controller Position: " .. tostring(left_controller_position.x) .. ", " .. tostring(left_controller_position.y) .. ", " .. tostring(left_controller_position.z))
    vr_print("Left Controller Rotation: " .. tostring(left_controller_rotation.x) .. ", " .. tostring(left_controller_rotation.y) .. ", " .. tostring(left_controller_rotation.z) .. ", " .. tostring(left_controller_rotation.w))        
end

if right_controller_index ~= -1 then
    local right_controller_position = UEVR_Vector3f.new()
    local right_controller_rotation = UEVR_Quaternionf.new()
    params.vr.get_pose(right_controller_index, right_controller_position, right_controller_rotation)

    vr_print("Right Controller Position: " .. tostring(right_controller_position.x) .. ", " .. tostring(right_controller_position.y) .. ", " .. tostring(right_controller_position.z))
    vr_print("Right Controller Rotation: " .. tostring(right_controller_rotation.x) .. ", " .. tostring(right_controller_rotation.y) .. ", " .. tostring(right_controller_rotation.z) .. ", " .. tostring(right_controller_rotation.w))        
end

local left_eye_offset = UEVR_Vector3f.new()
local right_eye_offset = UEVR_Vector3f.new()

params.vr.get_eye_offset(0, left_eye_offset)
params.vr.get_eye_offset(1, right_eye_offset)

vr_print("Left Eye Offset: " .. tostring(left_eye_offset.x) .. ", " .. tostring(left_eye_offset.y) .. ", " .. tostring(left_eye_offset.z))
vr_print("Right Eye Offset: " .. tostring(right_eye_offset.x) .. ", " .. tostring(right_eye_offset.y) .. ", " .. tostring(right_eye_offset.z))

local is_using_controllers = params.vr.is_using_controllers()
vr_print("Is Using Controllers: " .. tostring(is_using_controllers))
```