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
