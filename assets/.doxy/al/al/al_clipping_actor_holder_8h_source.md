

# File alClippingActorHolder.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Clipping**](dir_b42721b03f0382f09cda06110232e739.md) **>** [**alClippingActorHolder.h**](al_clipping_actor_holder_8h.md)

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


