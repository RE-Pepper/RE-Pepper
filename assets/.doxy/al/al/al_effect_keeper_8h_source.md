

# File alEffectKeeper.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Effect**](dir_132b48dc7483d6ef85515d7c8db2516a.md) **>** [**alEffectKeeper.h**](al_effect_keeper_8h.md)

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


