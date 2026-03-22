

# File alAreaShape.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**src**](dir_6f98f21a57298fb921e921b3faae2f7d.md) **>** [**AreaObj**](dir_dde2c1009da0509eb11ce4bb60c98584.md) **>** [**alAreaShape.cpp**](al_area_shape_8cpp.md)

[Go to the documentation of this file](al_area_shape_8cpp.md)


```C++
#include <AreaObj/alAreaShape.h>

namespace al
{

AreaShape::AreaShape() : mBaseMtxPtr( nullptr ), mScale( sead::Vector3f( 1, 1, 1 ) )
{
}

/* TODO: Move this to header */
void AreaShape::setScale( const sead::Vector3f& scale )
{
        mScale = scale;
}

} // namespace al
```


