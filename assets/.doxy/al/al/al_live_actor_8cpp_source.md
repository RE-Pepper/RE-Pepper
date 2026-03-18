

# File alLiveActor.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**src**](dir_d8628e97cbd71936d4b5fb3774410590.md) **>** [**LiveActor**](dir_8d17faa1063b24478b1232799869255d.md) **>** [**alLiveActor.cpp**](al_live_actor_8cpp.md)

[Go to the documentation of this file](al_live_actor_8cpp.md)


```C++
#include <LiveActor/alActorInitInfo.h>
#include <LiveActor/alLiveActor.h>
#include <LiveActor/alLiveActorFunction.h>
#include <LiveActor/alLiveActorGroup.h>
#include <LiveActor/alLiveActorKit.h>
#include <Rail/alRailKeeper.h>

namespace al
{

LiveActor::LiveActor( const char* name )
    : mActorName( name ), mActorPoseKeeper( nullptr ), mActorExecuteInfo( nullptr ),
      mActorActionKeeper( nullptr ), mCollider( nullptr ), mCollisionParts( nullptr ),
      mModelKeeper( nullptr ), mNerveKeeper( nullptr ), mHitSensorKeeper( nullptr ),
      mEffectKeeper( nullptr ), mAudioKeeper( nullptr ), mStageSwitchKeeper( nullptr ),
      mRailKeeper( nullptr ), mShadowKeeper( nullptr ), mActorLightCtrl( nullptr ), _4C( nullptr ),
      mSubActorKeeper( nullptr )
{
        getLiveActorKit()->getAllActors()->registerActor( this );
}

NerveKeeper* LiveActor::getNerveKeeper() const
{
        return mNerveKeeper;
}

void LiveActor::init( const ActorInitInfo& info )
{
}

void LiveActor::initAfterPlacement()
{
}

void LiveActor::appear()
{
        makeActorAppeared();
}

void LiveActor::kill()
{
        makeActorDead();
}

void LiveActor::calcAnim()
{
        if ( !mLiveActorFlag.isDead && ( !mLiveActorFlag.isClipped || mLiveActorFlag.isDrawClipping ) )
        {
                if ( mActorPoseKeeper )
                        alLiveActorFunction::calcAnimDirect( this );
                if ( getAudioKeeper() )
                        getAudioKeeper()->update();
        }
}

void LiveActor::attackSensor( HitSensor* me, HitSensor* other )
{
}

bool LiveActor::receiveMsg( u32 msg, HitSensor* other, HitSensor* me )
{
        return false;
}

void LiveActor::draw()
{
}

EffectKeeper* LiveActor::getEffectKeeper() const
{
        return mEffectKeeper;
}

AudioKeeper* LiveActor::getAudioKeeper() const
{
        return mAudioKeeper;
}

StageSwitchKeeper* LiveActor::getStageSwitchKeeper() const
{
        return mStageSwitchKeeper;
}

void LiveActor::initStageSwitchKeeper()
{
        mStageSwitchKeeper = new StageSwitchKeeper();
}

void LiveActor::control()
{
}

void LiveActor::initNerveKeeper( NerveKeeper* nk )
{
        mNerveKeeper = nk;
}

void LiveActor::initPoseKeeper( ActorPoseKeeperBase* pPoseKeeper )
{
        mActorPoseKeeper = pPoseKeeper;
}

void LiveActor::initRailKeeper( const ActorInitInfo& info )
{
        mRailKeeper = al::tryCreateRailKeeper( al::getPlacementInfo( info ) );
}

} // namespace al
```


