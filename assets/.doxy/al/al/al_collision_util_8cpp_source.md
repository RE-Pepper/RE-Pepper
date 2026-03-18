

# File alCollisionUtil.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**src**](dir_d8628e97cbd71936d4b5fb3774410590.md) **>** [**Collision**](dir_4625c3c25d458a4908e8cd58e73b9017.md) **>** [**alCollisionUtil.cpp**](al_collision_util_8cpp.md)

[Go to the documentation of this file](al_collision_util_8cpp.md)


```C++
#include <Collision/alCollider.h>
#include <Collision/alCollisionUtil.h>
#include <LiveActor/alLiveActor.h>

namespace al
{

bool isCollidedGround( const LiveActor* actor )
{
        return actor->getCollider()->getGroundDistance() >= 0;
}

} // namespace al
```


