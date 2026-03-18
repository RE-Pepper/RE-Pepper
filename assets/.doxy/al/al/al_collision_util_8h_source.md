

# File alCollisionUtil.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Collision**](dir_d59a8b5ffa8fb2437785c15a7148fb09.md) **>** [**alCollisionUtil.h**](al_collision_util_8h.md)

[Go to the documentation of this file](al_collision_util_8h.md)


```C++
#pragma once

#include <math/seadMatrix.h>

namespace al
{
class LiveActor;

void syncCollisionMtx( LiveActor* actor, const sead::Matrix34f* );

bool isCollided( const LiveActor* actor );
bool isCollidedGround( const LiveActor* actor );
bool isCollidedWall( const LiveActor* actor );
bool isOnGround( const LiveActor* actor, u32 );

} // namespace al
```


