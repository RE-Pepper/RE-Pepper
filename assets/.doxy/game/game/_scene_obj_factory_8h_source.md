

# File SceneObjFactory.h

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**include**](dir_e05fb92cc301336445c4f62f6c4f58b8.md) **>** [**Scene**](dir_84f8925aa2d2bbbcb80a56e59501bb98.md) **>** [**SceneObjFactory.h**](_scene_obj_factory_8h.md)

[Go to the documentation of this file](_scene_obj_factory_8h.md)


```C++
#pragma once

#include <Scene/alSceneObjHolder.h>

namespace SceneObjFactory
{

al::SceneObjHolder* createSceneObjHolder();

} // namespace SceneObjFactory

enum SceneObjType
{
        SceneObjType_CameraShaker          = 1,
        SceneObjType_SwitchAreaDirector    = 3,
        SceneObjType_AudioDirector         = 4, // not sure
        SceneObjType_CoinRotater           = 7,
        SceneObjType_CoinCollectInfoKeeper = 9, // not sure
        SceneObjType_ItemHolder            = 10,
        SceneObjType_GhostPlayerRecorder   = 20
};
```


