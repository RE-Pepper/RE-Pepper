

# File alCollisionUtil.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**Collision**](dir_b64277db147a0cb833174dd0bf4617cc.md) **>** [**alCollisionUtil.h**](al_collision_util_8h.md)

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


