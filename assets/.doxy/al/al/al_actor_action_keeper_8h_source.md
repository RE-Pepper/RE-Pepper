

# File alActorActionKeeper.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**LiveActor**](dir_834378260339034a4005b37c1f1948d3.md) **>** [**alActorActionKeeper.h**](al_actor_action_keeper_8h.md)

[Go to the documentation of this file](al_actor_action_keeper_8h.md)


```C++
#pragma once

namespace al
{

class ActionAnimCtrl;

class LiveActor;

class ActorActionKeeper
{
private:
        void*           _0;
        void*           _4;
        ActionAnimCtrl* mActionAnimCtrl;

public:
        void tryStartActionNoAnim( const char* name );
};

void startHitReaction( const LiveActor* actor, const char* name );

#define AL_LIVEACTOR_REACTION( TYPE ) void startHitReaction##TYPE( const LiveActor* actor );

AL_LIVEACTOR_REACTION( Appear )
AL_LIVEACTOR_REACTION( Disappear )
AL_LIVEACTOR_REACTION( PressDown )
AL_LIVEACTOR_REACTION( Death )
AL_LIVEACTOR_REACTION( Hit )
AL_LIVEACTOR_REACTION( BlowHit )
AL_LIVEACTOR_REACTION( Break )
AL_LIVEACTOR_REACTION( Start )
AL_LIVEACTOR_REACTION( End )
AL_LIVEACTOR_REACTION( OnGround )
AL_LIVEACTOR_REACTION( Get )

#undef AL_LIVEACTOR_REACTION

} // namespace al
```


