

# File alExecuteRequestKeeper.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**Execute**](dir_b0627dbdf07c5051f864ccb41a35881f.md) **>** [**alExecuteRequestKeeper.h**](al_execute_request_keeper_8h.md)

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


