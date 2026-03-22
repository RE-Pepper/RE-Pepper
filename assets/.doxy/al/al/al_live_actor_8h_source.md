

# File alLiveActor.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**LiveActor**](dir_834378260339034a4005b37c1f1948d3.md) **>** [**alLiveActor.h**](al_live_actor_8h.md)

[Go to the documentation of this file](al_live_actor_8h.md)


```C++
#pragma once

#include <Audio/alAudioKeeper.h>
#include <Effect/alEffectKeeper.h>
#include <LiveActor/alLiveActorFlag.h>
#include <Nerve/alNerveKeeper.h>
#include <Stage/alStageSwitchKeeper.h>
#include <math/seadMatrix.h>

class alActorPoseFunction;
class alLiveActorFunction;

namespace al
{
class ActorPoseKeeperBase;
class ActorExecuteInfo;
class ActorActionKeeper;
class Collider;
class CollisionParts;
class ModelKeeper;
class HitSensorKeeper;
class RailKeeper;
class ShadowKeeper;
class ActorLightCtrl;
class SubActorKeeper;
class HitSensor;

class LiveActor : public IUseNerve,
                  public IUseEffectKeeper,
                  public IUseAudioKeeper,
                  public IUseStageSwitch
{
        friend class ::alActorPoseFunction;
        friend class ::alLiveActorFunction;

private:
        const char* mActorName;

protected:
        ActorPoseKeeperBase* mActorPoseKeeper;
        ActorExecuteInfo*    mActorExecuteInfo;
        ActorActionKeeper*   mActorActionKeeper;
        Collider*            mCollider;
        CollisionParts*      mCollisionParts;
        ModelKeeper*         mModelKeeper;
        NerveKeeper*         mNerveKeeper;
        HitSensorKeeper*     mHitSensorKeeper;
        EffectKeeper*        mEffectKeeper;
        AudioKeeper*         mAudioKeeper;
        StageSwitchKeeper*   mStageSwitchKeeper;
        RailKeeper*          mRailKeeper;
        ShadowKeeper*        mShadowKeeper;
        ActorLightCtrl*      mActorLightCtrl;
        void*                _4C;
        SubActorKeeper*      mSubActorKeeper;

private:
        LiveActorFlag mLiveActorFlag;

public:
        const char* getName() const
        {
                return mActorName;
        }

        ActorPoseKeeperBase* getActorPoseKeeper() const
        {
                return mActorPoseKeeper;
        }

        ActorExecuteInfo* getActorExecuteInfo() const
        {
                return mActorExecuteInfo;
        }

        ActorActionKeeper* getActorActionKeeper() const
        {
                return mActorActionKeeper;
        }

        Collider* getCollider() const
        {
                return mCollider;
        }

        ModelKeeper* getModelKeeper() const
        {
                return mModelKeeper;
        }

        HitSensorKeeper* getHitSensorKeeper() const
        {
                return mHitSensorKeeper;
        }

        RailKeeper* getRailKeeper() const
        {
                return mRailKeeper;
        }

        ShadowKeeper* getShadowKeeper() const
        {
                return mShadowKeeper;
        }

        LiveActorFlag& getLiveActorFlag()
        {
                return mLiveActorFlag;
        }

        const LiveActorFlag& getLiveActorFlag() const
        {
                return mLiveActorFlag;
        }

public:
        virtual NerveKeeper* getNerveKeeper() const;

        void initPoseKeeper( ActorPoseKeeperBase* pPoseKeeper );
        void initCollider( float radius, float yOffset, u32 );
        void initNerveKeeper( NerveKeeper* nk );
        void initRailKeeper( const ActorInitInfo& info );

        virtual void                   init( const ActorInitInfo& info );
        virtual void                   initAfterPlacement();
        virtual void                   appear();
        virtual void                   makeActorAppeared();
        virtual void                   kill();
        virtual void                   makeActorDead();
        virtual void                   movement();
        virtual void                   calcAnim();
        virtual void                   draw();
        virtual void                   startClipped();
        virtual void                   endClipped();
        virtual void                   attackSensor( HitSensor* me, HitSensor* other );
        virtual bool                   receiveMsg( u32 msg, HitSensor* other, HitSensor* me );
        virtual const sead::Matrix34f* getBaseMtx() const;
        virtual EffectKeeper*          getEffectKeeper() const;
        virtual AudioKeeper*           getAudioKeeper() const;
        virtual StageSwitchKeeper*     getStageSwitchKeeper() const;
        virtual void                   initStageSwitchKeeper();
        virtual void                   control();
        virtual void                   calcAndSetBaseMtx() {}
        virtual void                   updateCollider();
        virtual void                   v22() {}
        virtual void                   v23() {}

public:
        LiveActor( const char* name );
};

static_assert( sizeof( LiveActor ) == 0x60, "" );

} // namespace al
```


