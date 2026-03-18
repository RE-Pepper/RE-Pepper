

# File alSubActorFunction.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**LiveActor**](dir_ae80ee5cf9da1054faf149dc2356c7ac.md) **>** [**alSubActorFunction.h**](al_sub_actor_function_8h.md)

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


