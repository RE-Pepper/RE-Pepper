

# File alRailMoveMovement.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**src**](dir_d8628e97cbd71936d4b5fb3774410590.md) **>** [**Rail**](dir_6ff4c1b13859b82bf8a5d6f47c0db9b6.md) **>** [**alRailMoveMovement.cpp**](al_rail_move_movement_8cpp.md)

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


