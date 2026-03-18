

# File alLiveActorFlag.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**src**](dir_d8628e97cbd71936d4b5fb3774410590.md) **>** [**LiveActor**](dir_8d17faa1063b24478b1232799869255d.md) **>** [**alLiveActorFlag.cpp**](al_live_actor_flag_8cpp.md)

[Go to the documentation of this file](al_live_actor_flag_8cpp.md)


```C++
#include <LiveActor/alLiveActor.h>
#include <LiveActor/alLiveActorFlag.h>

namespace al
{

LiveActorFlag::LiveActorFlag()
    : isDead( true ), isClipped( false ), isInvalidClipping( true ), isDrawClipping( false ), flag5( false ),
      isHideModel( false ), isOffCollide( true ), flag8( false ), isValidMaterialCode( false )
{
}

} // namespace al
```


