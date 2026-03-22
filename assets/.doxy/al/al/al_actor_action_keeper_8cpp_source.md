

# File alActorActionKeeper.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**src**](dir_6f98f21a57298fb921e921b3faae2f7d.md) **>** [**LiveActor**](dir_8deca751c472e73f27f3806d878e75d2.md) **>** [**alActorActionKeeper.cpp**](al_actor_action_keeper_8cpp.md)

[Go to the documentation of this file](al_actor_action_keeper_8cpp.md)


```C++
#include <LiveActor/alActorActionKeeper.h>

namespace al
{

#define AL_LIVEACTOR_REACTION( TYPE, NAME )                   \
        void startHitReaction##TYPE( const LiveActor* actor ) \
        {                                                     \
                startHitReaction( actor, NAME );              \
        }

AL_LIVEACTOR_REACTION( Appear, "出現" )
AL_LIVEACTOR_REACTION( Disappear, "消滅" )
AL_LIVEACTOR_REACTION( PressDown, "踏み潰され" )
AL_LIVEACTOR_REACTION( Death, "死亡" )
AL_LIVEACTOR_REACTION( Hit, "命中" )
AL_LIVEACTOR_REACTION( BlowHit, "吹き飛びヒット" )
AL_LIVEACTOR_REACTION( Break, "破壊" )
AL_LIVEACTOR_REACTION( Start, "開始" )
AL_LIVEACTOR_REACTION( End, "終了" )
AL_LIVEACTOR_REACTION( OnGround, "着地" )
AL_LIVEACTOR_REACTION( Get, "取得" )

#undef AL_LIVEACTOR_REACTION

} // namespace al
```


