

# File alExecuteTableHolder.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**src**](dir_d8628e97cbd71936d4b5fb3774410590.md) **>** [**Execute**](dir_f4cdcb9032257672e779ef34d2d06033.md) **>** [**alExecuteTableHolder.cpp**](al_execute_table_holder_8cpp.md)

[Go to the documentation of this file](al_execute_table_holder_8cpp.md)


```C++
#include <Execute/alExecuteRequestKeeper.h>
#include <Execute/alExecuteTableHolder.h>
#include <LiveActor/alActorExecuteInfo.h>
#include <LiveActor/alLiveActor.h>
#include <LiveActor/alLiveActorKit.h>

namespace al
{

void registerExecutorUser( IUseExecutor* p, const char* name )
{
        al::getLiveActorKit()->getExecuteDirector()->registerUser( p, name );
}

void registerExecutorFunctor( const FunctorBase& base, const char* name )
{
        al::getLiveActorKit()->getExecuteDirector()->registerFunctor( base, name );
}

void registerExecutorFunctorDraw( const FunctorBase& base, const char* name )
{
        al::getLiveActorKit()->getExecuteDirector()->registerFunctorDraw( base, name );
}

} // namespace al

namespace alActorSystemFunction
{

void addToExecutorMovement( al::LiveActor* actor )
{
        actor->getActorExecuteInfo()->getRequestKeeper()->request( actor, 0 );
}

} // namespace alActorSystemFunction
```


