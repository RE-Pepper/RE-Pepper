

# File alAreaShape.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**src**](dir_d8628e97cbd71936d4b5fb3774410590.md) **>** [**AreaObj**](dir_79b1387a1d862a1aa194fcab079affc0.md) **>** [**alAreaShape.cpp**](al_area_shape_8cpp.md)

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


