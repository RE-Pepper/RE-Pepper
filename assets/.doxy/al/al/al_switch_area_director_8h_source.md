

# File alSwitchAreaDirector.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**AreaObj**](dir_65406aa8482a23b720984def0cee3032.md) **>** [**alSwitchAreaDirector.h**](al_switch_area_director_8h.md)

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


