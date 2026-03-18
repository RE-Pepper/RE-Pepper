

# File alExecuteRequestKeeper.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Execute**](dir_a22e87c788a1f2e7d5d5429c64840582.md) **>** [**alExecuteRequestKeeper.h**](al_execute_request_keeper_8h.md)

[Go to the documentation of this file](al_execute_request_keeper_8h.md)


```C++
#pragma once

#include <stddef.h>

namespace al
{

class LiveActor;

class ExecuteRequestKeeper
{
private:
        u8 _0[ 0x10 ];

public:
        void request( LiveActor*, int );

public:
        ExecuteRequestKeeper( size_t );
};

} // namespace al
```


