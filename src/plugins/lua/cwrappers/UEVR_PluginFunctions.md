# UEVR_PluginFunctions

Accessed with `uevr.params.functions`

## Members

### `functions.log_error(msg)`

Logs an error message.

### `functions.log_warning(msg)`

Logs a warning message.

### `functions.log_info(msg)`

Logs an info message.

### `functions.is_drawing_ui()`

Returns `true` if UEVR is drawing its menu.

### `functions.get_commit_hash()`

Returns the commit hash of UEVR.

### `functions.get_tag()`

Returns the tag of UEVR.

### `functions.get_tag_long()`

Returns the long tag of UEVR.

### `functions.get_branch()`

Returns the branch of UEVR.

### `functions.get_build_date()`

Returns the build date of UEVR.

### `functions.get_build_time()`

Returns the build time of UEVR.

### `functions.get_commits_past_tag()`

Returns the number of commits past the last tag.

### `functions.get_total_commits()`

Returns the total number of commits to UEVR.

### `functions.remove_callback(cb)`

Removes a previously registered callback.

### `functions.get_persistent_dir()`

Returns the path to the persistent configuration directory for the current game.

### `functions.register_inline_hook(target, dst, original)`

Registers an inline hook. `target` is the address to hook, `dst` is the destination function, `original` is an output pointer for the original function.

### `functions.unregister_inline_hook(hook_id)`

Unregisters an inline hook by its ID.

### `functions.dispatch_lua_event(event_name, event_data)`

Dispatches a Lua event to all script contexts.

### `functions.dispatch_custom_event(event_name, event_data)`

Dispatches a custom event for plugins to listen to via `on_custom_event`.