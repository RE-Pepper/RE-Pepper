

# File alStageSwitchKeeper.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**src**](dir_d8628e97cbd71936d4b5fb3774410590.md) **>** [**Stage**](dir_1105584207b8da44b58906e6f5240647.md) **>** [**alStageSwitchKeeper.cpp**](al_stage_switch_keeper_8cpp.md)

[Go to the documentation of this file](al_stage_switch_keeper_8cpp.md)


```C++
#include <Stage/alStageSwitchAccesser.h>
#include <Stage/alStageSwitchKeeper.h>

namespace al
{

#ifdef NON_MATCHING
StageSwitchKeeper::StageSwitchKeeper() : mSwitches( nullptr ), mSwitchCount( 0 )
{
        mSwitchCount = 5; // optimized away
        mSwitches    = new StageSwitchAccesser[ 5 ];
}
#endif

StageSwitchAccesser* StageSwitchKeeper::getStageSwitchAccesser( int type )
{
        return &mSwitches[ type ];
}

} // namespace al
```


