

# File alLiveActorFlag.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**src**](dir_6f98f21a57298fb921e921b3faae2f7d.md) **>** [**LiveActor**](dir_8deca751c472e73f27f3806d878e75d2.md) **>** [**alLiveActorFlag.cpp**](al_live_actor_flag_8cpp.md)

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


