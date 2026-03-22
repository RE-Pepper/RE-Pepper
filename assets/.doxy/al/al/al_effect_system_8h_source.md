

# File alEffectSystem.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**Effect**](dir_ff51cf8ab20432040552f45403bead0b.md) **>** [**alEffectSystem.h**](al_effect_system_8h.md)

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


