

# File alExecuteTableHolder.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Execute**](dir_a22e87c788a1f2e7d5d5429c64840582.md) **>** [**alExecuteTableHolder.h**](al_execute_table_holder_8h.md)

[Go to the documentation of this file](al_execute_table_holder_8h.md)


```C++
#pragma once

#include <Execute/alExecuteDirector.h>

namespace al
{

class LiveActor;

void registerExecutorUser( IUseExecutor* p, const char* name );
void registerExecutorFunctor( const FunctorBase& base, const char* name );
void registerExecutorFunctorDraw( const FunctorBase& base, const char* name );

} // namespace al

namespace alActorSystemFunction
{

void addToExecutorMovement( al::LiveActor* actor );
void removeFromExecutorDraw( al::LiveActor* actor );

} // namespace alActorSystemFunction
```


