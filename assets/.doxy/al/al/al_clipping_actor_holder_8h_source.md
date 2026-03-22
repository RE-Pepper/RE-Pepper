

# File alClippingActorHolder.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**Clipping**](dir_7e8c68cf19e0ef7d7545051dcecbf0eb.md) **>** [**alClippingActorHolder.h**](al_clipping_actor_holder_8h.md)

[Go to the documentation of this file](al_clipping_actor_holder_8h.md)


```C++
#pragma once

namespace al
{

class ClippingActorInfoList;
class LiveActor;

class ClippingActorHolder
{
private:
        int                    _0;
        int                    _4;
        ClippingActorInfoList* _8;
        ClippingActorInfoList* _C;
        ClippingActorInfoList* _10;
        ClippingActorInfoList* _14;

public:
        void invalidateClipping( LiveActor* actor );
        void validateClipping( LiveActor* actor );

public:
        ClippingActorHolder( int );
};

} // namespace al
```


