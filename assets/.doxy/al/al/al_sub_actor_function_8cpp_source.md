

# File alSubActorFunction.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**src**](dir_d8628e97cbd71936d4b5fb3774410590.md) **>** [**LiveActor**](dir_8d17faa1063b24478b1232799869255d.md) **>** [**alSubActorFunction.cpp**](al_sub_actor_function_8cpp.md)

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


