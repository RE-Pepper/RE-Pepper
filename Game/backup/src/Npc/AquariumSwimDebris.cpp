#include "MapObj/AquariumSwimDebris.h"

#include <LiveActor/alActorActionKeeper.h>
#include <LiveActor/alActorInitUtil.h>
#include <LiveActor/alLiveActorFunction.h>
#include <Nerve/alNerve.h>
#include <Nerve/alNerveFunction.h>
#include <Placement/alPlacementFunction.h>
#include <Stage/alStageSwitchKeeper.h>

namespace NrvAquariumSwimDebris
{

NERVE_DEF( AquariumSwimDebris, Appear );

} // namespace NrvAquariumSwimDebris

AquariumSwimDebris::AquariumSwimDebris( const sead::SafeString& name ) : MapObjActor( name )
{
}

void AquariumSwimDebris::init( const al::ActorInitInfo& info )
{
        al::initActorWithArchiveName( this, info, "AquariumSwimDebris", nullptr );
        al::initNerve( this, &NrvAquariumSwimDebris::Appear, 1 );
        al::initStageSwitchAppear( this, info );
        al::trySyncStageSwitchAppear( this );
}

void AquariumSwimDebris::exeAppear()
{
        if ( al::isFirstStep( this ) )
                al::startHitReaction( this, "èoåª" );
}
