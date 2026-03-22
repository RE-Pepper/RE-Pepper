

# File alActorStateBase.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**Nerve**](dir_cea16a3cd0068aab539e5f3441822a40.md) **>** [**alActorStateBase.h**](al_actor_state_base_8h.md)

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


