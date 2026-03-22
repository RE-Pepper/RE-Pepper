#include "MapObj/TransparentWall.h"

#include <LiveActor/alActorInitUtil.h>
#include <LiveActor/alLiveActorFunction.h>
#include <Placement/alPlacementFunction.h>
#include <Stage/alStageSwitchKeeper.h>

TransparentWall::TransparentWall( const sead::SafeString& name ) : MapObjActor( name )
{
}

void TransparentWall::init( const al::ActorInitInfo& info )
{
        if ( al::isObjectName( info, "TransparentWallMoveLimit" ) )
                al::initActorWithArchiveName( this, info, "TransparentWall", "MoveLimit" );
        else
                al::initActor( this, info );
        al::initStageSwitchAppear( this, info );
        al::trySyncStageSwitchAppear( this );
        al::initStageSwitchKill( this, info );
        al::trySyncStageSwitchKill( this );
}

void TransparentWall::makeActorDead()
{
        LiveActor::makeActorDead();
}
