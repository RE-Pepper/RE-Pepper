

# File alISceneObj.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**Scene**](dir_7bfae1a6d4e86bc4cb4ede3d69a6b687.md) **>** [**alISceneObj.h**](al_i_scene_obj_8h.md)

[Go to the documentation of this file](al_i_scene_obj_8h.md)


```C++
#pragma once

namespace al
{
class ActorInitInfo;

class ISceneObj
{
public:
        virtual const char* getSceneObjName() const = 0;

        virtual void initAfterPlacementSceneObj( const ActorInitInfo& info )
        {
        }

        virtual void initSceneObj()
        {
        }
};

} // namespace al
```


