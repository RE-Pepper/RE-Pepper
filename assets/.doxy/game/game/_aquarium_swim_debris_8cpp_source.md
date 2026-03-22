

# File AquariumSwimDebris.cpp

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**src**](dir_47d28cd3eb946f860e1fe0f4e720b9c2.md) **>** [**Npc**](dir_89665896fed3b86ffeb2c95c7fea51f5.md) **>** [**AquariumSwimDebris.cpp**](_aquarium_swim_debris_8cpp.md)

[Go to the documentation of this file](_aquarium_swim_debris_8cpp.md)


```C++
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
                al::startHitReaction( this, "出現" );
}
```


