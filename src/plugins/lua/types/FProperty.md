# UEVR_FProperty

Represents a property in Unreal Engine. Inherits from [UEVR_FField](FField.md).

## Functions

### `property:get_offset()`

Returns the byte offset of the property within its parent struct.

### `property:get_property_flags()`

Returns the property flags as a bitfield.

### `property:is_param()`

Returns true if the property is a function parameter.

### `property:is_out_param()`

Returns true if the property is an out parameter.

### `property:is_return_param()`

Returns true if the property is a return value parameter.

### `property:is_reference_param()`

Returns true if the property is passed by reference.

### `property:is_pod()`

Returns true if the property is a plain old data type (no garbage collection).
