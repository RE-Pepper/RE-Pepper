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
