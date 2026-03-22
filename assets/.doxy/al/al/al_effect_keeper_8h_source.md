

# File alEffectKeeper.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**Effect**](dir_ff51cf8ab20432040552f45403bead0b.md) **>** [**alEffectKeeper.h**](al_effect_keeper_8h.md)

[Go to the documentation of this file](al_effect_keeper_8h.md)


```C++
#pragma once

#include <math/seadVector.h>

namespace al
{

class EffectKeeper
{
public:
        void update();
        void deleteAndClearEffectAll();
};

class IUseEffectKeeper
{
public:
        virtual EffectKeeper* getEffectKeeper() const = 0;
};

void emitEffect( IUseEffectKeeper* p, const char* name, const sead::Vector3f* at = nullptr );
bool tryEmitEffect( IUseEffectKeeper* p, const char* name );

} // namespace al
```


