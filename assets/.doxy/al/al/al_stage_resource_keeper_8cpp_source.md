

# File alStageResourceKeeper.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**src**](dir_6f98f21a57298fb921e921b3faae2f7d.md) **>** [**Stage**](dir_5711be3bb70244779513d118f4c8331f.md) **>** [**alStageResourceKeeper.cpp**](al_stage_resource_keeper_8cpp.md)

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


