#include "MapObj/FlowerPot.h"

#include <LiveActor/alActorInitUtil.h>
#include <LiveActor/alLiveActorFunction.h>
#include <Nerve/alNerve.h>
#include <Nerve/alNerveFunction.h>

namespace NrvFlowerPot
{

NERVE_DEF( FlowerPot, Wait );

} // namespace NrvFlowerPot

FlowerPot::FlowerPot( const sead::SafeString& name ) : MapObjActor( name )
{
}

void FlowerPot::init( const al::ActorInitInfo& info )
{
        al::initActorWithArchiveName( this, info, "FlowerPot" );
        al::initNerve( this, &NrvFlowerPot::Wait );
        makeActorAppeared();
}

void FlowerPot::exeWait()
{
}
