

# File alLiveActorGroup.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**src**](dir_d8628e97cbd71936d4b5fb3774410590.md) **>** [**LiveActor**](dir_8d17faa1063b24478b1232799869255d.md) **>** [**alLiveActorGroup.cpp**](al_live_actor_group_8cpp.md)

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


