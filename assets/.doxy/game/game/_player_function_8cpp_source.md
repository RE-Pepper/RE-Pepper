

# File PlayerFunction.cpp

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**src**](dir_47d28cd3eb946f860e1fe0f4e720b9c2.md) **>** [**Player**](dir_9f791c72b7e31512581b67600bde1506.md) **>** [**PlayerFunction.cpp**](_player_function_8cpp.md)

[Go to the documentation of this file](_player_function_8cpp.md)


```C++
#include "Player/PlayerFunction.h"

#include <LiveActor/alActorPoseKeeper.h>
#include <System/Application.h>

#include "Player/PlayerActor.h"

namespace rp
{

#pragma no_inline
#ifdef NON_MATCHING

// linker shenanigans
PlayerActor* getPlayerActor()
{
        return Application::instance()->getPlayerActor();
}

const sead::Vector3f& getPlayerPos()
{
        return al::getTrans( getPlayerActor() );
}
#endif

} // namespace rp
```


