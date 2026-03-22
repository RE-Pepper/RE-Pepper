

# File alRailMoveMovement.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**Rail**](dir_c8bcdc1e1ae46381fd1d0b5e3e0c3157.md) **>** [**alRailMoveMovement.h**](al_rail_move_movement_8h.md)

[Go to the documentation of this file](al_rail_move_movement_8h.md)


```C++
#pragma once

#include <LiveActor/alLiveActor.h>
#include <Nerve/alHostStateBase.h>

namespace al
{

class RailMoveMovement : public HostStateBase<LiveActor>
{
private:
        float mSpeed;
        u32   mMoveType;

public:
        void exeMove();

public:
        RailMoveMovement( LiveActor* host, const ActorInitInfo& info, const char* speedParamName = "Arg0", const char* moveTypeParamName = "Arg1" );
};

} // namespace al
```


