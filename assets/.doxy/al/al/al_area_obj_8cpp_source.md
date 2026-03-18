

# File alAreaObj.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**src**](dir_d8628e97cbd71936d4b5fb3774410590.md) **>** [**AreaObj**](dir_79b1387a1d862a1aa194fcab079affc0.md) **>** [**alAreaObj.cpp**](al_area_obj_8cpp.md)

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


