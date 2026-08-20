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
