

# File alActorPoseFunction.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**LiveActor**](dir_834378260339034a4005b37c1f1948d3.md) **>** [**alActorPoseFunction.h**](al_actor_pose_function_8h.md)

[Go to the documentation of this file](al_actor_pose_function_8h.md)


```C++
#pragma once

#include <LiveActor/alActorPoseKeeper.h>
#include <LiveActor/alLiveActor.h>
#include <math/seadMatrix.h>

class alActorPoseFunction
{
public:
        static void calcBaseMtx( sead::Matrix34f* out, const al::LiveActor* actor )
        {
                actor->mActorPoseKeeper->calcBaseMtx( out );
        }
};
```


