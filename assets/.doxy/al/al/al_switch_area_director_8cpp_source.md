

# File alSwitchAreaDirector.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**src**](dir_d8628e97cbd71936d4b5fb3774410590.md) **>** [**AreaObj**](dir_79b1387a1d862a1aa194fcab079affc0.md) **>** [**alSwitchAreaDirector.cpp**](al_switch_area_director_8cpp.md)

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


