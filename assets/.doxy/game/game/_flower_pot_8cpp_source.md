

# File FlowerPot.cpp

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**src**](dir_47d28cd3eb946f860e1fe0f4e720b9c2.md) **>** [**Npc**](dir_89665896fed3b86ffeb2c95c7fea51f5.md) **>** [**FlowerPot.cpp**](_flower_pot_8cpp.md)

[Go to the documentation of this file](_flower_pot_8cpp.md)


```C++
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
```


