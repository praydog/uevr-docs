# UnrealVR

Welcome to UnrealVR! This powerful tool will transform your favorite Unreal Engine games into 6DOF VR experiences with minimal effort.

## Features

- Frontend GUI for easy process injection
- Supports OpenVR and OpenXR runtimes
- Native UE4/UE5 stereo rendering system for a truly immersive VR experience
- 3 rendering modes: Native Stereo, Synchronized Sequential, and Alternating/AFR
- Automatic handling of most in-game UI so it is projected into 3D space
- In-game menu with shortcuts for adjusting settings
- Access to various CVars for fixing broken shaders/effects
- Optional depth buffer integration for improved latency on some headsets
- Per-game configurations
- Plugin system for modders to add additional features like motion controls

## Getting Started

1. Launch the frontend GUI (UnrealVR.exe)
2. Launch the target game
3. Locate the game in the process dropdown list
4. Select your desired runtime (OpenVR/OpenXR)
5. Toggle existing VR plugin nullification (if necessary)
6. Configure pre-injection settings
7. Inject

## To-dos before injection

1. Disable HDR (it will still work without it, but the game will be darker than usual if it is)
2. Start as administrator if the game is not visible in the list
3. Pass -nohmd to the command line and/or delete VR plugins from the game directory if the game contains any existing VR plugins

## Quick overview of rendering methods

### Native Stereo

When it works, it looks the best, performs the best (usually). Can cause crashes or graphical bugs if the game does not play well with it.

Temporal effects like TAA are fully intact. DLSS/FSR2 usually work completely fine with no ghosting in this mode.

Fully synchronized eye rendering. Works with the majority of games.

### Synchronized Sequential

A form of AFR. Can fix many rendering bugs that are introduced with Native Stereo.

Fully synchronized eye rendering. Game world does not advance time between frames.

Looks normal but temporal effects like TAA will have ghosting/doubling effect. Motion blur will need to be turned off.

This is the first alternative option that should be used if Native Stereo is not working as expected or you are encountering graphical bugs.

### AFR

Alternate Frame Rendering. Renders each eye on separate frames, with the game world advancing time in between frames, causing desyncs and usually nausea along with it.

Not synchronized. Generally should not be used unless the other two are unusable in some way.

## In-Game Menu

Press the **Insert** key or **L3+R3** on a controller to access the in-game menu, which opens by default at startup. With the menu open, hold **RT** for various shortcuts:

- RT + Left Stick: Move the camera left/right/forward/back
- RT + Right Stick: Move the camera up/down
- RT + B: Reset camera offset
- RT + Y: Recenter view
- RT + X: Reset standing origin

## Additional information

Read the [Detailed overview](usage/overview.md) for a comprehensive guide on how to fine-tune your VR experience.
