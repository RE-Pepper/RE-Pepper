

# File alAreaObj.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**src**](dir_6f98f21a57298fb921e921b3faae2f7d.md) **>** [**AreaObj**](dir_dde2c1009da0509eb11ce4bb60c98584.md) **>** [**alAreaObj.cpp**](al_area_obj_8cpp.md)

[Go to the documentation of this file](al_area_obj_8cpp.md)


```C++
#include <AreaObj/alAreaObj.h>
#include <AreaObj/alAreaShape.h>
#include <Stage/alStageSwitchKeeper.h>

namespace al
{

#ifdef NON_MATCHING
AreaObj::AreaObj( const char* name )
    : mName( name ), mAreaShape( nullptr ), mStageSwitchKeeper( nullptr ), _10( sead::Matrix34f::ident ),
      _40( nullptr ), _44( -1 ), _48( 1 )
{
}
#endif

StageSwitchKeeper* AreaObj::getStageSwitchKeeper() const
{
        return mStageSwitchKeeper;
}

void AreaObj::initStageSwitchKeeper()
{
        mStageSwitchKeeper = new StageSwitchKeeper;
}

bool AreaObj::isInVolume( const sead::Vector3f& trans ) const
{
        if ( _48 )
                return mAreaShape->isInVolume( trans );
        return false;
}

} // namespace al
```


