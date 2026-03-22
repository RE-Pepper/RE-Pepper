

# File alAreaShapeCube.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**src**](dir_6f98f21a57298fb921e921b3faae2f7d.md) **>** [**AreaObj**](dir_dde2c1009da0509eb11ce4bb60c98584.md) **>** [**alAreaShapeCube.cpp**](al_area_shape_cube_8cpp.md)

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


