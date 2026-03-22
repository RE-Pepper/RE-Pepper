

# File alSwitchAreaDirector.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**AreaObj**](dir_b7fc9200a4f7d26d4acf4ee56ee313c7.md) **>** [**alSwitchAreaDirector.h**](al_switch_area_director_8h.md)

[Go to the documentation of this file](al_switch_area_director_8h.md)


```C++
#pragma once

#include <LiveActor/alLiveActor.h>
#include <Scene/alISceneObj.h>

namespace al
{
class SwitchKeepOnAreaGroup;
class SwitchOnAreaGroup;

class SwitchAreaDirector : public LiveActor, public ISceneObj
{
private:
        SwitchOnAreaGroup*     mSwitchOnAreaGroup;
        SwitchKeepOnAreaGroup* mSwitchKeepOnAreaGroup;

public:
        virtual void movement();
        virtual void unk1();

public:
        SwitchAreaDirector();
};

} // namespace al
```


