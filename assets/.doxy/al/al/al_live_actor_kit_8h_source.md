

# File alLiveActorKit.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**LiveActor**](dir_834378260339034a4005b37c1f1948d3.md) **>** [**alLiveActorKit.h**](al_live_actor_kit_8h.md)

[Go to the documentation of this file](al_live_actor_kit_8h.md)


```C++
#pragma once

namespace al
{
class ExecuteDirector;
class EffectSystem;
class FogDirector;
class ClippingDirector;
class CollisionDirector;
class HitSensorDirector;
class LiveActorGroup;

class LiveActorKit
{
private:
        int                mAllActorsBufferSize;
        ExecuteDirector*   mExecuteDirector;
        EffectSystem*      mEffectSystem;
        void*              _C;
        void*              _10;
        FogDirector*       mFogDirector;
        void*              _18;
        void*              _1C;
        void*              _20;
        ClippingDirector*  mClippingDirector;
        CollisionDirector* mCollisionDirector;
        HitSensorDirector* mHitSensorDirector;
        void*              _30;
        void*              _34;
        void*              _38;
        LiveActorGroup*    mAllActors;
        void*              _40;

public:
        ClippingDirector* getClippingDirector() const
        {
                return mClippingDirector;
        }

        ExecuteDirector* getExecuteDirector() const
        {
                return mExecuteDirector;
        }

        LiveActorGroup* getAllActors() const
        {
                return mAllActors;
        }

        void update();

        void endInit();

public:
        LiveActorKit( int groupBufSize );
};

void          initLiveActorKit( LiveActorKit* kit );
LiveActorKit* getLiveActorKit();

void executeDraw( const LiveActorKit* kit, const char* );
void executeDrawList( const LiveActorKit* kit, const char*, const char* );

} // namespace al
```


