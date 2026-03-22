

# File alSubActorFunction.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**LiveActor**](dir_834378260339034a4005b37c1f1948d3.md) **>** [**alSubActorFunction.h**](al_sub_actor_function_8h.md)

[Go to the documentation of this file](al_sub_actor_function_8h.md)


```C++
#pragma once

namespace al
{
class SubActorKeeper;
}

class alSubActorFunction
{
public:
        static void trySyncAlive( al::SubActorKeeper* p );
        static void trySyncDead( al::SubActorKeeper* p );

        static void trySyncClippingStart( al::SubActorKeeper* p );
        static void trySyncClippingEnd( al::SubActorKeeper* p );

        static void tryCalcAnim( al::SubActorKeeper* p );
};
```


