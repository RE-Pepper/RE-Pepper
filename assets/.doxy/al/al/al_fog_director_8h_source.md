

# File alFogDirector.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Fog**](dir_cf3b936e0891eb65a94b757a33d015d1.md) **>** [**alFogDirector.h**](al_fog_director_8h.md)

[Go to the documentation of this file](al_fog_director_8h.md)


```C++
#pragma once

#include <Execute/alExecuteDirector.h>
#include <Yaml/alByamlIter.h>

namespace al
{

class FogDirector : public IUseExecutor
{
public:
        u8*       _4[ 0x78 ];
        ByamlIter _7C;

public:
        void endInit();

public:
        virtual void execute();
};

} // namespace al
```


