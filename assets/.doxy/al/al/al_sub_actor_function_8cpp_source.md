

# File alSubActorFunction.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**src**](dir_6f98f21a57298fb921e921b3faae2f7d.md) **>** [**LiveActor**](dir_8deca751c472e73f27f3806d878e75d2.md) **>** [**alSubActorFunction.cpp**](al_sub_actor_function_8cpp.md)

[Go to the documentation of this file](al_sub_actor_function_8cpp.md)


```C++
#include <LiveActor/alLiveActor.h>
#include <LiveActor/alLiveActorFunction.h>
#include <LiveActor/alSubActorFunction.h>
#include <LiveActor/alSubActorKeeper.h>

void alSubActorFunction::trySyncAlive( al::SubActorKeeper* p )
{
        for ( int i = 0; i < p->mSubActors.size(); i++ )
        {
                al::SubActorKeeper::Entry* subActor = p->mSubActors.unsafeAt( i );
                if ( subActor->_8 & 1 )
                        subActor->actor->makeActorAppeared();
        }
}

void alSubActorFunction::trySyncDead( al::SubActorKeeper* p )
{
        for ( int i = 0; i < p->mSubActors.size(); i++ )
        {
                al::SubActorKeeper::Entry* subActor = p->mSubActors.unsafeAt( i );
                if ( subActor->_8 & 1 )
                        subActor->actor->makeActorDead();
        }
}

void alSubActorFunction::trySyncClippingStart( al::SubActorKeeper* p )
{
        for ( int i = 0; i < p->mSubActors.size(); i++ )
        {
                al::SubActorKeeper::Entry* subActor = p->mSubActors.unsafeAt( i );
                if ( subActor->_8 & 2 && al::isAlive( subActor->actor ) && !al::isClipped( subActor->actor ) )
                        subActor->actor->startClipped();
        }
}

void alSubActorFunction::trySyncClippingEnd( al::SubActorKeeper* p )
{
        for ( int i = 0; i < p->mSubActors.size(); i++ )
        {
                al::SubActorKeeper::Entry* subActor = p->mSubActors.unsafeAt( i );
                if ( subActor->_8 & 2 && al::isAlive( subActor->actor ) && al::isClipped( subActor->actor ) )
                        subActor->actor->endClipped();
        }
}

void alSubActorFunction::tryCalcAnim( al::SubActorKeeper* p )
{
        for ( int i = 0; i < p->mSubActors.size(); i++ )
        {
                al::SubActorKeeper::Entry* subActor = p->mSubActors.unsafeAt( i );
                if ( subActor->_8 & 8 && al::isAlive( subActor->actor ) )
                        subActor->actor->calcAnim();
        }
}
```


