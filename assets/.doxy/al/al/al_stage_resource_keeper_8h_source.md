

# File alStageResourceKeeper.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Stage**](dir_5b0b61705299d400abf6aff2e591c6a0.md) **>** [**alStageResourceKeeper.h**](al_stage_resource_keeper_8h.md)

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


