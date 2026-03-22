

# File alRailFunction.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**src**](dir_6f98f21a57298fb921e921b3faae2f7d.md) **>** [**Rail**](dir_7704832a95887b8dfaac4c9470889cbe.md) **>** [**alRailFunction.cpp**](al_rail_function_8cpp.md)

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


