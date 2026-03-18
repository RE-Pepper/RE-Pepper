

# File alEffectSystem.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Effect**](dir_132b48dc7483d6ef85515d7c8db2516a.md) **>** [**alEffectSystem.h**](al_effect_system_8h.md)

[Go to the documentation of this file](al_effect_system_8h.md)


```C++
#pragma once

#include <heap/seadHeap.h>

namespace al
{

class EffectSystem
{
private:
        sead::Heap* _0;

public:
        void init();
        void startScene();

public:
        EffectSystem();
};

} // namespace al
```


