

# File alSceneFunction.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Scene**](dir_bbf0d395114b7d01e47e296975854f01.md) **>** [**alSceneFunction.h**](al_scene_function_8h.md)

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


