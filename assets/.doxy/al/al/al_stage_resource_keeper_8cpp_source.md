

# File alStageResourceKeeper.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**src**](dir_d8628e97cbd71936d4b5fb3774410590.md) **>** [**Stage**](dir_1105584207b8da44b58906e6f5240647.md) **>** [**alStageResourceKeeper.cpp**](al_stage_resource_keeper_8cpp.md)

[Go to the documentation of this file](al_stage_resource_keeper_8cpp.md)


```C++
#include <Stage/alStageResourceKeeper.h>

namespace al
{

StageResourceKeeper::StageResourceKeeper() : mResources( nullptr )
{
}

al::Resource* StageResourceKeeper::getResourceDesign() const
{
        return mResources[ 1 ];
}

al::Resource* StageResourceKeeper::getResourceMap() const
{
        return mResources[ 0 ];
}

al::Resource* StageResourceKeeper::getResourceSound() const
{
        return mResources[ 2 ];
}

} // namespace al
```


