

# File alRailMoveMovement.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Rail**](dir_eddceeca1a9539e4ec5247c1a556acdf.md) **>** [**alRailMoveMovement.h**](al_rail_move_movement_8h.md)

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


