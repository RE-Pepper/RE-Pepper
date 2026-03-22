#include "MapObj/PeachRope.h"

#include <LiveActor/alActorActionKeeper.h>
#include <LiveActor/alActorInitUtil.h>
#include <LiveActor/alLiveActorFunction.h>

PeachRope::PeachRope( const sead::SafeString& name ) : MapObjActor( name )
{
}

void PeachRope::init( const al::ActorInitInfo& info )
{
        al::initActorWithArchiveName( this, info, "PeachRope" );
        makeActorAppeared();
}

void PeachRope::kill()
{
        al::startHitReactionDeath( this );
        LiveActor::kill();
}
