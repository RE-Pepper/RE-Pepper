

# File alAreaShapeCube.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**src**](dir_d8628e97cbd71936d4b5fb3774410590.md) **>** [**AreaObj**](dir_79b1387a1d862a1aa194fcab079affc0.md) **>** [**alAreaShapeCube.cpp**](al_area_shape_cube_8cpp.md)

[Go to the documentation of this file](al_area_shape_cube_8cpp.md)


```C++
#include <AreaObj/alAreaShapeCube.h>

namespace al
{

AreaShapeCube::AreaShapeCube( bool isCubeBase ) : mIsCubeBase( isCubeBase )
{
}

#ifdef NON_MATCHING

// comparison is different
bool AreaShapeCube::isInVolume( const sead::Vector3f& trans ) const
{
        sead::Vector3f localPos = sead::Vector3f::zero;
        calcLocalPos( &localPos, trans );
        sead::Vector2f bottomTopYBounds =
                mIsCubeBase ? sead::Vector2f( 0, 1000 ) : sead::Vector2f( -500, 500 );

        return localPos.y > bottomTopYBounds.x && localPos.y < bottomTopYBounds.y &&
               localPos.x > -500 && localPos.y < 500 && localPos.z > -500 && localPos.z < 500;
}
#endif

} // namespace al
```


