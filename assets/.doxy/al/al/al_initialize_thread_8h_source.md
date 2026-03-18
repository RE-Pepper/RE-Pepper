

# File alInitializeThread.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**System**](dir_29a5069bbf312f731d8cb4e203fae6bc.md) **>** [**alInitializeThread.h**](al_initialize_thread_8h.md)

[Go to the documentation of this file](al_initialize_thread_8h.md)


```C++
#pragma once

#include <heap/seadHeap.h>

namespace al
{
class FunctorBase;

void createAndStartInitializeThread( sead::Heap* heap, int stackSize, const FunctorBase& func );

} // namespace al
```


