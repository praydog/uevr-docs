# C Wrapper Types

These are C++ wrapper classes provided by `include/uevr/API.hpp`. They wrap the C API handles and provide a more ergonomic interface.

## UObject

Base class for all Unreal Engine objects.

### Methods

- `UClass* get_class() const`
- `UObject* get_outer() const`
- `bool is_a(UClass* klass) const`
- `void process_event(UFunction* function, void* params)`
- `void call_function(std::wstring_view name, void* params)`
- `FName* get_fname() const`
- `std::wstring get_full_name() const`
- `template<typename T> T* get_property_data(std::wstring_view name) const`
- `bool get_bool_property(std::wstring_view name) const`
- `void set_bool_property(std::wstring_view name, bool value)`
- `template<typename T> T* dcast()`

## UField : UObject

Base class for fields (types, functions, properties).

## UStruct : UField

Represents a struct type.

### Methods

- `static UClass* static_class()`
- `UStruct* get_super_struct() const`
- `UStruct* get_super() const`
- `UFunction* find_function(std::wstring_view name) const`
- `FProperty* find_property(std::wstring_view name) const`
- `FField* get_child_properties() const`
- `UField* get_children() const`
- `int32_t get_properties_size() const`
- `int32_t get_min_alignment() const`

## UClass : UStruct

Represents a class type.

### Methods

- `static UClass* static_class()`
- `UObject* get_class_default_object() const`
- `std::vector<UObject*> get_objects_matching(bool allow_default = false) const`
- `UObject* get_first_object_matching(bool allow_default = false) const`

## UFunction : UStruct

Represents a function.

### Methods

- `static UClass* static_class()`
- `void call(UObject* obj, void* params)`
- `void* get_native_function() const`
- `uint32_t get_function_flags() const`
- `void set_function_flags(uint32_t flags)`
- `bool hook_ptr(UEVR_UFunction_CPPPreNative pre, UEVR_UFunction_CPPPostNative post)`

## UScriptStruct : UStruct

Represents a script struct (POD type).

### Methods

- `static UClass* static_class()`
- `StructOps* get_struct_ops() const`
- `int32_t get_struct_size() const`

## FField

Wrapper for both UField and FField.

### Methods

- `FField* get_next() const`
- `FName* get_fname() const`
- `FFieldClass* get_class() const`

## FProperty : FField

Represents a property.

### Methods

- `int32_t get_offset() const`
- `uint64_t get_property_flags() const`
- `bool is_param() const`
- `bool is_out_param() const`
- `bool is_return_param() const`
- `bool is_reference_param() const`
- `bool is_pod() const`

## FFieldClass

Represents a field class.

### Methods

- `FName* get_fname() const`
- `std::wstring get_name() const`

## FName

Represents a name.

### Methods

- `FName(std::wstring_view name, EFindName find_type = EFindName::Add)`
- `std::wstring to_string() const`

## FUObjectArray

Global UObject array.

### Methods

- `static FUObjectArray* get()`
- `static bool is_chunked()`
- `static bool is_inlined()`
- `static size_t get_objects_offset()`
- `static size_t get_item_distance()`
- `int32_t get_object_count() const`
- `void* get_objects_ptr() const`
- `UObject* get_object(int32_t index) const`

### FUObjectItem

```cpp
struct FUObjectItem {
    API::UObject* object;
    int32_t flags;
    int32_t cluster_index;
    int32_t serial_number;
};
```

## TArray<T>

A dynamic array.

### Members

- `T* data`
- `int32_t count`
- `int32_t capacity`

### Methods

- `T* begin()`
- `T* end()`
- `bool empty() const`
