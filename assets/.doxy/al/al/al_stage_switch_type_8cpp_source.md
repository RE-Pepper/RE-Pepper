

# File alStageSwitchType.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**src**](dir_d8628e97cbd71936d4b5fb3774410590.md) **>** [**Stage**](dir_1105584207b8da44b58906e6f5240647.md) **>** [**alStageSwitchType.cpp**](al_stage_switch_type_8cpp.md)

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


