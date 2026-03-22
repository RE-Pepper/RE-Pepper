

# File alRailFunction.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**Rail**](dir_c8bcdc1e1ae46381fd1d0b5e3e0c3157.md) **>** [**alRailFunction.h**](al_rail_function_8h.md)

[Go to the documentation of this file](al_rail_function_8h.md)


```C++
#pragma once

namespace al
{
class LiveActor;

void setSyncRailToStart( LiveActor* actor );

const sead::Vector3f& getRailDir( const LiveActor* actor );
bool                  isRailReachedGoal( const LiveActor* actor );

void moveSyncRail( LiveActor* actor, float speed );
void moveSyncRailTurn( LiveActor* actor, float speed );
void moveSyncRailLoop( LiveActor* actor, float speed );

bool isLoopRail( const LiveActor* actor );
bool isExistRail( const LiveActor* actor );

} // namespace al
```


