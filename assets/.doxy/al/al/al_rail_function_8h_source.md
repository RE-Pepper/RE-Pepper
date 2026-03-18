

# File alRailFunction.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Rail**](dir_eddceeca1a9539e4ec5247c1a556acdf.md) **>** [**alRailFunction.h**](al_rail_function_8h.md)

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


