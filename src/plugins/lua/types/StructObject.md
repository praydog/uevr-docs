# StructObject

StructObject is a custom UEVR Lua type that represents a struct in Unreal Engine. It's for non-UObject based structs which support reflection.

## Functions

### `StructObject.new(struct: UEVR_UStruct*)`

Constructs a new StructObject from a UEVR_UStruct pointer.

### `StructObject.new(object: UEVR_UObject*)`

Constructs a new StructObject from a UEVR_UObject pointer, if the object inherits from UStruct.

### `obj:get_address()`

Returns the memory address of the struct as a number.

### `obj:get_struct()`

Returns the [UEVR_UStruct](UStruct.md) descriptor for this struct.

### `obj:get_property(name: string)`

Returns the value of the specified property by name.

### `obj:set_property(name: string, value: any)`

Sets the value of the specified property by name.

### `obj:read_qword()`
### `obj:read_dword()`
### `obj:read_word()`
### `obj:read_byte()`
### `obj:read_float()`
### `obj:read_double()`

Reads a value of the specified type from the struct at the current offset.

### `obj:write_qword(value)`
### `obj:write_dword(value)`
### `obj:write_word(value)`
### `obj:write_byte(value)`
### `obj:write_float(value)`
### `obj:write_double(value)`

Writes a value of the specified type to the struct at the current offset.

### `obj[name]` (metamethod)

Equivalent to `obj:get_property(name)`. Allows table-like access to properties.

### `obj[name] = value` (metamethod)

Equivalent to `obj:set_property(name, value)`. Allows table-like assignment to properties.