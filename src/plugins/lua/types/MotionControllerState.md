# UEVR_MotionControllerState

## Functions

### `state:set_rotation_offset(offset: variant)`

Sets the rotation offset of the motion controller state.

`offset` can be a `UEVR_Quaternionf`, a `Vector4f`, or a `Vector3d`.

### `state:set_location_offset(offset: variant)`

Sets the location offset of the motion controller state.

`offset` can be a `UEVR_Vector3f`, a `Vector3f`, or a `Vector3d`.

### `state:set_hand(hand: int)`

Sets the hand of the motion controller state.

`hand` can be `0` for left hand or `1` for right hand, or `2` for the HMD.

### `state:set_permanant(permanent: bool)`

Sets the permanant flag of the motion controller state. Permanent meaning UObjectHook will not reset the rotation or location at the end of the tick.