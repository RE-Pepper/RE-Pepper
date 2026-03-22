

# File alExecuteTableHolder.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**src**](dir_6f98f21a57298fb921e921b3faae2f7d.md) **>** [**Execute**](dir_4b230cb65e2bae93fe6927972e49843b.md) **>** [**alExecuteTableHolder.cpp**](al_execute_table_holder_8cpp.md)

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


