

# File alRailFunction.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**src**](dir_d8628e97cbd71936d4b5fb3774410590.md) **>** [**Rail**](dir_6ff4c1b13859b82bf8a5d6f47c0db9b6.md) **>** [**alRailFunction.cpp**](al_rail_function_8cpp.md)

[Go to the documentation of this file](al_rail_function_8cpp.md)


```C++
#include <LiveActor/alActorPoseKeeper.h>
#include <LiveActor/alLiveActor.h>
#include <Rail/alRailFunction.h>
#include <Rail/alRailKeeper.h>
#include <Rail/alRailRider.h>

namespace al
{

#ifdef NON_MATCHING
// 4 instructions scrambled at the end
void setSyncRailToStart( LiveActor* actor )
{
        actor->getRailKeeper()->getRailRider()->moveToRailStart();
        setTrans( actor, actor->getRailKeeper()->getRailRider()->getCurrentPos() );
}
#endif

const sead::Vector3f& getRailDir( const LiveActor* actor )
{
        return actor->getRailKeeper()->getRailRider()->getCurrentDir();
}

bool isRailReachedGoal( const LiveActor* actor )
{
        return actor->getRailKeeper()->getRailRider()->isReachedGoal();
}

bool isLoopRail( const LiveActor* actor )
{
        return actor->getRailKeeper()->getRailRider()->isLoop();
}

bool isExistRail( const LiveActor* actor )
{
        if ( actor->getRailKeeper() )
                return actor->getRailKeeper()->isExistRail();
        return false;
}

} // namespace al
```


