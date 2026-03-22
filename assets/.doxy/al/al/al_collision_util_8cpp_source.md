

# File alCollisionUtil.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**src**](dir_6f98f21a57298fb921e921b3faae2f7d.md) **>** [**Collision**](dir_b09a96783c41b30bc153ca6a88ba8512.md) **>** [**alCollisionUtil.cpp**](al_collision_util_8cpp.md)

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


