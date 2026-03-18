

# File alLiveActorFlag.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**LiveActor**](dir_ae80ee5cf9da1054faf149dc2356c7ac.md) **>** [**alLiveActorFlag.h**](al_live_actor_flag_8h.md)

[Go to the documentation of this file](al_live_actor_flag_8h.md)


```C++
#pragma once

namespace al
{

struct LiveActorFlag
{
        bool isDead;
        bool isClipped;
        bool isInvalidClipping;
        bool isDrawClipping;
        bool flag5;
        bool isHideModel;
        bool isOffCollide;
        bool flag8;
        bool isValidMaterialCode;

        LiveActorFlag();
};

} // namespace al
```


