

# File alFogDirector.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**Fog**](dir_82d961fedc01bae4a429681f03079cb6.md) **>** [**alFogDirector.h**](al_fog_director_8h.md)

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


