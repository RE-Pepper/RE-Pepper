

# File alStageSwitchAccesser.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**Stage**](dir_daa0595dec2e5cfbe17969deed9028aa.md) **>** [**alStageSwitchAccesser.h**](al_stage_switch_accesser_8h.md)

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


