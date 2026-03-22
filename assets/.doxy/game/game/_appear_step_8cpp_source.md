

# File AppearStep.cpp

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**src**](dir_47d28cd3eb946f860e1fe0f4e720b9c2.md) **>** [**MapObj**](dir_d5af9f6f62d27d9e3db1b7ff0fb6c0e1.md) **>** [**AppearStep.cpp**](_appear_step_8cpp.md)

[Go to the documentation of this file](_appear_step_8cpp.md)


```C++
#include "MapObj/AppearStep.h"

#include <Functor/alFunctorV0M.h>
#include <LiveActor/alActorInitUtil.h>
#include <LiveActor/alActorPoseKeeper.h>
#include <LiveActor/alLiveActorFunction.h>
#include <Nerve/alNerve.h>
#include <Nerve/alNerveFunction.h>
#include <Stage/alStageSwitchKeeper.h>

namespace NrvAppearStep
{

NERVE_DEF( AppearStep, Appear )
NERVE_DEF( AppearStep, Wait )
NERVE_DEF( AppearStep, Disappear )
NERVE_DEF( AppearStep, End )

} // namespace NrvAppearStep

AppearStep::AppearStep( const sead::SafeString& name ) : MapObjActor( name )
{
}

#ifdef NON_MATCHING

void AppearStep::init( const al::ActorInitInfo& info )
{
        al::initActorPoseTQSV( this );
        al::initMapPartsActor( this, info );
        al::initNerve( this, &NrvAppearStep::End );
        al::initStageSwitchAppear( this, info );
        al::listenStageSwitchOnAppear(
                this, al::FunctorV0M<AppearStep*, void ( AppearStep::* )()>( this, &AppearStep::startAppear ), al::FunctorV0M<AppearStep*, void ( AppearStep::* )()>( this, &AppearStep::startDisappear ) )
                ? makeActorDead()
                : makeActorAppeared();
}

#endif

void AppearStep::startAppear()
{
        if ( al::isNerve( this, &NrvAppearStep::Disappear ) || al::isNerve( this, &NrvAppearStep::End ) )
        {
                al::invalidateClipping( this );
                al::setNerve( this, &NrvAppearStep::Appear );
                makeActorAppeared();
        }
}

void AppearStep::startDisappear()
{
        if ( al::isNerve( this, &NrvAppearStep::Appear ) || al::isNerve( this, &NrvAppearStep::Wait ) )
        {
                al::invalidateClipping( this );
                al::setNerve( this, &NrvAppearStep::Disappear );
        }
}

void AppearStep::exeAppear()
{
        if ( al::isFirstStep( this ) )
                al::tryStartAction( this, "Appear" );

        if ( al::isActionEnd( this ) )
                al::setNerve( this, &NrvAppearStep::Wait );
}

void AppearStep::exeWait()
{
        if ( al::isFirstStep( this ) )
                al::validateClipping( this );
}

void AppearStep::exeDisappear()
{
        if ( al::isFirstStep( this ) )
                al::tryStartAction( this, "Disappear" );

        if ( al::isActionEnd( this ) )
                al::setNerve( this, &NrvAppearStep::End );
}

void AppearStep::exeEnd()
{
        if ( al::isFirstStep( this ) )
        {
                al::validateClipping( this );
                kill();
        }
}
```


