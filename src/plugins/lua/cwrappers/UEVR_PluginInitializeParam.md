# UEVR_PluginInitializeParam

Accessed with `uevr.params`.

## Members

### `param.uevr_module`

The HMODULE of UEVR.

### `param.version`

The version of UEVR.

Returns:
```c
typedef struct {
    int major;
    int minor;
    int patch;
} UEVR_PluginVersion;
```

### `param.functions`

Returns [UEVR_PluginFunctions](UEVR_PluginFunctions.md).

### `param.callbacks`

Returns [UEVR_PluginCallbacks](UEVR_PluginCallbacks.md).

### `param.renderer`

Returns [UEVR_RendererData](UEVR_RendererData.md).

### `param.vr`

Returns [UEVR_VRData](UEVR_VRData.md).

### `param.openvr`

Returns [UEVR_OpenVRData](UEVR_OpenVRData.md).

### `param.openxr`

Returns [UEVR_OpenXRData](UEVR_OpenXRData.md).

### `param.sdk`

Returns [UEVR_SDKData](UEVR_SDKData.md).
