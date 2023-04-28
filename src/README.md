# UEVR

Welcome to UEVR! This powerful tool will transform your favorite Unreal Engine games into 6DOF VR experiences with minimal effort.

## Features

- Frontend GUI for easy process injection
- Supports OpenVR and OpenXR runtimes
- Native UE4/UE5 stereo rendering system for a truly immersive VR experience
- 3 rendering modes: Native Stereo, Synchronized Sequential, and Alternating/AFR
- 3DOF motion controls in many games, essentially emulating a semi-native VR experience
- Automatic handling of most in-game UI so it is projected into 3D space
- In-game menu with shortcuts for adjusting settings
- Access to various CVars for fixing broken shaders/effects
- Optional depth buffer integration for improved latency on some headsets
- Per-game configurations
- Plugin system/Blueprint support for modders to add additional features like motion controls

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
3. Pass `-nohmd` to the game's command line and/or delete VR plugins from the game directory if the game contains any existing VR plugins

## Quick overview of rendering methods

### Native Stereo

When it works, it looks the best, performs the best (usually). Can cause crashes or graphical bugs if the game does not play well with it.

Temporal effects like TAA are fully intact. DLSS/FSR2 usually work completely fine with no ghosting in this mode.

Fully synchronized eye rendering. Works with the majority of games. Uses the actual stereo rendering pipeline in the Unreal Engine to achieve a stereoscopic image.

### Synchronized Sequential

A form of AFR. Can fix many rendering bugs that are introduced with Native Stereo. Renders two frames **sequentially** in a **synchronized** fashion on the same engine tick.

Fully synchronized eye rendering. Game world does not advance time between frames.

Looks normal but temporal effects like TAA will have ghosting/doubling effect. Motion blur will need to be turned off.

This is the first alternative option that should be used if Native Stereo is not working as expected or you are encountering graphical bugs.

**Skip Draw** skips the viewport draw on the next engine tick. Usually works the best but sometimes particle effects may not play at the correct speed.

**Skip Tick** skips the next engine tick entirely. Usually buggy but does fix particle effects and sometimes brings higher performance.

### AFR

Alternated Frame Rendering. Renders each eye on separate frames in an alternating fashion, with the game world advancing time in between frames. Causes eye desyncs and usually nausea along with it.

Not synchronized. Generally should not be used unless the other two are unusable in some way.

## In-Game Menu

Press the **Insert** key or **L3+R3** on a controller to access the in-game menu, which opens by default at startup. With the menu open, hold **RT** for various shortcuts:

- RT + Left Stick: Move the camera left/right/forward/back
- RT + Right Stick: Move the camera up/down
- RT + B: Reset camera offset
- RT + Y: Recenter view
- RT + X: Reset standing origin

## Overview of basic injection and control methods

[![video](https://img.youtube.com/vi/AJjg8qUNaN4/0.jpg)](https://www.youtube.com/watch?v=AJjg8qUNaN4)

## Additional information

Read the [Detailed overview](usage/overview.md) for a comprehensive guide on how to fine-tune your VR experience.

## Special thanks

* [TheNewJavaman](https://github.com/TheNewJavaman) - Developer of the previous Unreal VR project.

To all the testers. These include:

* [Brian Tate](https://twitter.com/Flat2VR) - Founder of the Flat2VR community. He is the catalyst that kicked off this project. He was digging around and found out that most of the stereo pipeline is left in the engine.

* [Alex G/Virtual Insider](https://www.youtube.com/c/VirtualInsider) - A tester from the start. Has helped find many bugs and issues. Has also provided many helpful suggestions and ideas.

* [Alex/Waifu Enjoyer](https://www.youtube.com/@waifu_enjoyer) - One of the most prolific testers. Has tested hundreds of games and has helped find many bugs and issues. Has also provided many helpful suggestions and ideas. Has provided helpful statistics on game compatibility.

* [Alchemist](https://github.com/NicolasAubinet/) - DRG VR developer.

* [Jay Fullerton](https://www.youtube.com/@jayfullerton6981) - Has tested many games, and stands out as one of the testers with a lower end system. This has helped get an idea of how the tool performs on lower end hardware.

* Kitt - Mechwarrior 5 VR developer.

* Lance McCary - Has helped find many bugs and issues. Has also provided many helpful suggestions and ideas. Helped coordinate with Matthieu Bucchianeri to get eye tracked foveated rendering working in OpenXR Toolkit.

* Kalth Streil - Has helped find many bugs and issues.

* [Matthieu Bucchianeri](https://github.com/mbucchia) - Creator of OpenXR Toolkit. Has helped figure out what needed to be changed to get eye tracked foveated rendering working. Has also provided many helpful technical insights into the OpenXR API and VR development in general.

* [Narknon](https://github.com/narknon) - UE4SS developer. Provided a lot of helpful information about the Unreal Engine in general.

* [PinkMilkProductions](https://github.com/PinkMilkProductions) - DRG VR developer.

* [webhead](https://www.reddit.com/user/webheadVR)