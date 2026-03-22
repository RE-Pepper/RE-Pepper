

# File alLiveActorGroup.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**src**](dir_6f98f21a57298fb921e921b3faae2f7d.md) **>** [**LiveActor**](dir_8deca751c472e73f27f3806d878e75d2.md) **>** [**alLiveActorGroup.cpp**](al_live_actor_group_8cpp.md)

[Go to the documentation of this file](al_live_actor_group_8cpp.md)


```C++
#include <LiveActor/alLiveActorGroup.h>

namespace al
{

#ifdef NON_MATCHING
LiveActorGroup::LiveActorGroup( const char* name, int bufSize )
    : mName( name )
{
        mActors.allocBufferInline( bufSize );
}
#endif

void LiveActorGroup::registerActor( LiveActor* actor )
{
        mActors.pushBack( actor );
}

void LiveActorGroup::killAll()
{
        for ( int i = 0; i < mActors.size(); i++ )
                mActors.unsafeAt( i )->kill();
}

void LiveActorGroup::makeActorDeadAll()
{
        for ( int i = 0; i < mActors.size(); i++ )
                mActors.unsafeAt( i )->makeActorDead();
}

} // namespace al
```


