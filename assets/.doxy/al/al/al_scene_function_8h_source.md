

# File alSceneFunction.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**Scene**](dir_7bfae1a6d4e86bc4cb4ede3d69a6b687.md) **>** [**alSceneFunction.h**](al_scene_function_8h.md)

[Go to the documentation of this file](al_scene_function_8h.md)


```C++
#pragma once

#include <Placement/alPlacementInfo.h>
#include <Resource/alResource.h>
#include <Scene/alScene.h>

namespace al
{
class Resource;
class Scene;

void initPlacementMap( Scene* scene, const Resource* stageArchive, const ActorInitInfo& infoTemplate, const char* infoIterName );

bool tryGetPlacementInfo( PlacementInfo* out, const Resource* stageArchive, const char* infoIterName );

} // namespace al
```


