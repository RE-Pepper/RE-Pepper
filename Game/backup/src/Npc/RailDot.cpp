#include "MapObj/RailDot.h"

#include <LiveActor/alActorInitUtil.h>
#include <LiveActor/alLiveActorFunction.h>
#include <Nerve/alNerve.h>
#include <Nerve/alNerveFunction.h>

namespace NrvRailDot
{

NERVE_DEF( RailDot, Wait );

} // namespace NrvRailDot

RailDot::RailDot( const sead::SafeString& name ) : MapObjActor( name )
{
}

void RailDot::init( const al::ActorInitInfo& info )
{
        al::initActorWithArchiveName( this, info, "RailDot" );
        al::initNerve( this, &NrvRailDot::Wait );
        makeActorAppeared();
}

void RailDot::exeWait()
{
}
