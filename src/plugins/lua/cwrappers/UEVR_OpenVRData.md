# UEVR_OpenVRData

Accessed with `uevr.params.openvr`.

Provides access to the underlying OpenVR (SteamVR) interfaces. All accessors return opaque handles to the corresponding `IVR*` interface, or `nullptr` if the runtime is not OpenVR.

## Members

### `openvr.get_vr_system()`

Returns the `IVRSystem` interface handle.

### `openvr.get_vr_chaperone()`

Returns the `IVRChaperone` interface handle.

### `openvr.get_vr_chaperone_setup()`

Returns the `IVRChaperoneSetup` interface handle.

### `openvr.get_vr_compositor()`

Returns the `IVRCompositor` interface handle.

### `openvr.get_vr_overlay()`

Returns the `IVROverlay` interface handle.

### `openvr.get_vr_overlay_view()`

Returns the `IVROverlayView` interface handle.

### `openvr.get_vr_headset_view()`

Returns the `IVRHeadsetView` interface handle.

### `openvr.get_vr_screenshots()`

Returns the `IVRScreenshots` interface handle.

### `openvr.get_vr_render_models()`

Returns the `IVRRenderModels` interface handle.

### `openvr.get_vr_applications()`

Returns the `IVRApplications` interface handle.

### `openvr.get_vr_settings()`

Returns the `IVRSettings` interface handle.

### `openvr.get_vr_resources()`

Returns the `IVRResources` interface handle.

### `openvr.get_vr_extended_display()`

Returns the `IVRExtendedDisplay` interface handle.

### `openvr.get_vr_tracked_camera()`

Returns the `IVRTrackedCamera` interface handle.

### `openvr.get_vr_driver_manager()`

Returns the `IVRDriverManager` interface handle.

### `openvr.get_vr_input()`

Returns the `IVRInput` interface handle.

### `openvr.get_vr_io_buffer()`

Returns the `IVRIOBuffer` interface handle.

### `openvr.get_vr_spatial_anchors()`

Returns the `IVRSpatialAnchors` interface handle.

### `openvr.get_vr_notifications()`

Returns the `IVRNotifications` interface handle.

### `openvr.get_vr_debug()`

Returns the `IVRDebug` interface handle.
