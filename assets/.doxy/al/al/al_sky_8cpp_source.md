

# File alSky.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**src**](dir_6f98f21a57298fb921e921b3faae2f7d.md) **>** [**Npc**](dir_be9125abb251b9d49bf58065264ab1d9.md) **>** [**alSky.cpp**](al_sky_8cpp.md)

[Go to the documentation of this file](al_sky_8cpp.md)


```C++
#include <Camera/alCamera.h>
#include <LiveActor/alActorInitUtil.h>
#include <LiveActor/alActorPoseKeeper.h>
#include <LiveActor/alLiveActorFunction.h>
#include <Npc/alSky.h>
#include <Stage/alStageSwitchKeeper.h>

namespace al
{

Sky::Sky( const char* name ) : MapObjActor( name ), mCameraTransPtr( nullptr )
{
}

void Sky::init( const ActorInitInfo& info )
{
        initActor( this, info );
        initStageSwitchAppear( this, info );
        mCameraTransPtr = al::getCameraPos();
        invalidateClipping( this );
        makeActorAppeared();
        trySyncStageSwitchAppear( this );
}

void Sky::calcAnim()
{
        setTrans( this, *mCameraTransPtr );
        LiveActor::calcAnim();
}

} // namespace al
```


