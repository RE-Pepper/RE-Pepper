#include <Camera/alCamera.h>
#include <LiveActor/alActorInitUtil.h>
#include <LiveActor/alActorPoseKeeper.h>
#include <LiveActor/alLiveActorFunction.h>
#include <Npc/Sky.h>
#include <Stage/alStageSwitchKeeper.h>



Sky::Sky( const char* name ) : al::MapObjActor( name ), mCameraTransPtr( nullptr )
{
}

void Sky::init( const al::ActorInitInfo& info )
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
