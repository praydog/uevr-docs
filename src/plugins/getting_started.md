# UEVR: Plugin Development

This section covers the basics of developing plugins for UEVR. If you're looking for information on how to use UEVR, check out the [Usage](../usage/overview.md) section.

If you are unfamiliar with C/C++, you can try the [Blueprint API](blueprint.md).

## Overview

Plugins in UEVR are developed primarily in C++. However, the API header is written in C. This means it's possible to bind it to other languages, or even just write them in C. 

The API header is located in `include/uevr/API.h`. 

The C++ API header is in `include/uevr/API.hpp`.

The base C++ plugin header is in `include/uevr/Plugin.hpp`.

## Plugin Installation

Place the compiled plugin DLL into the game's persistent configuration directory at `%APPDATA%/UnrealVRMod/<game_exe_name>/plugins/`, or into the global directory at `%APPDATA%/UEVR/plugins/`.

During plugin development, you many want to create a symbolic link from the `plugins` dir to your project's DLL output directory. This way, you can build the plugin and have it automatically load into UEVR.

## Plugin Lifecycle

Plugins are loaded and unloaded at runtime. The plugin lifecycle is as follows:

1. UEVR starts its initialization process
2. UEVR initially loads all plugins, and calls their `DLLMain` functions
   * If the plugin is a C++ plugin, the DLLMain function will call the `on_dllmain` function of the plugin
3. UEVR begins initializing the rest of its own components
4. After initialization, UEVR calls the `on_initialize` function of each plugin
5. During its execution loop, UEVR will call the various `on_*` functions of each plugin
6. The user can choose to unload all plugins, and reload them at will at runtime

## The easy way

`Plugin.hpp` provides a class that can be inherited from to create a plugin. This class provides a number of virtual functions that can be overridden to implement the plugin's functionality.

The way it is structured is also how you would use the API in C++ using the API.h and API.hpp headers.

`Plugin.hpp` also implements a DLLMain for you, so you don't have to worry about that. All you need to worry about is overriding the virtual functions.

The project must be compiled as a DLL.

### A simple example

```cpp
#include <memory>

#include "uevr/Plugin.hpp"

using namespace uevr;

#define PLUGIN_LOG_ONCE(...) {\
    static bool _logged_ = false; \
    if (!_logged_) { \
        _logged_ = true; \
        API::get()->log_info(__VA_ARGS__); \
    }}

class ExamplePlugin : public uevr::Plugin {
public:
    ExamplePlugin() = default;

    void on_dllmain() override {}

    void on_initialize() override {
        // Logs to the appdata UnrealVRMod log.txt file
        API::get()->log_error("%s %s", "Hello", "error");
        API::get()->log_warn("%s %s", "Hello", "warning");
        API::get()->log_info("%s %s", "Hello", "info");
    }

    void on_pre_engine_tick(API::UGameEngine* engine, float delta) override {
        PLUGIN_LOG_ONCE("Pre Engine Tick: %f", delta);
    }

    void on_post_engine_tick(API::UGameEngine* engine, float delta) override {
        PLUGIN_LOG_ONCE("Post Engine Tick: %f", delta);
    }

    void on_pre_slate_draw_window_render_thread(UEVR_FSlateRHIRendererHandle renderer, UEVR_FViewportInfoHandle viewport_info) override {
        PLUGIN_LOG_ONCE("Pre Slate Draw Window");
    }

    void on_post_slate_draw_window_render_thread(UEVR_FSlateRHIRendererHandle renderer, UEVR_FViewportInfoHandle viewport_info) override {
        PLUGIN_LOG_ONCE("Post Slate Draw Window");
    }
};

// Actually creates the plugin. Very important that this global is created.
// The fact that it's using std::unique_ptr is not important, as long as the constructor is called in some way.
std::unique_ptr<ExamplePlugin> g_plugin{new ExamplePlugin()};
```

## Available Virtual Functions

`Plugin.hpp` exposes the following virtual functions that can be overridden:

### Main plugin callbacks

- `void on_dllmain()`
- `void on_initialize()`
- `void on_present()`
- `void on_post_render_vr_framework_dx11(ID3D11DeviceContext* context, ID3D11Texture2D* texture, ID3D11RenderTargetView* rtv)`
- `void on_post_render_vr_framework_dx12(ID3D12GraphicsCommandList* command_list, ID3D12Resource* rt, D3D12_CPU_DESCRIPTOR_HANDLE* rtv)`
- `void on_device_reset()`
- `bool on_message(HWND hwnd, UINT msg, WPARAM wparam, LPARAM lparam)`
- `void on_xinput_get_state(uint32_t* retval, uint32_t user_index, XINPUT_STATE* state)`
- `void on_xinput_set_state(uint32_t* retval, uint32_t user_index, XINPUT_VIBRATION* vibration)`

### Game/Engine callbacks

- `void on_pre_engine_tick(API::UGameEngine* engine, float delta)`
- `void on_post_engine_tick(API::UGameEngine* engine, float delta)`
- `void on_pre_slate_draw_window_render_thread(UEVR_FSlateRHIRendererHandle renderer, UEVR_FViewportInfoHandle viewport_info)`
- `void on_post_slate_draw_window_render_thread(UEVR_FSlateRHIRendererHandle renderer, UEVR_FViewportInfoHandle viewport_info)`
- `void on_pre_calculate_stereo_view_offset(UEVR_StereoRenderingDeviceHandle device, int view_index, float world_to_meters, UEVR_Vector3f* position, UEVR_Rotatorf* rotation, bool is_double)`
- `void on_post_calculate_stereo_view_offset(UEVR_StereoRenderingDeviceHandle device, int view_index, float world_to_meters, UEVR_Vector3f* position, UEVR_Rotatorf* rotation, bool is_double)`
- `void on_pre_viewport_client_draw(UEVR_UGameViewportClientHandle viewport_client, UEVR_FViewportHandle viewport, UEVR_FCanvasHandle canvas)`
- `void on_post_viewport_client_draw(UEVR_UGameViewportClientHandle viewport_client, UEVR_FViewportHandle viewport, UEVR_FCanvasHandle canvas)`
- `void on_custom_event(const char* event_name, const char* event_data)`

### Rendering callbacks

- `void on_frame()`
- `void on_draw_ui()`
- `void on_config_load(const utility::Config& cfg, bool set_defaults)`
- `void on_config_save(utility::Config& cfg)`

