

# File PeachRope.cpp

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**src**](dir_47d28cd3eb946f860e1fe0f4e720b9c2.md) **>** [**Npc**](dir_89665896fed3b86ffeb2c95c7fea51f5.md) **>** [**PeachRope.cpp**](_peach_rope_8cpp.md)

[Go to the documentation of this file](_peach_rope_8cpp.md)


```C++
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
```


