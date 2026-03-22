

# File alStageResourceKeeper.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**Stage**](dir_daa0595dec2e5cfbe17969deed9028aa.md) **>** [**alStageResourceKeeper.h**](al_stage_resource_keeper_8h.md)

[Go to the documentation of this file](al_stage_resource_keeper_8h.md)


```C++
#pragma once

#include <heap/seadHeap.h>

namespace al
{
class Resource;

class StageResourceKeeper
{
private:
        al::Resource** mResources;

public:
        void initAndLoadResource( const char* stageName, int scenario, sead::Heap* heap );

        al::Resource* getResourceDesign() const;
        al::Resource* getResourceMap() const;
        al::Resource* getResourceSound() const;

public:
        StageResourceKeeper();
};

} // namespace al
```


