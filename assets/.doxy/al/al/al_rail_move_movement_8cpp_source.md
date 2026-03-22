

# File alRailMoveMovement.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**src**](dir_6f98f21a57298fb921e921b3faae2f7d.md) **>** [**Rail**](dir_7704832a95887b8dfaac4c9470889cbe.md) **>** [**alRailMoveMovement.cpp**](al_rail_move_movement_8cpp.md)

[Go to the documentation of this file](al_rail_move_movement_8cpp.md)


```C++
#include <LiveActor/alActorInitInfo.h>
#include <Nerve/alNerve.h>
#include <Placement/alPlacementFunction.h>
#include <Rail/alRailFunction.h>
#include <Rail/alRailMoveMovement.h>

namespace al
{

namespace NrvRailMoveMovement
{

NERVE_DEF( RailMoveMovement, Move )

} // namespace NrvRailMoveMovement

#ifdef NON_MATCHING
// string
RailMoveMovement::RailMoveMovement( LiveActor* host, const ActorInitInfo& info, const char* speedParamName, const char* moveTypeParamName )
    : al::HostStateBase<al::LiveActor>( host, "レール移動挙動" ), mSpeed( 10 ), mMoveType( 0 )
{
        tryGetArg( &mSpeed, getPlacementInfo( info ), speedParamName );
        tryGetArg( (int*)&mMoveType, getPlacementInfo( info ), moveTypeParamName );
        if ( mMoveType >= 2 )
                mMoveType = 0;
        initNerve( &NrvRailMoveMovement::Move );
}
#endif

void RailMoveMovement::exeMove()
{
        if ( isExistRail( mHost ) )
        {
                if ( mMoveType == 0 )
                        moveSyncRail( mHost, mSpeed );
                else if ( mMoveType == 1 )
                        moveSyncRailTurn( mHost, mSpeed );
                else if ( mMoveType == 2 )
                        moveSyncRailLoop( mHost, mSpeed );
        }
}

} // namespace al
```


