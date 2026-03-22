

# File alSwitchAreaDirector.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**src**](dir_6f98f21a57298fb921e921b3faae2f7d.md) **>** [**AreaObj**](dir_dde2c1009da0509eb11ce4bb60c98584.md) **>** [**alSwitchAreaDirector.cpp**](al_switch_area_director_8cpp.md)

[Go to the documentation of this file](al_switch_area_director_8cpp.md)


```C++
#include <AreaObj/alSwitchAreaDirector.h>
#include <AreaObj/alSwitchKeepOnAreaGroup.h>
#include <AreaObj/alSwitchOnAreaGroup.h>

#include "Player/PlayerFunction.h" // GAME

namespace al
{

SwitchAreaDirector::SwitchAreaDirector()
    : LiveActor( "スイッチエリアディレクター" ), mSwitchOnAreaGroup( nullptr ),
      mSwitchKeepOnAreaGroup( nullptr )
{
}

#ifdef NON_MATCHING

// not using stm for vector copy
void SwitchAreaDirector::movement()
{
        sead::Vector3f pos = rp::getPlayerPos();
        if ( mSwitchOnAreaGroup )
                mSwitchOnAreaGroup->update( pos );
        if ( mSwitchKeepOnAreaGroup )
                mSwitchKeepOnAreaGroup->update( pos );
}
#endif

} // namespace al
```


