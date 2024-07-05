# UEVR_VRData

## Functions

### `is_runtime_ready()`

Returns true if the VR runtime is ready.

### `is_openvr()`

Returns true if the VR runtime is OpenVR.

### `is_openxr()`

Returns true if the VR runtime is OpenXR.

### `is_hmd_active()`

Returns true if the HMD is active. Usually meaning the headset is on and tracking.

### `get_standing_origin(out standing_origin: UEVR_Vector3f)`

Returns the standing origin of the HMD.

### `get_rotation_offset(out rotation_offset: UEVR_Vector3f)`

Returns the rotation offset of the HMD.

### `set_standing_origin(standing_origin: UEVR_Vector3f)`

Sets the standing origin of the HMD.

### `set_rotation_offset(rotation_offset: UEVR_Vector3f)`

Sets the rotation offset of the HMD.

### `get_hmd_index()`

Returns the index of the HMD.

### `get_left_controller_index()`

Returns the index of the left controller.

### `get_right_controller_index()`

Returns the index of the right controller.

### `get_pose(index: number, out position: UEVR_Vector3f, out rotation: UEVR_Quaternionf)`

Returns the pose of the specified device.

### `get_transform(index: number, out transform: UEVR_Transform)`

Returns the transform of the specified device.

### `get_eye_offset(index: number, out eye_offset: UEVR_Vector3f)`

Returns the eye offset of the specified eye.

### `get_ue_projection_matrix(index: number, out projection_matrix: UEVR_Matrix4f)`

Returns the projection matrix of the specified eye.

### `get_left_joystick_source()`

Returns the source handle of the left joystick.

### `get_right_joystick_source()`

Returns the source handle of the right joystick.

### `get_action_handle(action_name: string)`

Returns the handle of the specified action.

### `is_action_active(action_name: string)`

Returns true if the specified action is active.

### `get_joystick_axis(index: number, out axis: UEVR_Vector2f)`

Returns the axis of the specified joystick.

### `trigger_haptic_vibration(seconds_from_now: number, duration: number, frequency: number, amplitude: number, source_handle: number)`

Triggers haptic vibration on the specified device.

### `is_using_controllers()`

Returns true if the VR system is using controllers within the past 30 seconds.

### `get_lowest_xinput_index()`

### `recenter_view()`

Recenters the view.

### `recenter_horizon()`

Recenters the horizon.

### `get_aim_method()`

Returns the aim method as an integer.

### `set_aim_method(aim_method: number)`

Sets the aim method.

### `is_aim_allowed()`

Returns true if aiming is allowed.

### `set_aim_allowed(aim_allowed: bool)`

Sets whether aiming is allowed.

### `get_hmd_width()`

Returns the render width of the HMD.

### `get_hmd_height()`

Returns the render height of the HMD.

### `get_ui_width()`

Returns the render width of the UI.

### `get_ui_height()`

Returns the render height of the UI.

### `is_snap_turn_enabled()`

Returns true if snap turning is enabled.

### `set_snap_turn_enabled(snap_turn_enabled: bool)`

Sets whether snap turning is enabled.

### `set_decoupled_pitch_enabled(decoupled_pitch_enabled: bool)`

Sets whether decoupled pitch is enabled.

### `set_mod_value(name: string, value: string)`

Sets the value of the specified mod.

### `get_mod_value(name: string)`

Returns the value of the specified mod as a Lua string.

### `save_config()`

Saves the configuration.

### `reload_config()`

Reloads the configuration.

