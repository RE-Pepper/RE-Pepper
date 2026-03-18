

# File alLiveActorKit.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**LiveActor**](dir_ae80ee5cf9da1054faf149dc2356c7ac.md) **>** [**alLiveActorKit.h**](al_live_actor_kit_8h.md)

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


