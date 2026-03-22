

# File alStageSwitchType.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**src**](dir_6f98f21a57298fb921e921b3faae2f7d.md) **>** [**Stage**](dir_5711be3bb70244779513d118f4c8331f.md) **>** [**alStageSwitchType.cpp**](al_stage_switch_type_8cpp.md)

[Go to the documentation of this file](al_stage_switch_type_8cpp.md)


```C++
#pragma once

#include <Stage/alStageSwitchType.h>

namespace al
{

const char* getStageSwitchName( StageSwitchType type )
{
        switch ( type )
        {
        case StageSwitchType_Appear:
                return "SwitchAppear";
        case StageSwitchType_Kill:
                return "SwitchKill";
        case StageSwitchType_DeadOn:
                return "SwitchDeadOn";
        case StageSwitchType_A:
                return "SwitchA";
        case StageSwitchType_B:
                return "SwitchB";
        default:
                return "";
        }
}

} // namespace al
```


