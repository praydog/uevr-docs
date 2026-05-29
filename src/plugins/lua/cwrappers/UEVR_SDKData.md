# UEVR_SDKData

Accessed with `uevr.params.sdk`

Provides access to all engine/game-specific SDK function tables.

## Members

### `sdk.functions`

Returns `UEVR_SDKFunctions` — high-level SDK helpers such as `get_uengine`, `get_uobject_array`, `get_player_controller`, `get_local_pawn`, `spawn_object`, `execute_command`, `execute_command_ex`, `get_console_manager`, `set_cvar_int`, and `add_component_by_class`.

### `sdk.callbacks`

Returns `UEVR_SDKCallbacks` — the engine-tick / slate / stereo / viewport callback table (see [callbacks](../callbacks.md)).

### `sdk.uobject`

Returns `UEVR_UObjectFunctions` — UObject manipulation (`get_class`, `get_outer`, `is_a`, `process_event`, `call_function`, `get_fname`, `get_property_data`, `get_bool_property`, `set_bool_property`).

### `sdk.uobject_array`

Returns `UEVR_UObjectArrayFunctions` — global UObject array access. See [FUObjectArray](../types/FUObjectArray.md).

### `sdk.ffield`

Returns `UEVR_FFieldFunctions`. See [FField](../types/FField.md).

### `sdk.fproperty`

Returns `UEVR_FPropertyFunctions`. See [FProperty](../types/FProperty.md).

### `sdk.ustruct`

Returns `UEVR_UStructFunctions`. See [UStruct](../types/UStruct.md).

### `sdk.uclass`

Returns `UEVR_UClassFunctions`. See [UClass](../types/UClass.md).

### `sdk.ufunction`

Returns `UEVR_UFunctionFunctions`. See [UFunction](../types/UFunction.md).

### `sdk.uobject_hook`

Returns `UEVR_UObjectHookFunctions`. See [UObjectHook](../types/UObjectHook.md).

### `sdk.ffield_class`

Returns `UEVR_FFieldClassFunctions`. See [FFieldClass](../types/FFieldClass.md).

### `sdk.fname`

Returns `UEVR_FNameFunctions`. See [FName](../types/FName.md).

### `sdk.console`

Returns `UEVR_ConsoleFunctions` — console manager / variable / command helpers. See [FConsoleManager](../types/FConsoleManager.md).

### `sdk.malloc`

Returns `UEVR_FMallocFunctions` — engine allocator (`get`, `malloc`, `realloc`, `free`).

### `sdk.render_target_pool_hook`

Returns `UEVR_FRenderTargetPoolHookFunctions` (`activate`, `get_render_target`).

### `sdk.stereo_hook`

Returns `UEVR_FFakeStereoRenderingHookFunctions` (`get_scene_render_target`, `get_ui_render_target`).

### `sdk.frhitexture2d`

Returns `UEVR_FRHITexture2DFunctions` (`get_native_resource`).

### `sdk.uscriptstruct`

Returns `UEVR_UScriptStructFunctions`. See [UScriptStruct](../types/UScriptStruct.md).

### `sdk.farrayproperty`

Returns `UEVR_FArrayPropertyFunctions` (`get_inner`).

### `sdk.fboolproperty`

Returns `UEVR_FBoolPropertyFunctions` (bitfield bool property accessors: `get_field_size`, `get_byte_offset`, `get_byte_mask`, `get_field_mask`, `get_value_from_object`, `get_value_from_propbase`, `set_value_in_object`, `set_value_in_propbase`).

### `sdk.fstructproperty`

Returns `UEVR_FStructPropertyFunctions` (`get_struct`).

### `sdk.fenumproperty`

Returns `UEVR_FEnumPropertyFunctions` (`get_underlying_prop`, `get_enum`).

### `sdk.ufield`

Returns `UEVR_UFieldFunctions`. See [UField](../types/UField.md).

### `sdk.game_viewport_client`

Returns `UEVR_UGameViewportClientFunctions` (`exec`, `exec_ex`). See [UGameViewportClient](../types/UGameViewportClient.md).
