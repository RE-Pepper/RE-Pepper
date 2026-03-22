

# File alLiveActorKit.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**src**](dir_6f98f21a57298fb921e921b3faae2f7d.md) **>** [**LiveActor**](dir_8deca751c472e73f27f3806d878e75d2.md) **>** [**alLiveActorKit.cpp**](al_live_actor_kit_8cpp.md)

[Go to the documentation of this file](al_live_actor_kit_8cpp.md)


```C++
#include <Clipping/alClippingDirector.h>
#include <Collision/alCollisionDirector.h>
#include <Effect/alEffectSystem.h>
#include <Execute/alExecuteDirector.h>
#include <Fog/alFogDirector.h>
#include <Functor/alFunctorV0F.h>
#include <LiveActor/alLiveActorGroup.h>
#include <LiveActor/alLiveActorKit.h>
#include <System/Application.h>

namespace al
{

LiveActorKit::LiveActorKit( int groupBufSize )
    : mAllActorsBufferSize( groupBufSize ), mExecuteDirector( nullptr ), mEffectSystem( nullptr ),
      _C( nullptr ), _10( nullptr ), mFogDirector( nullptr ), _18( nullptr ), _1C( nullptr ), _20( nullptr ),
      mClippingDirector( nullptr ), mCollisionDirector( nullptr ), mHitSensorDirector( nullptr ),
      _30( nullptr ), _34( nullptr ), _38( nullptr ), mAllActors( nullptr ), _40( nullptr )
{
        mAllActors = new LiveActorGroup( "全てのアクター", mAllActorsBufferSize );
}

extern "C" void fn_00240350();
extern "C" void fn_001e8a64();

extern "C" void fn_001cc9b0( const char*, const FunctorV0F& );

#ifdef NON_MATCHING

// loop is weird
void LiveActorKit::endInit()
{
        fn_001cc9b0( "プレイヤー影ボリュームのフィル", FunctorV0F( fn_00240350 ) );
        fn_001cc9b0( "影ボリュームのフィル", FunctorV0F( fn_001e8a64 ) );
        mEffectSystem->startScene();
        mExecuteDirector->createExecutorListTable();
        mCollisionDirector->endInit();
        mFogDirector->endInit();
        mClippingDirector->endInit();
        sead::PtrArray<LiveActor> actors = mAllActors->getArray<LiveActor>();
        for ( int i = 0; i < actors.size(); i++ )
                actors[ i ]->initAfterPlacement();
}
#endif

void initLiveActorKit( LiveActorKit* kit )
{
        al::getApplication()->setLiveActorKit( kit );
}

LiveActorKit* getLiveActorKit()
{
        return al::getApplication()->getLiveActorKit();
}

} // namespace al
```


