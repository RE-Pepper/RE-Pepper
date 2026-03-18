

# File alActorStateBase.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Nerve**](dir_0d638fa675477dde0733aed9f19ea6f2.md) **>** [**alActorStateBase.h**](al_actor_state_base_8h.md)

[Go to the documentation of this file](al_actor_state_base_8h.md)


```C++
#pragma once

#include <Nerve/alNerveStateBase.h>

namespace al
{
class LiveActor;

class ActorStateBase : public al::NerveStateBase
{
protected:
        LiveActor* const mHost;

public:
        ActorStateBase( const char* name, LiveActor* host ) : NerveStateBase( name ), mHost( host )
        {
        }
};

} // namespace al
```


