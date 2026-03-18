

# File alStageSwitchType.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Stage**](dir_5b0b61705299d400abf6aff2e591c6a0.md) **>** [**alStageSwitchType.h**](al_stage_switch_type_8h.md)

[Go to the documentation of this file](al_stage_switch_type_8h.md)


```C++
#pragma once

namespace al
{

enum StageSwitchType
{
        StageSwitchType_Appear,
        StageSwitchType_Kill,
        StageSwitchType_DeadOn,
        StageSwitchType_A,
        StageSwitchType_B
};

const char* getStageSwitchName( StageSwitchType type );

} // namespace al
```


