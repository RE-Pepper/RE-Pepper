

# File TransparentWall.cpp

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**src**](dir_47d28cd3eb946f860e1fe0f4e720b9c2.md) **>** [**MapObj**](dir_d5af9f6f62d27d9e3db1b7ff0fb6c0e1.md) **>** [**TransparentWall.cpp**](_transparent_wall_8cpp.md)

[Go to the documentation of this file](_transparent_wall_8cpp.md)


```C++
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
```


