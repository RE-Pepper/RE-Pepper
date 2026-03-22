

# File alExecuteTableHolder.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**Execute**](dir_b0627dbdf07c5051f864ccb41a35881f.md) **>** [**alExecuteTableHolder.h**](al_execute_table_holder_8h.md)

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


