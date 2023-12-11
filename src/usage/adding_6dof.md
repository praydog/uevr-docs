# UEVR: UObjectHook

## What is UObjectHook?

UObjectHook is an extra part of UEVR that can be used to do many things, such as:

* Attach the camera to any object or component in the game
* Add 6DoF motion controls by attaching any components to the motion controllers
    * This is usually contingent on the 3DoF motion controls working in the first place
* Modify and view any property of any active UObject in the game
* Toggle the visibility of any component in the game
* Save the state of all of the above for persistence across sessions

## Attaching the camera to an object

<video width="640" height="480" controls>
<source src="videos/camera_attach.mp4" type="video/mp4">
</video>

In this example, we'll attach the camera to the local player/pawn.

1. Open the in-game menu and enable advanced options if not already enabled
2. Navigate to UObjectHook on the left side
3. Go to "Common Objects"
4. Go to "Acknowledged Pawn"
5. Click "Attach Camera to" (click "Attach Camera to (Relative)" if the game is already first-person)
6. Click "Save State"

Doing this allows you to turn third person games into first person games. If done in a first person game, this removes unwanted camera movement that should not be there in VR.