

# File alStageSwitchKeeper.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**src**](dir_6f98f21a57298fb921e921b3faae2f7d.md) **>** [**Stage**](dir_5711be3bb70244779513d118f4c8331f.md) **>** [**alStageSwitchKeeper.cpp**](al_stage_switch_keeper_8cpp.md)

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


