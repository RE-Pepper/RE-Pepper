

# File alStageSwitchAccesser.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Stage**](dir_5b0b61705299d400abf6aff2e591c6a0.md) **>** [**alStageSwitchAccesser.h**](al_stage_switch_accesser_8h.md)

[Go to the documentation of this file](al_stage_switch_accesser_8h.md)


```C++
#pragma once

#include <Placement/alPlacementInfo.h>
#include <Stage/alStageSwitchType.h>

namespace al
{

class StageSwitchAccesser
{
private:
        int mId;
        int mType;

public:
        int initWithPlacementInfo( StageSwitchType type1, const PlacementInfo& info, StageSwitchType type2 );

        bool isTypeKillDeadOn() const;
        int  fn_0024e734() const; // ?

public:
        StageSwitchAccesser();
};

} // namespace al
```


