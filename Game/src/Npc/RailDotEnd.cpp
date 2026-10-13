#include "MapObj/RailDotEnd.h"

#include <LiveActor/alActorInitUtil.h>
#include <LiveActor/alLiveActorFunction.h>
#include <Nerve/alNerve.h>
#include <Nerve/alNerveFunction.h>

namespace NrvRailDotEnd
{

NERVE_DEF( RailDotEnd, Wait );

} // namespace NrvRailDotEnd

RailDotEnd::RailDotEnd( const sead::SafeString& name ) : MapObjActor( name )
{
}

void RailDotEnd::init( const al::ActorInitInfo& info )
{
        al::initActorWithArchiveName( this, info, "RailDotEnd" );
        al::initNerve( this, &NrvRailDotEnd::Wait );
        makeActorAppeared();
}

void RailDotEnd::exeWait()
{
}
